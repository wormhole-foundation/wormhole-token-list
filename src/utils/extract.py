import os
from .gen_data import TOKENS

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

MANUAL_LOGOS = {
  "SBR": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/Saber2gLauYim4Mvftnrasomsv6NvAuncvMEZwcLpD1/logo.svg",
  "mSOL": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So/logo.png",
  "1SOL": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/4ThReWAbAVZjNVgs5Ui9Pk3cZ5TYaD9u6Y89fp6EFzoF/logo.png",
  "FXS": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct/logo.png",
  "LINK": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/2wpTofQ8SkACrkZWrZDjXPitYa8AwWgX8AfxdeBRRVLX/logo.png",
  "MIMet": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/HRQke5DKdDo3jV7wnomyiM8AA3EzkVnxMDdo2FQ5XUe1/logo.png",
  "gOHM": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/FUGsN8H74WjRBBMfQWcf9Kk32gebA9VnNaGxqwcVvUW7/logo.png",
  "stETH": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/H2mf9QNdU2Niq6QR7367Ua2trBsvscLyX5bz7R3Pw5sE/logo.png",
  "BNB": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa/logo.png",
  "CAKE": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/J8LKx7pr9Zxh9nMhhT7X3EBmj5RzuhFrHKyJAe2F2i9S/logo.png",
  "AVAX": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE/logo.png",
  "LDO": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/HZRCwxP2Vq9PCpPXooayhJ2bxTpo5xfpQrwB1svh332p/logo.png",
  "JOE": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/CriXdFS9iRAYbGEQiTcUqbWwG9RBmYt5B6LwTnoJ61Sm/logo.png",
}


def load_logos():
  import json
  from collections import OrderedDict

  markets_path = os.path.join(dir_path, 'markets.json')
  with open(markets_path, 'r') as f:
    markets = json.load(f)

  tokens = OrderedDict(TOKENS)
  orig_data = markets['tokens']
  for sub_data in orig_data.values():
    for addr, block in sub_data.items():
      symbol = block['symbol']
      candidate_suffixes = ['', 'so', 'et', 'te', 'bs', 'po', 'av']
      candidate_symbols = [symbol + s for s in candidate_suffixes]
      for candidate in candidate_symbols:
        if candidate in tokens:
          if 'logo' not in tokens[candidate]:
            tokens[candidate]['logo'] = block['logo']

  for token, logo in MANUAL_LOGOS.items():
    tokens[token]['logo'] = logo

  for token, block in tokens.items():
    if 'logo' not in block:
      print(token)

  outpath = os.path.join(dir_path, 'utils', 'tokens.json')
  f = open(outpath, 'w')
  f.write(json.dumps(tokens, separators=(',', ': '), indent=2, ensure_ascii=True))
  print('wrote %s' % outpath)


if __name__ == "__main__":
  load_logos()
