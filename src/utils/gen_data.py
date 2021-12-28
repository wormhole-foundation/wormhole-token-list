"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""
import copy
import pandas as pd
import os


dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

TOKENS = {
  ###############
  # Solana native
  ###############
  "SOL": {
    "symbol": "SOL",
    "name": "SOL (Wormhole)",
    "destAddresses": {
      "eth": "0xD31a59c85aE9D8edEFeC411D448f90841571b89c",
      "bsc": "0xfA54fF1a158B5189Ebba6ae130CEd6bbd3aEA76e",
      "terra": "terra190tqwgqx7s8qrknz6kckct7v607cu068gfujpk",
      "avax": "0xFE6B19286885a4F7F55AdAD09C3Cd1f906D2478F",
    },
    "origin": "sol",
    "sourceAddress": "So11111111111111111111111111111111111111112",
    "coingeckoId": "solana",
  },
  "mSOL": {
    "symbol": "mSOL",
    "name": "Marinade staked SOL (Wormhole)",
    "destAddresses": {
      "eth": "0x756bFb452cFE36A5Bc82e4F5f4261A89a18c242b",
      "terra": "terra1qvlpf2v0zmru3gtex40sqq02wxp39x3cjh359y",
    },
    "origin": "sol",
    "sourceAddress": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
    "coingeckoId": "marinade-staked-sol",
  },
  "USDCso": {
    "symbol": "USDCso",
    "name": "USD Coin (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0x41f7B8b9b897276b7AAE926a9016935280b44E97",
      "bsc": "0x91Ca579B0D47E5cfD5D0862c21D5659d39C8eCf0",
      "terra": "terra1e6mq63y64zcxz8xyu5van4tgkhemj3r86yvgu4",
      "avax": "0x0950Fc1AD509358dAeaD5eB8020a3c7d8b43b9DA",
    },
    "origin": "sol",
    "sourceAddress": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "coingeckoId": "usd-coin",
  },
  "USDTso": {
    "symbol": "USDTso",
    "name": "Tether USD (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0x1CDD2EaB61112697626F7b4bB0e23Da4FeBF7B7C",
      "bsc": "0x49d5cC521F75e13fa8eb4E89E9D381352C897c96",
      "terra": "terra1hd9n65snaluvf7en0p4hqzse9eqecejz2k8rl5",
      "avax": "0xF0FF231e3F1A50F83136717f287ADAB862f89431",
    },
    "origin": "sol",
    "sourceAddress": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
    "coingeckoId": "tether",
  },
  "RAY": {
    "symbol": "RAY",
    "name": "Raydium (Wormhole)",
    "destAddresses": {
      "eth": "0xE617dd80c621a5072bD8cBa65E9d76c07327004d",
      "bsc": "0x13b6A55662f6591f8B8408Af1C73B017E32eEdB8",
      "terra": "terra1ht5sepn28z999jx33sdduuxm9acthad507jg9q",
    },
    "origin": "sol",
    "sourceAddress": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
    "coingeckoId": "raydium",
  },
  "SBR": {
    "symbol": "SBR",
    "name": "Saber (Wormhole)",
    "destAddresses": {
      "bsc": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
      "terra": "terra17h82zsq6q8x5tsgm5ugcx4gytw3axguvzt4pkc",
    },
    "origin": "sol",
    "sourceAddress": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
    "coingeckoId": "saber",
  },
  "SRMso": {
    "symbol": "SRMso",
    "name": "Serum (Wormhole)",
    "destAddresses": {
      "eth": "0xE3ADAA4fb7c92AB833Ee08B3561D9c434aA2A3eE",
      "bsc": "0x12BeffdCEcb547640DC30e1495E4B9cdc21922b4",
      "terra": "terra1dkam9wd5yvaswv4yq3n2aqd4wm5j8n82qc0c7c",
    },
    "origin": "sol",
    "sourceAddress": "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt",
    "coingeckoId": "serum",
  },
  ###############
  # Terra native
  ###############
  "UST": {
    "symbol": "UST",
    "name": "UST (Wormhole)",
    "destAddresses": {
      "eth": "0xa693b19d2931d498c5b318df961919bb4aee87a5",
      "bsc": "0x3d4350cD54aeF9f9b2C29435e0fa809957B3F30a",
      "avax": "0xb599c3590F42f8F995ECfa0f85D2980B76862fc1",
      "matic": "0xE6469Ba6D2fD6130788E0eA9C0a0515900563b59",
    },
    "origin": "terra",
    "sourceAddress": "uusd",
    "coingeckoId": "terra-usd",
  },
  "LUNA": {
    "symbol": "LUNA",
    "name": "LUNA (Wormhole)",
    "destAddresses": {
      "eth": "0xbd31ea8212119f94a611fa969881cba3ea06fa3d",
      "bsc": "0x156ab3346823B651294766e23e6Cf87254d68962",
      "avax": "0x70928E5B188def72817b7775F0BF6325968e563B",
    },
    "origin": "terra",
    "sourceAddress": "uluna",
    "coingeckoId": "terra-luna",
  },
  # "": {
  #   "symbol": "",
  #   "name": " (Wormhole)",
  #   "destAddresses": {
  #     "eth": "",
  #     "bsc": "",
  #     "terra": "",
  #   },
  #   "origin": "sol",
  #   "sourceAddress": "",
  #   "coingeckoId": "",
  # },
}

