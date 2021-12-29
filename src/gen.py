"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""
import copy
import pandas as pd
import os
import json
from collections import OrderedDict

from config.market_urls import MARKETS
from config.token_data import TOKENS


dir_path = os.path.dirname(os.path.realpath(__file__))

# wormhole-specific token data is cached in digested version of file to make it
# easier to understand diffs (eliminate distractions from shitcoins)
SOLANA_DATA_PATH = os.path.join(dir_path, 'utils', 'solana_wormhole_tokens.json')


CHAIN_IDS_TO_NAMES = OrderedDict([
  (1, 'sol'),
  (2, 'eth'),
  (3, 'terra'),
  (4, 'bsc'),
  (5, 'matic'),
  (6, 'avax'),
])
CHAIN_NAMES_TO_IDS = OrderedDict([(v, k) for (k, v) in CHAIN_IDS_TO_NAMES.items()])


SOURCE_INFO = {
  'eth': ('Ethereum', 'et', "https://etherscan.io", "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585"),
  'bsc': ('BSC', 'bs', "https://bscscan.com", "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7"),
  'terra': ('Terra', 'te', "https://finder.terra.money/columbus-5", "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf"),
  'matic': ('Polygon', 'po', "https://polygonscan.com", "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde"),
  'avax': ('Avalanche', 'av', "https://snowtrace.io", "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052"),
  'sol': ('Solana', 'so', "https://solscan.io", "https://solscan.io/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb"),
}


def _link_address(dest, addr):
  category = 'address' if dest == 'terra' else 'token'
  return "[%s](%s/%s/%s)" % (addr, SOURCE_INFO[dest][2], category, addr)


def _link_coingecko(name, coingecko_id):
  if pd.isna(coingecko_id):
    return name
  else:
    return "[%s](http://coingecko.com/en/coins/%s)" % (name, coingecko_id)


def _link_source_address(source_chain, source_addr):
  source_contract = "%s/address/%s" % (SOURCE_INFO[source_chain][2] , source_addr)
  return "[%s](%s)" % (source_addr, source_contract)


def _get_markets_cell(markets_list):
  if isinstance(markets_list, list):
    return ", ".join(["[%s](%s)" % (MARKETS[m]["name"], MARKETS[m]["link"]) for m in markets_list])
  return ''


def get_df(dest):
  tokens = {}
  for source_chain, chain_tokens in sorted(TOKENS.items()):
    for coin, entry in chain_tokens.items():
      if dest not in entry['destAddresses']:
        continue
      entry = copy.deepcopy(entry)

      entry['origin'] = source_chain
      entry['address'] = entry['destAddresses'][dest]
      entry.pop('destAddresses')

      if 'markets' in entry:
        markets = entry.pop('markets', {})
        if dest in markets:
          entry['markets'] = markets[dest]

      tokens[coin] = entry

  return pd.DataFrame(tokens.values())


def get_df_solana(dest):
  with open(SOLANA_DATA_PATH, 'r') as f:
    TOKENS = json.load(f)
  return pd.DataFrame(TOKENS.values())


def gen_markdown(dest):
  dest_full = SOURCE_INFO[dest][0]

  if dest == 'sol':
    df = get_df_solana(dest)
  else:
    df = get_df(dest)

  if df.shape[0] == 0:
    print('no tokens for dest=%s' % dest)
    return

  df = df.sort_values(by='symbol')
  df['name'] = [_link_coingecko(n, c) for (n, c) in zip(df['name'].values, df['coingeckoId'].values)]
  df['address'] = [_link_address(dest, x) for x in df['address'].values]
  df['sourceAddress'] = [_link_source_address(x, y) for (x,y) in
                         zip(df['origin'].values, df['sourceAddress'].values)]
  df['origin'] = [SOURCE_INFO[x][0].lower() for x in df['origin'].values]

  if 'markets' in df.columns:
    df['markets'] = [_get_markets_cell(x) for x in df['markets'].values]

  if dest == 'sol':
    df['serumV3Usdc'] = ['' if pd.isna(x) else x for x in df['serumV3Usdc'].values]
    df['serumV3Usdt'] = ['' if pd.isna(x) else x for x in df['serumV3Usdt'].values]
    col_rename = {
      'serumV3Usdc': 'serumAddressUSDC',
      'serumV3Usdt': 'serumAddressUSDT',
    }
    df.columns = [col_rename.get(x, x) for x in df.columns]

  df['symbol_reprise'] = df['symbol']

  df = df.drop(['coingeckoId'], axis=1)

  order = ['symbol', 'name', 'address', 'origin', 'sourceAddress',
           'markets', 'serumAddressUSDC', 'serumAddressUSDT', 'symbol_reprise']
  df = df[[c for c in order if c in df.columns]]
  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to %s)
