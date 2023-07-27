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
from config.token_data import TOKENS as _ORIG_TOKENS

from common import DIR_PATH, SRC_PATH, ASSET_PATH, get_logo_path, get_logo_raw_url


CHAINS = SOURCE_INFO.keys()
CONTENT_PATH = os.path.join(DIR_PATH, 'content')

# wormhole-specific token data is cached in digested version of file to make it
# easier to understand diffs (eliminate distractions from shitcoins)
SOLANA_DATA_PATH = os.path.join(SRC_PATH, 'utils', 'solana_wormhole_tokens.json')
with open(SOLANA_DATA_PATH, 'r') as f:
  DEST_SOLANA_TOKENS = json.load(f)

TOKENS = copy.deepcopy(_ORIG_TOKENS)
for symbol, block in DEST_SOLANA_TOKENS.items():
  origin = block['origin']
  sol_address = block['address']
  if symbol not in TOKENS[origin]:
    # synthesize new block
    new_block = OrderedDict()
    new_block['symbol'] = symbol
    new_block['name'] = block['name']
    new_block['destinations'] = {'sol': {
        'address': block['address'],
        'decimals': block['decimals']
    }}
    new_block['sourceAddress'] = block['sourceAddress']
    new_block['coingeckoId'] = block['coingeckoId']
    if 'logo' in block:
      new_block['logo'] = block['logo']
    TOKENS[origin][symbol] = new_block
  # maybe update serum stuff
  for field in ['serumV3Usdc', 'serumV3Usdt']:
    if field in block:
      TOKENS[origin][symbol][field] = block[field]



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
  filepath = os.path.join(ASSET_PATH, '%s_wh.png' % tok)
  if os.path.exists(filepath):
    return '![%s](https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/assets/%s_wh.png)' % (tok, tok)
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
      if dest not in entry['destinations']:
        continue
      entry = copy.deepcopy(entry)

      entry['origin'] = source_chain
      entry['address'] = entry['destinations'][dest]['address']
      entry['decimals'] = entry['destinations'][dest]['decimals']
      entry.pop('destinations')

      if 'markets' in entry:
        markets = entry.pop('markets', {})
        if dest in markets:
          entry['markets'] = markets[dest]

      # overwrite logo if it exists
      outpath = get_logo_path(coin)
      if os.path.exists(outpath):
        entry['logo'] = get_logo_raw_url(coin)

      tokens[coin] = entry

  return pd.DataFrame(tokens.values())


def gen_dest_csv():
  dfs = []
  for dest in CHAINS:
    df = get_dest_df(dest)
    df['dest'] = dest
    if 'markets' in df.columns:
      df = df.drop(['markets'], axis=1)
    dfs.append(df)
  df = pd.concat(dfs)
  order = ['dest', 'symbol', 'name', 'address', 'decimals', 'origin', 'sourceAddress',
           'sourceDecimals', 'coingeckoId', 'logo', 'serumV3Usdc', 'serumV3Usdt']
  df = df[[c for c in order if c in df.columns]]
  outpath = os.path.join(CONTENT_PATH, 'by_dest.csv')
  df.to_csv(outpath, index=False)
  print('wrote %s' % outpath)


def gen_dest_info(dest):
  dest_full = SOURCE_INFO[dest][0]

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
  order = ['img', 'symbol', 'name', 'address', 'decimals',
           'origin', 'sourceAddress', 'sourceDecimals', 'markets',
           'serumAddressUSDC', 'serumAddressUSDT', 'symbol_reprise']
  df = df[[c for c in order if c in df.columns]]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to %s)