SOURCE_INFO = {
  'eth': ('Ethereum', 'et', "https://etherscan.io", "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585"),
  'bsc': ('BSC', 'bs', "https://bscscan.com", "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7"),
  'terra': ('Terra', 'te', "https://finder.terra.money/columbus-5", "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf"),
  'matic': ('Polygon', 'po', "https://polygonscan.com", "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde"),
  'avax': ('Avalanche', 'av', "https://snowtrace.io", "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052"),
  'sol': ('Solana', 'so', "https://solscan.io", "https://solscan.io/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb"),
  # 'algo': ('Algorand', 'al'),
}


def _link_address(dest, addr):
  return "[%s](%s/token/%s)" % (addr, SOURCE_INFO[dest][2], addr)


def _link_coingecko(name, coingecko_id):
  if pd.isna(coingecko_id):
    return name
  else:
    return "[%s](http://coingecko.com/en/coins/%s)" % (name, coingecko_id)


def _link_source_address(source_chain, source_addr):
  source_contract = "%s/address/%s" % (SOURCE_INFO[source_chain][2] , source_addr)
  return "[%s](%s)" % (source_addr, source_contract)


def gen_markdown(dest):
  dest_full = SOURCE_INFO[dest][0]
  tokens = {}
  for coin, entry in TOKENS.items():
    if dest not in entry['destAddresses']:
      continue
    entry = copy.deepcopy(entry)
    entry['address'] = entry['destAddresses'][dest]
    entry.pop('destAddresses')
    tokens[coin] = entry
  df = pd.DataFrame(tokens.values())
  if df.shape[0] == 0:
    print('no tokens for dest=%s' % dest)
    return
  df = df.sort_values(by='symbol')
  df['name'] = [_link_coingecko(n, c) for (n, c) in zip(df['name'].values, df['coingeckoId'].values)]
  df['address'] = [_link_address(dest, x) for x in df['address'].values]
  df['sourceAddress'] = [_link_source_address(x, y) for (x,y) in
                         zip(df['origin'].values, df['sourceAddress'].values)]
  df['symbol_reprise'] = df['symbol']

  df = df.drop(['coingeckoId'], axis=1)

  # col_rename = {
  # }
  # df.columns = [col_rename.get(x, x) for x in df.columns]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to %s)
===================================
  """ % dest_full
  outpath = os.path.join(dir_path, 'dest_%s.md' % dest_full.lower())
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


if __name__ == "__main__":
  for dest in ['eth', 'bsc', 'terra', 'avax', 'matic']:
    gen_markdown(dest)
