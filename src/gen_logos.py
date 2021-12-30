import argparse
import os
import cairosvg
import requests
import tempfile
from io import BytesIO
from PIL import Image

from config.constants import SUFFIXES
from config.token_data import TOKENS


L = 120
S = int(L/4)
OFFSET = int(L/60)
REM = L-S
STANDARD_DIM = (L, L)
MINI_DIM = (S, S)


dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logogen')
BASE_PATH = os.path.join(dir_path, 'base')
ASSET_PATH = os.path.join(os.path.dirname(os.path.dirname(dir_path)), 'assets')


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
  path = os.path.join(dir_path, 'components', '%s.png' % chain_name)
  img = Image.open(path).resize(MINI_DIM).convert('RGBA')
  img = add_margin(img, L-S-OFFSET, L-S-OFFSET, OFFSET, OFFSET)
  return img


def get_wormhole_logo():
  # bottom right
  path = os.path.join(dir_path, 'components', 'wormhole.png')
  img = Image.open(path).resize(MINI_DIM).convert('RGBA')
  img = add_margin(img, L-S-OFFSET, OFFSET, OFFSET, L-S-OFFSET)
  return img


def get_base_logo_url(name):
  for src, tok_dict in TOKENS.items():
    if name in tok_dict:
      if 'logo' in tok_dict[name]:
        return tok_dict[name]['logo']
      else:
        raise Exception('either give a link to logo in token_data.py')


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
      tmp = tempfile.NamedTemporaryFile()
      cairosvg.svg2png(url=logo_url, write_to=tmp.name)
      img = Image.open(tmp.name)
    # case 2: not
    else:
      response = requests.get(logo_url)
      img = Image.open(BytesIO(response.content))
  return img.resize(STANDARD_DIM).convert('RGBA')


def get_logo(name, wormhole=True, chain=None):
  stack = [get_base_logo(name)]
  if wormhole:
    stack.append(get_wormhole_logo())
  if chain is not None:
    stack.append(get_chain_logo(chain))

  composite = stack[0]
  for image in stack[1:]:
    composite = Image.alpha_composite(composite, image)
  return composite


def get_logo_path(name, wormhole=True, chain=None):
  filename = name
  if wormhole:
    filename += "_wh"
  return os.path.join(ASSET_PATH, '%s.png' % filename)


def write_logo(name, outpath, wormhole=True, chain=None):
  composite = get_logo(name, wormhole=wormhole, chain=chain)
  composite.save(outpath)


def write_logos(overwrite=False):
  for src_chain, tok_list in TOKENS.items():
    tokens = tok_list.keys()
    for tok in tokens:
      use_chain = tok[-2:] in SUFFIXES
      outpath = get_logo_path(tok, wormhole=True, chain=src_chain if use_chain else None)
      if not overwrite and os.path.exists(outpath):
        continue
      write_logo(tok, outpath, wormhole=True, chain=src_chain if use_chain else None)
      print('wrote %s' % outpath)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--overwrite', '-o', action='store_true')
  args, unknown_args = parser.parse_known_args()
  write_logos(overwrite=args.overwrite)
