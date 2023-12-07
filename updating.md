List maintenance
========================

Various human- and machine-readable outputs are generated from the configuration in 
[src/config/token_data.py](src/config/token_data.py)
and [src/config/market_urls.py](src/config/market_urls.py).

## Updating

The main file to be updated is [src/config/token_data.py](src/config/token_data.py).

Entries in there are organized first by source chain (sol, eth, terra, bsc, matic, avax),
then are dictionaries with the following entries:
* `symbol`: e.g. `ATLAS`
* `name`: e.g. `Star Atlas (Portal)`
* `sourceAddress`: the address on the source chain
* `destAddresses`: a dictionary mapping dest chains to addresses (use the [Token Origin Verifier](https://portalbridge.com/advanced-tools/#/token-origin-verifier) to look this up)
* `markets`: a dictionary mapping dest chains to a list of market names where the wrapped asset is tradable
* `coingeckoId`: the API id on the 'Info' section of coingecko, generally the last part of the url
  * e.g. `star-atlas` if the coingecko url is `https://www.coingecko.com/en/coins/star-atlas`
* `logo`: link to thumbnail of the logo (can copy image url from etherscan or coinmarketcap).  OR you can save a png in [src/logogen/base](src/logogen/base).

Example:
```python
TOKENS = {
  'sol': {
    "ATLAS": {
      "symbol": "ATLAS",
      "name": "Star Atlas (Portal)",
      "sourceAddress": "ATLASXmbPQxBUYbxPsV97usA3fPQYEqzQBUHgiFCUsXx",
      "destAddresses": {
        "eth": "0xb9F747162AB1E95d07361f9048BcDF6eDdA9eEA7",
        "terra": "terra1rg8f993m9834afwazersesgx7jjxv4p87q9wvc",
        "bsc": "0x83850D97018f665EB746FBb8f18351e977d1b0D6",
      },
      "markets": {
        "bsc": ["pancakeswap"],
      },
      "coingeckoId": "star-atlas",
      "logo": "https://assets.coingecko.com/coins/images/17659/small/Icon_Reverse.png",
    },
    ...
  },
  ...
}
```

The market names must be defined in [src/config/market_urls.py](src/config/market_urls.py), so you'll occasionally need
to add to this if defining a new market.

## Generating output

> For contributors with write privileges, an action should automatically run on your PR to perform the update.

After updating the above files, run the below to update the `.md` and `.json` outputs:
```
npm run gen
```

See the [logo generation instructions](src/logogen/README.md) for instructions on generating logos with wormhole logos.