===================================
_See [by_dest.csv](by_dest.csv) ([raw](https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/content/by_dest.csv)) for a superset of this data in csv._

  """ % dest_full
  outpath = os.path.join(CONTENT_PATH, 'dest_%s.md' % dest_full.lower())
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


def get_source_df(source, include_markets=True):
  chain_tokens = TOKENS[source]
  tokens = {}
  for coin, entry in chain_tokens.items():
    entry = copy.deepcopy(entry)
    for dest in CHAIN_NAMES_TO_IDS.keys():
      if dest == source:
        continue
      dest_data = entry['destinations'].get(dest, None)
      if dest_data is not None:
        entry['%sAddress' % dest] = dest_data['address']
        entry['%sDecimals' % dest] = dest_data['decimals']
      else:
        entry['%sAddress' % dest] = None
        entry['%sDecimals' % dest] = None
      if include_markets:
        if 'markets' in entry:
          entry['%sMarkets' % dest] = entry['markets'].get(dest, None)
        else:
          entry['%sMarkets' % dest] = None
      tokens[coin] = entry

  source_df = pd.DataFrame(tokens.values())
  if source_df.shape[0] > 0:
    source_df = source_df.sort_values(by="symbol")
  return source_df


def gen_source_csv():
  dfs = []
  for source in CHAINS:
    df = get_source_df(source, include_markets=False)
    df['source'] = source
    if 'markets' in df.columns:
      df = df.drop(['markets'], axis=1)
    if 'destinations' in df.columns:
      df = df.drop(['destinations'], axis=1)
    dfs.append(df)
  df = pd.concat(dfs)
  columns = ['source'] + [c for c in df.columns if c not in ['source']]

  order = ['source','symbol','name','sourceAddress','sourceDecimals','coingeckoId','logo']
  for bc in CHAINS:
    order.extend(['%sAddress' % bc, '%sDecimals' % bc])
  df = df[[c for c in order if c in columns]]
  outpath = os.path.join(CONTENT_PATH, 'by_source.csv')
  df.to_csv(outpath, index=False)
  print('wrote %s' % outpath)


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
    order.extend(['%sAddress' % dest, '%sDecimals' % dest, '%sMarkets' % dest])
  order.append('symbol_reprise')
  df = df[[c for c in order if c in df.columns]]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Resultant wrapped-asset addresses (wormholing from %s)
_See [by_source.csv](by_source.csv) ([raw](https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/content/by_source.csv)) for a superset of this data in csv._
=========================================================================
  """ % source_full
  outpath = os.path.join(CONTENT_PATH, 'source_%s.md' % source_full.lower())
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

      # TODO: always use our logo?
      if os.path.exists(get_logo_path(symbol)):
        logo = get_logo_raw_url(symbol)
      elif 'logo' in block:
        logo = block['logo']
      else:
        raise Exception('no logo for %s' % symbol)

      mapping = {chain_id: addr}
      for dest_chain, dest_data in block['destinations'].items():
        mapping[CHAIN_NAMES_TO_IDS[dest_chain]] = dest_data['address']
      for dest_chain_id, addr in mapping.items():
        d = OrderedDict([
          ('symbol', symbol),
        ])
        if logo is not None:
          d['logo'] = logo
        token_output[str(dest_chain_id)][addr] = d
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
      if 'markets' not in block or 'destinations' not in block:
        continue
      # destinations: {1 -> XXX}
      addresses_dict = {chain_id: block['sourceAddress']}
      for chain_name, dest_data in block['destinations'].items():
        addresses_dict[CHAIN_NAMES_TO_IDS[chain_name]] = dest_data['address']
      # markets: {1 -> raydium}
      markets_dict = {CHAIN_NAMES_TO_IDS[chain_name]: mkts for (chain_name, mkts) in block['markets'].items()}

      for source_chain_id, address in addresses_dict.items():
        for dest_chain_id, markets in markets_dict.items():
          if source_chain_id == dest_chain_id:  # TODO: could remove this check
            continue
          token_markets[str(source_chain_id)][str(dest_chain_id)][address] = {'markets': markets}

  output['tokenMarkets'] = token_markets

  outpath = os.path.join(SRC_PATH, 'markets.json')
  f = open(outpath, 'w')
  f.write(json.dumps(output, separators=(',', ': '), indent=2, ensure_ascii=True, sort_keys=True))
  print('wrote %s' % outpath)


def gen_outputs():
  for chain in CHAINS:
    gen_dest_info(chain)
    gen_source_info(chain)
  gen_dest_csv()
  gen_source_csv()
  gen_markets_json()


if __name__ == "__main__":
  gen_outputs()