===================================
  """ % dest_full
  outpath = os.path.join(dir_path, 'dest_%s.md' % dest_full.lower())
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


def gen_markets_json():
  output = OrderedDict()

  output['markets'] = MARKETS

  # tokens: {sourceChain -> {addr -> {symbol, logo}}}
  token_output = {str(i): {} for i in CHAIN_IDS_TO_NAMES.keys()}

  for chain_name, chain_tokens in sorted(TOKENS.items()):
    chain_id = CHAIN_NAMES_TO_IDS[chain_name]
    for symbol, block in chain_tokens.items():
      addr = block['sourceAddress']
      logo = block['logo']
      mapping = {chain_id: addr}
      for dest_chain, dest_addr in block['destAddresses'].items():
        mapping[CHAIN_NAMES_TO_IDS[dest_chain]] = dest_addr
      for dest_chain_id, addr in mapping.items():
        token_output[str(dest_chain_id)][addr] = OrderedDict([
          ('symbol', symbol),
          ('logo', logo),
        ])
    output['tokens'] = token_output

  # tokenMarkets: {sourceChain -> {destChain -> {address -> {'markets': []}}}}

  # populate empty
  token_markets = {}
  for src_chain_id in sorted(CHAIN_IDS_TO_NAMES.keys()):
    token_markets[str(src_chain_id)] = {}
    for dest_chain_id in sorted(CHAIN_IDS_TO_NAMES.keys()):
      if src_chain_id == dest_chain_id:  # TODO: could remove this check
        continue
      token_markets[str(src_chain_id)][str(dest_chain_id)] = {}

  for chain_name, tokens in TOKENS.items():
    chain_id = CHAIN_NAMES_TO_IDS[chain_name]
    for symbol, block in TOKENS[chain_name].items():
      if 'markets' not in block or 'destAddresses' not in block:
        continue
      # destAddresses: {1 -> XXX}
      addresses_dict = {chain_id: block['sourceAddress']}
      for chain_name, address in block['destAddresses'].items():
        addresses_dict[CHAIN_NAMES_TO_IDS[chain_name]] = address
      # markets: {1 -> raydium}
      markets_dict = {CHAIN_NAMES_TO_IDS[chain_name]: mkts for (chain_name, mkts) in block['markets'].items()}

      for source_chain_id, address in addresses_dict.items():
        for dest_chain_id, markets in markets_dict.items():
          if source_chain_id == dest_chain_id:  # TODO: could remove this check
            continue
          token_markets[str(source_chain_id)][str(dest_chain_id)][address] = {'markets': markets}

  output['tokenMarkets'] = token_markets

  outpath = os.path.join(dir_path, 'markets.json')
  f = open(outpath, 'w')
  f.write(json.dumps(output, separators=(',', ': '), indent=2, ensure_ascii=True, sort_keys=True))
  print('wrote %s' % outpath)



def gen_outputs():
  for dest in ['sol', 'eth', 'bsc', 'terra', 'avax', 'matic']:
    gen_markdown(dest)


if __name__ == "__main__":
  gen_outputs()
  gen_markets_json()
