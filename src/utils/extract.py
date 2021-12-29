import os
from gen_data import TOKENS

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


ID_TO_CHAIN = {
  1: 'sol',
  2: 'eth',
  3: 'terra',
  4: 'bsc',
  5: 'matic',
  6: 'avax',
}

def load_logos():
  import json
  from collections import OrderedDict

  tokens = OrderedDict(TOKENS)
  tokens_by_addr = OrderedDict()
  for symbol, block in tokens.items():
    # by source
    addr = block['sourceAddress']
    tokens_by_addr[addr.lower()] = block
    # by dest
    for dest_chain, addr in block['destAddresses'].items():
      tokens_by_addr[addr.lower()] = block

  markets_path = os.path.join(dir_path, 'markets.json')
  with open(markets_path, 'r') as f:
    markets = json.load(f)

  token_markets = markets['tokenMarkets']
  for origin_chain_id, sub_dict in sorted(token_markets.items()):
    for dest_chain_id, sub_dict1 in sorted(sub_dict.items()):
      dest_chain = ID_TO_CHAIN[int(dest_chain_id)]
      for addr, sub_dict2 in sub_dict1.items():
        addr1 = addr.lower()
        my_markets = sub_dict2['markets']
        if addr1 not in tokens_by_addr:
          import pdb; pdb.set_trace()
        if 'markets' not in tokens_by_addr[addr1]:
          tokens_by_addr[addr1]['markets'] = OrderedDict()
        tokens_by_addr[addr1]['markets'][dest_chain] = my_markets

  outpath = os.path.join(dir_path, 'utils', 'tokens.json')
  f = open(outpath, 'w')
  f.write(json.dumps(tokens, separators=(',', ': '), indent=2, ensure_ascii=True))
  print('wrote %s' % outpath)


if __name__ == "__main__":
  load_logos()
