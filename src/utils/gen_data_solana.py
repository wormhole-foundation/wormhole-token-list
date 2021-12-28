"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""
import json
import pandas as pd
import os


dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# wormhole-specific token data is cached in digested version of file to make it
# easier to understand diffs (eliminate distractions from shitcoins)
token_data_path = os.path.join(dir_path, 'utils', 'solana_wormhole_tokens.json')


def _link_address(addr):
  return "[%s](http://solscan.io/token/%s)" % (addr, addr)


def _link_coingecko(name, coingecko_id):
  if pd.isna(coingecko_id):
    return name
  else:
    return "[%s](http://coingecko.com/en/coins/%s)" % (name, coingecko_id)


def _link_source_address(source_addr, source_contract):
  if pd.isna(source_contract):
    return source_addr
  else:
    return "[%s](%s)" % (source_addr, source_contract)


def gen_markdown():
  with open(token_data_path, 'r') as f:
    TOKENS = json.load(f)
  df = pd.DataFrame(TOKENS.values())
  df = df.sort_values(by='symbol')
  df['name'] = [_link_coingecko(n, c) for (n, c) in zip(df['name'].values, df['coingeckoId'].values)]
  df['address'] = [_link_address(x) for x in df['address'].values]
  df['sourceAddress'] = [_link_source_address(x, y) for (x,y) in
                         zip(df['sourceAddress'].values, df['sourceContract'].values)]
  df['serumV3Usdc'] = ['' if pd.isna(x) else x for x in df['serumV3Usdc'].values]
  df['serumV3Usdt'] = ['' if pd.isna(x) else x for x in df['serumV3Usdt'].values]
  df['symbol_reprise'] = df['symbol']

  df = df.drop(['coingeckoId', 'sourceContract'], axis=1)

  col_rename = {
    'serumV3Usdc': 'serumAddressUSDC',
    'serumV3Usdt': 'serumAddressUSDT',
  }
  df.columns = [col_rename.get(x, x) for x in df.columns]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to Solana)
===================================
  """
  outpath = os.path.join(dir_path, 'dest_solana.md')
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


if __name__ == "__main__":
  gen_markdown()
