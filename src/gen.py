"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""
import copy
import pandas as pd
import os
import json
from collections import OrderedDict

from config.constants import SOURCE_INFO, CHAIN_IDS_TO_NAMES, CHAIN_NAMES_TO_IDS
from config.market_urls import MARKETS
from config.token_data import TOKENS


dir_path = os.path.dirname(os.path.realpath(__file__))
content_path = os.path.join(os.path.dirname(dir_path), 'content')
assets_path = os.path.join(os.path.dirname(dir_path), 'assets')

# wormhole-specific token data is cached in digested version of file to make it
# easier to understand diffs (eliminate distractions from shitcoins)
SOLANA_DATA_PATH = os.path.join(dir_path, 'utils', 'solana_wormhole_tokens.json')


def _link_address(dest, addr):
  category = 'address' if dest == 'terra' else 'token'
  return "[%s](%s/%s/%s)" % (addr, SOURCE_INFO[dest][2], category, addr)


def _link_coingecko(name, coingecko_id):
  if pd.isna(coingecko_id):
    return name
  else:
    return "[%s](http://coingecko.com/en/coins/%s)" % (name, coingecko_id)


def _link_source_address(source_chain, source_addr):
  if source_addr is None:
    return ''
  source_contract = "%s/address/%s" % (SOURCE_INFO[source_chain][2] , source_addr)
  return "[%s](%s)" % (source_addr, source_contract)


def _get_img(tok):
  filepath = os.path.join(assets_path, '%s_wh.png' % tok)
  if os.path.exists(filepath):
    return '![%s](https://raw.githubusercontent.com/certusone/wormhole-token-list/main/assets/%s_wh.png)' % (tok, tok)
  else:
    return ''


def _get_markets_cell(markets_list):
  if isinstance(markets_list, list):
    return ", ".join(["[%s](%s)" % (MARKETS[m]["name"].lower(), MARKETS[m]["link"]) for m in markets_list])
  return ''


def get_dest_df(dest):
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


def get_dest_df_solana():
  with open(SOLANA_DATA_PATH, 'r') as f:
    TOKENS = json.load(f)
  df = pd.DataFrame(TOKENS.values())
  base_df = get_dest_df('sol')
  sym_markets = dict(zip(base_df['symbol'].values, base_df['markets'].values))
  df['markets'] = [sym_markets.get(s, '') for s in df['symbol'].values]
  return df


def gen_dest_info(dest):
  dest_full = SOURCE_INFO[dest][0]

  if dest == 'sol':
    df = get_dest_df_solana()
  else:
    df = get_dest_df(dest)

  if df.shape[0] == 0:
    print('no tokens for dest=%s' % dest)
    return

  df = df.sort_values(by='symbol')
  df['img'] = [_get_img(tok) for tok in df['symbol'].values]
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

  # reorder for readability
  order = ['img', 'symbol', 'name', 'address', 'origin', 'sourceAddress',
           'markets', 'serumAddressUSDC', 'serumAddressUSDT', 'symbol_reprise']
  df = df[[c for c in order if c in df.columns]]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to %s)
===================================
  """ % dest_full
  outpath = os.path.join(content_path, 'dest_%s.md' % dest_full.lower())
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


def get_source_df(source):
  chain_tokens = TOKENS[source]
  tokens = {}
  for coin, entry in chain_tokens.items():
    entry = copy.deepcopy(entry)
    for dest in CHAIN_NAMES_TO_IDS.keys():
      if dest == source:
        continue
      entry['%sAddress' % dest] = entry['destAddresses'].get(dest, None)
      if 'markets' in entry:
        entry['%sMarkets' % dest] = entry['markets'].get(dest, None)
      else:
        entry['%sMarkets' % dest] = None
      tokens[coin] = entry

  return pd.DataFrame(tokens.values()).sort_values(by='symbol')


def gen_source_info(source):
  source_full = SOURCE_INFO[source][0]
  df = get_source_df(source)

  if df.shape[0] == 0:
    print('no tokens for source=%s' % source)
    return
  df['img'] = [_get_img(tok) for tok in df['symbol'].values]
  df['name'] = [_link_coingecko(n, c) for (n, c) in zip(df['name'].values, df['coingeckoId'].values)]
  df['sourceAddress'] = [_link_source_address(source, x) for x in df['sourceAddress'].values]
  for dest in CHAIN_NAMES_TO_IDS.keys():
    if dest == source:
      continue
    df['%sAddress' % dest] = [_link_source_address(dest, x) for x in df['%sAddress' % dest].values]
    df['%sMarkets' % dest] = [_get_markets_cell(x) for x in df['%sMarkets' % dest].values]

  df['symbol_reprise'] = df['symbol']

  df = df.drop(['coingeckoId'], axis=1)

  # reorder for readability
  order = ['img', 'symbol', 'name', 'sourceAddress']
  for dest in CHAIN_NAMES_TO_IDS:
    order.extend(['%sAddress' % dest, '%sMarkets' % dest])
  order.append('symbol_reprise')
  df = df[[c for c in order if c in df.columns]]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Resultant wrapped-asset addresses (wormholing from %s)
===================================
  """ % source_full
  outpath = os.path.join(content_path, 'source_%s.md' % source_full.lower())
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
  for chain in ['sol', 'eth', 'bsc', 'terra', 'avax', 'matic']:
    gen_dest_info(chain)
    gen_source_info(chain)
  gen_markets_json()


if __name__ == "__main__":
  gen_outputs()
