import argparse
import os
import cairosvg
import requests
import tempfile
from io import BytesIO
from PIL import Image

from config.constants import SUFFIXES, SOURCE_INFO
from config.token_data import TOKENS

from common import SRC_PATH, ASSET_PATH, get_logo_path, get_logo_raw_url


L = 120  # dim of image
S = int(L * 0.5)  # dim of wormhole logo
OFFSET = 0
REM = L-S
STANDARD_DIM = (L, L)
MINI_DIM = (S, S)

PREVIEW_SIZE = 50  # 50x50

BASE_PATH = os.path.join(SRC_PATH, 'logogen', 'base')


def add_margin(pil_img, top, right, bottom, left, color=None):
  if color is None:
    color = (255, 255, 255, 0)
  width, height = pil_img.size
  new_width = width + right + left
  new_height = height + top + bottom
  result = Image.new(pil_img.mode, (new_width, new_height), color)
  result.paste(pil_img, (left, top))
  return result


def get_chain_logo(chain_name):
  # bottom left
  path = os.path.join(SRC_PATH, 'logogen', 'components', '%s.png' % chain_name)
  img = Image.open(path).resize(MINI_DIM).convert('RGBA')
  img = add_margin(img, L-S-OFFSET, L-S-OFFSET, OFFSET, OFFSET)
  return img


def get_wormhole_logo(style=None):
  # bottom right
  filename = 'wormhole' if style is None else 'wormhole_%s' % style
  path = os.path.join(SRC_PATH, 'logogen', 'components', filename + '.png')
  img = Image.open(path).resize(MINI_DIM).convert('RGBA')
  img = add_margin(img, OFFSET, OFFSET, L-S-OFFSET, L-S-OFFSET)
  return img


def get_base_logo_url(name):
  for src, tok_dict in TOKENS.items():
    if name in tok_dict:
      if 'logo' in tok_dict[name]:
        return tok_dict[name]['logo']
      else:
        raise Exception('token %s either needs logo in src/logogen/base, or link to logo in token_data.py' % name)


def get_base_logo(name):
  # if supplied in base dir use that
  filename = '%s.png' % name[:-2] if name[-2:] in SUFFIXES else '%s.png' % name
  if filename in os.listdir(BASE_PATH):
    img = Image.open(os.path.join(BASE_PATH, filename))
  # else get from internet
  else:
    logo_url = get_base_logo_url(name)
    logo_url = logo_url.replace('https://', 'http://')
    print(f'using for {name}: {logo_url}')

    # case 1: svg
    if logo_url.endswith('svg'):
      with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.close()
        cairosvg.svg2png(url=logo_url, write_to=tmp.name)
        with Image.open(tmp.name) as img:
          img = img.copy()
        os.unlink(tmp.name) 
    # case 2: not
    else:
      response = requests.get(logo_url, headers={'User-Agent': 'Mozilla/5.0'})
      img = Image.open(BytesIO(response.content))
  
  SMALLER_DIM = (L - 30, L - 30) # subtract to account for margins of base logo
  img = img.resize(SMALLER_DIM).convert('RGBA')

  # calculate margins to make it back to STANDARD_DIM
  margin_horizontal = (STANDARD_DIM[0] - SMALLER_DIM[0]) // 2
  margin_vertical = (STANDARD_DIM[1] - SMALLER_DIM[1]) // 2

  # add margins
  img = add_margin(img, margin_vertical, margin_horizontal, margin_vertical, margin_horizontal)

  return img


def get_logo(name, wormhole=True, chain=None, style=None):
  # Get base logo and add margin to it
  base_logo = get_base_logo(name)

  stack = [base_logo]
  if wormhole:
    stack.append(get_wormhole_logo(style=style))
  if chain is not None:
    stack.append(get_chain_logo(chain))

  composite = stack[0]
  for image in stack[1:]:
    composite = Image.alpha_composite(composite, image)
  return composite



def write_logo(name, outpath, wormhole=True, chain=None, style=None):
  try:
    composite = get_logo(name, wormhole=wormhole, chain=chain, style=style)
    composite.save(outpath)

    preview = composite.resize((PREVIEW_SIZE, PREVIEW_SIZE)).convert('RGBA')
    preview_path = outpath.replace('.png', '_small.png')
    preview.save(preview_path)
  except Exception as e:
    print(f'Error writing logo for {name}')

def write_logos(overwrite=False, style=None):
  text = ["by source chain:"]
  for chain_name, _, _, _ in SOURCE_INFO.values():
    text.append("* [%s](#source-chain-%s)" % (chain_name, chain_name.lower()))
  text.append("")
  for src_chain, tok_list in TOKENS.items():
    chain_name = SOURCE_INFO[src_chain][0]
    text.append('## source chain: %s' % chain_name )
    tokens = tok_list.keys()
    for tok in tokens:
      use_chain = tok[-2:] in SUFFIXES
      outpath = get_logo_path(tok, wormhole=True)
      if overwrite or not os.path.exists(outpath):
        write_logo(tok, outpath, wormhole=True, chain=src_chain if use_chain else None, style=style)
        print('wrote %s' % outpath)
      text.append('### %s' % tok)
      text.append('![%s](%s_wh.png)' % (tok, tok))
      text.append('![%s](%s_wh_small.png)' % (tok, tok))
      raw_path = get_logo_raw_url(tok)
      text.append('\n```\n%s\n```' % raw_path)
      text.append('')
    text.append('')
  outpath = os.path.join(ASSET_PATH, 'preview.md')
  header = "# logos"
  with open(outpath, 'w') as f:
    f.write(header + '\n\n' + '\n'.join(text))
  print('wrote %s' % outpath)



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--overwrite', '-o', action='store_true')
  parser.add_argument('--style', '-s', choices=['barecolor', 'color', 'thickgray', 'thingray', None])
  args, unknown_args = parser.parse_known_args()
  write_logos(overwrite=args.overwrite, style=args.style)