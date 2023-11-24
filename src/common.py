import os


DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # wormhole-token-list
ASSET_PATH = os.path.join(DIR_PATH, 'assets')  # /assets
SRC_PATH = os.path.join(DIR_PATH, 'src')  # /src


def get_logo_path(name, wormhole=True):
  filename = name
  if wormhole:
    filename += "_wh"
  return os.path.join(ASSET_PATH, '%s.png' % filename)


def get_logo_raw_url(name):
  return 'https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/assets/%s_wh.png' % name
