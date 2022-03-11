import json
import os
from collections import OrderedDict

IGNORE = [
  'ANGLE',
  'FKM',
  'FOUR',
  'LUCHOW',
  'TMI',
  'TRYB',
  'swtUST-9',
]

json_path = os.path.join(os.environ['HOME'], 'git/crypto/token-list/src/tokens/solana.tokenlist.json')
outpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'solana_wormhole_tokens.json')

f = open(json_path, 'r')
data = json.load(f, object_pairs_hook=OrderedDict)
token_list = data['tokens']

token_list.sort(key=lambda x: x['symbol'])

useful_data = OrderedDict()

for idx, token_data in enumerate(token_list):
  symbol = token_data['symbol']
  name = token_data['name']

  if token_data['chainId'] != 101:
    continue
  if 'extensions' not in token_data:
    continue
  if "bridgeContract" not in token_data['extensions']:
    continue
  if symbol in IGNORE:
    continue
  if name.startswith('Saber') and 'decimals' in name:
    continue
  bc = token_data['extensions']['bridgeContract']
  is_eth = bc == "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585"
  is_bsc = bc == "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7"
  is_polygon = bc == "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde"
  is_terra = bc == "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf"
  is_avax = bc == "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052"
  is_oasis = bc == "https://explorer.oasis.updev.si/address/0x5848C791e09901b40A9Ef749f2a6735b418d7564"
  is_ftm = bc == "https://ftmscan.com/address/0x7C9Fc5741288cDFdD83CeB07f3ea7e22618D79D2"

  if is_eth:
    origin = 'eth'
  elif is_bsc:
    origin = 'bsc'
  elif is_polygon:
    origin = 'matic'
  elif is_terra:
    origin = 'terra'
  elif is_avax:
    origin = 'avax'
  elif is_oasis:
    origin = 'oasis'
  elif is_ftm:
    origin = 'ftm'
  else:
    continue

  data = OrderedDict()
  for field in ['symbol', 'name', 'address']:
    data[field] = token_data[field]
  data['origin'] = origin
  if 'address' in token_data.get('extensions', []):
    data['sourceAddress'] = token_data['extensions']['address']
  if 'assetContract' in token_data.get('extensions', []):
    data['sourceContract'] = token_data['extensions']['assetContract']
  for field in ['coingeckoId', 'serumV3Usdc', 'serumV3Usdt']:
    if field in token_data.get('extensions', []):
      data[field] = token_data['extensions'][field]

  useful_data[symbol] = data

f = open(outpath, 'w')
f.write(json.dumps(useful_data, separators=(',', ': '), indent=2, ensure_ascii=True))
print('wrote %s' % outpath)