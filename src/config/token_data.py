TOKENS = {
  ###################
  # 1. Solana native
  ###################
  "sol": {
    "PYTH": {
      "symbol": "PYTH",
      "name": "Pyth Network",
      "sourceAddress": "HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3",
      "coingeckoId": "pyth-network",
      "markets": {
      },
      "destinations": {
      },
      "sourceDecimals": 6
    },
    "RAY": {
      "symbol": "RAY",
      "name": "Raydium (Portal)",
      "sourceAddress": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
      "coingeckoId": "raydium",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R/logo.png",
      "markets": {
      },
      "destinations": {
        "eth": {
          "address": "0xE617dd80c621a5072bD8cBa65E9d76c07327004d",
          "decimals": 6
        },
        "terra": {
          "address": "terra1ht5sepn28z999jx33sdduuxm9acthad507jg9q",
          "decimals": 6
        },
        "bsc": {
          "address": "0x13b6A55662f6591f8B8408Af1C73B017E32eEdB8",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "SBR": {
      "symbol": "SBR",
      "name": "Saber (Portal)",
      "sourceAddress": "Saber2gLauYim4Mvftnrasomsv6NvAuncvMEZwcLpD1",
      "coingeckoId": "saber",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/Saber2gLauYim4Mvftnrasomsv6NvAuncvMEZwcLpD1/logo.svg",
      "destinations": {
        "terra": {
          "address": "terra17h82zsq6q8x5tsgm5ugcx4gytw3axguvzt4pkc",
          "decimals": 6
        },
        "bsc": {
          "address": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "SOL": {
      "symbol": "SOL",
      "name": "SOL (Portal)",
      "sourceAddress": "So11111111111111111111111111111111111111112",
      "coingeckoId": "solana",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/So11111111111111111111111111111111111111112/logo.png",
      "markets": {
        "eth": ["uniswap"],
#         "bsc": ["pancakeswap"],
#         "matic": ["quickswap"],
        "injective": ["helix"]
      },
      "destinations": {
        "eth": {
          "address": "0xD31a59c85aE9D8edEFeC411D448f90841571b89c",
          "decimals": 9
        },
        "terra2": {
          "address": "terra1ctelwayk6t2zu30a8v9kdg3u2gr0slpjdfny5pjp7m3tuquk32ysugyjdg",
          "decimals": 8
        },
        "terra": {
          "address": "terra190tqwgqx7s8qrknz6kckct7v607cu068gfujpk",
          "decimals": 8
        },
        "bsc": {
          "address": "0xfA54fF1a158B5189Ebba6ae130CEd6bbd3aEA76e",
          "decimals": 9
        },
        "avax": {
          "address": "0xFE6B19286885a4F7F55AdAD09C3Cd1f906D2478F",
          "decimals": 9
        },
        "matic": {
          "address": "0xd93f7e271cb87c23aaa73edc008a79646d1f9912",
          "decimals": 9
        },
        "oasis": {
          "address": "0xd17dDAC91670274F7ba1590a06EcA0f2FD2b12bc",
          "decimals": 9
        },
        "ftm": {
          "address": "0xd99021C2A33e4Cf243010539c9e9b7c52E0236c1",
          "decimals": 9
        },
        "injective": {
          "address": "inj1sthrn5ep8ls5vzz8f9gp89khhmedahhdkqa8z3",
          "decimals": 8
        }
      },
      "sourceDecimals": 9
    },
    "SRMso": {
      "symbol": "SRMso",
      "name": "Serum (Portal from Solana)",
      "sourceAddress": "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt",
      "coingeckoId": "serum",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG/logo.png",
      "destinations": {
        "eth": {
          "address": "0xE3ADAA4fb7c92AB833Ee08B3561D9c434aA2A3eE",
          "decimals": 6
        },
        "terra": {
          "address": "terra1dkam9wd5yvaswv4yq3n2aqd4wm5j8n82qc0c7c",
          "decimals": 6
        },
        "bsc": {
          "address": "0x12BeffdCEcb547640DC30e1495E4B9cdc21922b4",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "TBTC": {
      "symbol": "TBTC",
      "name": "Threshold Bitcoin",
      "sourceAddress": "6DNSN2BJsaPFdFFc1zP37kkeNe4Usc1Sqkzr9C9vPWcU",
      "coingeckoId": "tbtc",
      "logo": "https://assets.coingecko.com/coins/images/11224/small/0x18084fba666a33d37592fa2633fd49a74dd93a88.png?1674474504",
      "markets": {
        "eth": ['threshold'],
        "matic": ['threshold'],
        "arbitrum": ['threshold'],
        "optimism": ['threshold'],
        "base": ['threshold']
      },
      "destinations": {
        "eth": {
          "address": "0x18084fbA666a33d37592fA2633fD49a74DD93a88",
          "decimals": 8
        },
        "matic": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "arbitrum": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "optimism": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "base": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "USDCso": {
      "symbol": "USDCso",
      "name": "USD Coin (Portal from Solana)",
      "sourceAddress": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
      "coingeckoId": "usd-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/logo.png",
      "markets": {
        "eth": ["uniswap"],
#         "bsc": ["pancakeswap"],
#         "matic": ["quickswap"],
        "sol": ["jupiter"], #revert to native asset
      },
      "destinations": {
        "eth": {
          "address": "0x41f7B8b9b897276b7AAE926a9016935280b44E97",
          "decimals": 6
        },
        "terra": {
          "address": "terra1e6mq63y64zcxz8xyu5van4tgkhemj3r86yvgu4",
          "decimals": 6
        },
        "bsc": {
          "address": "0x91Ca579B0D47E5cfD5D0862c21D5659d39C8eCf0",
          "decimals": 6
        },
        "avax": {
          "address": "0x0950Fc1AD509358dAeaD5eB8020a3c7d8b43b9DA",
          "decimals": 6
        },
        "matic": {
          "address": "0x576cf361711cd940cd9c397bb98c4c896cbd38de",
          "decimals": 6
        },
        "oasis": {
          "address": "0x1d1149a53deB36F2836Ae7877c9176413aDfA4A8",
          "decimals": 6
        },
        "aurora": {
          "address": "0xDd1DaFedeBa5F9851C4F4a2876E0f3aF3c774B1A",
          "decimals": 6
        },
        "ftm": {
          "address": "0xb8398DA4FB3BC4306B9D9d9d13d9573e7d0E299f",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "USDTso": {
      "symbol": "USDTso",
      "name": "Tether USD (Portal from Solana)",
      "sourceAddress": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
      "coingeckoId": "tether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB/logo.svg",
      "markets": {
      },
      "destinations": {
        "eth": {
          "address": "0x1CDD2EaB61112697626F7b4bB0e23Da4FeBF7B7C",
          "decimals": 6
        },
        "terra": {
          "address": "terra1hd9n65snaluvf7en0p4hqzse9eqecejz2k8rl5",
          "decimals": 6
        },
        "bsc": {
          "address": "0x49d5cC521F75e13fa8eb4E89E9D381352C897c96",
          "decimals": 6
        },
        "avax": {
          "address": "0xF0FF231e3F1A50F83136717f287ADAB862f89431",
          "decimals": 6
        },
        "matic": {
          "address": "0x3553f861dec0257bada9f8ed268bf0d74e45e89c",
          "decimals": 6
        },
        "oasis": {
          "address": "0x24285C5232ce3858F00bacb950Cae1f59d1b2704",
          "decimals": 6
        },
        "aurora": {
          "address": "0xd80890AFDBd7148456D8Ee358eF9127F0F8c7faf",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "mSOL": {
      "symbol": "mSOL",
      "name": "Marinade staked SOL (Portal)",
      "sourceAddress": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
      "coingeckoId": "marinade-staked-sol",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So/logo.png",
      "destinations": {
        "eth": {
          "address": "0x756bFb452cFE36A5Bc82e4F5f4261A89a18c242b",
          "decimals": 9
        },
        "terra": {
          "address": "terra1qvlpf2v0zmru3gtex40sqq02wxp39x3cjh359y",
          "decimals": 8
        },
        "oasis": {
          "address": "0x5E11A4f64D3B9fA042dB9e1AA918F735038FdfD8",
          "decimals": 9
        }
      },
      "sourceDecimals": 9
    },
    "ZBC": {
      "symbol": "ZBC",
      "name": "Wrapped Zebec Token",
      "sourceAddress": "wzbcJyhGhQDLTV1S99apZiiBdE4jmYfbw99saMMdP59",
      "coingeckoId": "zebec-protocol",
      "logo": "https://raw.githubusercontent.com/Zebec-protocol/zebec-assets/master/wrap-logo.png",
      "markets": {
        "bsc": ["pancakeswap"]
      },
      "destinations": {
        "bsc": {
          "address": "0x37a56cdcd83dce2868f721de58cb3830c44c6303",
          "decimals": 9
        }
      },
      "sourceDecimals": 9
    },
    "XTAG": {
      "symbol": "XTAG",
      "name": "XTAG Token (Portal)",
      "sourceAddress": "5gs8nf4wojB5EXgDUWNLwXpknzgV2YWDhveAeBZpVLbp",
      "coingeckoId": "xhashtag",
      "logo": "https://raw.githubusercontent.com/sudomon/wormhole-token-list/main/src/logogen/base/xtag.png",
      "destinations": {
        "avax": {
          "address": "0xa608d79c5f695c0d4c0e773a4938b57e18e0fc57",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "KING": {
      "symbol": "KING",
      "name": "KING (Portal)",
      "sourceAddress": "9noXzpXnkyEcKF3AeXqUHTdR59V5uvrRBUZ9bwfQwxeq",
      "coingeckoId": "king",
      "logo": "https://static.wixstatic.com/media/326cf0_041cbca6882f4388b105ed00ac68188c~mv2.png/v1/crop/x_77,y_0,w_343,h_358/fill/w_319,h_332,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/326cf0_041cbca6882f4388b105ed00ac68188c~mv2.png",
      "markets": {
        "eth": [
          "uniswap",
        ],
        "sol": [
          "orca",
          "jupiter",
          "raydium"
        ],
      },
      "destinations": {
        "eth": {
          "address": "0xE28027c99C7746fFb56B0113e5d9708aC86fAE8f",
          "decimals": 9
        }
      },
      "sourceDecimals": 9
    },
    "BONK": {
      "symbol": "BONK",
      "name": "BONK (Portal)",
      "sourceAddress": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
      "coingeckoId": "bonk",
      "logo": "https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/src/logogen/base/BONK.png",
      "markets": {
        "eth": [
          "uniswap",
          "curve",
        ],
        "sol": [
          "orca",
          "jupiter",
        ],
        "bsc": [
          "pancakeswap"
        ],
        "matic": [
          "quickswap", 
          "sushi"
        ],
        "arbitrum": [
          "uniswap"
        ],
        "injective": ["helix"]
      },
      "destinations": {
        "eth": {
          "address": "0x1151CB3d861920e07a38e03eEAd12C32178567F6",
          "decimals": 5
        },
        "bsc": {
          "address": "0xA697e272a73744b343528C3Bc4702F2565b2F422",
          "decimals": 5
        },
        "matic": {
          "address": "0xe5B49820e5A1063F6F4DdF851327b5E8B2301048",
          "decimals": 5
        },
        "aptos": {
          "address": "0x2a90fae71afc7460ee42b20ee49a9c9b29272905ad71fef92fbd8b3905a24b56",
          "decimals": 5
        },
        "arbitrum": {
          "address": "0x09199d9a5f4448d0848e4395d065e1ad9c4a1f74",
          "decimals": 5
        },        
        "injective": {
          "address": "inj14rry9q6dym3dgcwzq79yay0e9azdz55jr465ch",
          "decimals": 5
        }
      },
      "sourceDecimals": 5
    },
  },
  #####################
  # 2. Ethereum native
  #####################
  "eth": {
    "1INCH": {
      "symbol": "1INCH",
      "name": "1INCH Token (Portal)",
      "sourceAddress": "0x111111111117dC0aa78b770fA6A738034120C302",
      "coingeckoId": "1inch",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "AjkPkq3nsyDe1yKcbyZT7N4aK4Evv9om9tzhQD3wsRC",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "1SOL": {
      "symbol": "1SOL",
      "name": "1sol.io (Portal)",
      "sourceAddress": "0x009178997aff09a67d4caccfeb897fb79d036214",
      "coingeckoId": "1sol",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/4ThReWAbAVZjNVgs5Ui9Pk3cZ5TYaD9u6Y89fp6EFzoF/logo.png",
      "destinations": {
        "sol": {
          "address": "4ThReWAbAVZjNVgs5Ui9Pk3cZ5TYaD9u6Y89fp6EFzoF",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "AAVE": {
      "symbol": "AAVE",
      "name": "Aave Token (Portal)",
      "sourceAddress": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
      "coingeckoId": "aave",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "3vAs4D1WE6Na4tCgt4BApgFfENbm8WY7q4cSPD1yM4Cg",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "AKRO": {
      "symbol": "AKRO",
      "name": "Akropolis (Portal)",
      "sourceAddress": "0x8ab7404063ec4dbcfd4598215992dc3f8ec853d7",
      "coingeckoId": "akropolis",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/G3h8NZgJozk9crme2me6sKDJuSQ12mNCtvC9NbSWqGuk/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "12uHjozDVgyGWeLqQ8DMCRbig8amW5VmvZu3FdMMdcaG",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ALEPH": {
      "symbol": "ALEPH",
      "name": "Aleph.im (Portal)",
      "sourceAddress": "0x27702a26126e0b3702af63ee09ac4d1a084ef628",
      "coingeckoId": "aleph-im",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "3UCMiSnkcnkPE1pgQ5ggPCBv6dXgVUy16TmMUe1WpG9x",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ALICE": {
      "symbol": "ALICE",
      "name": "My Neighbor Alice (Portal)",
      "sourceAddress": "0xac51066d7bec65dc4589368da368b212745d63e8",
      "coingeckoId": "my-neighbor-alice",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "9ARQsBfAn65q522cEqSJuse3cLhA31jgWDBGQHeiq7Mg",
          "decimals": 8
        }
      },
      "sourceDecimals": 6
    },
    "AMP": {
      "symbol": "AMP",
      "name": "Amp (Portal)",
      "sourceAddress": "0xff20817765cb7f73d4bde2e66e067e58d11095c2",
      "coingeckoId": "amp",
      "destinations": {
        "sol": {
          "address": "D559HwgjYGDYsXpmFUKxhFTEwutvS9sya1kXiyCVogCV",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "AMPL": {
      "symbol": "AMPL",
      "name": "Ampleforth (Portal)",
      "sourceAddress": "0xd46ba6d942050d489dbd938a2c909a5d5039a161",
      "coingeckoId": "ampleforth",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "EHKQvJGu48ydKA4d3RivrkNyTJTkSdoS32UafxSX1yak",
          "decimals": 8
        }
      },
      "sourceDecimals": 9
    },
    "ANKR": {
      "symbol": "ANKR",
      "name": "Ankr (Portal)",
      "sourceAddress": "0x8290333cef9e6d528dd5618fb97a76f268f3edd4",
      "coingeckoId": "ankr",
      "destinations": {
        "sol": {
          "address": "Gq2norJ1kBemBp3mPfkgAUMhMMmnFmY4zEyi26tRcxFB",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "AUDIO": {
      "symbol": "AUDIO",
      "name": "Audius (Portal)",
      "sourceAddress": "0x18aaa7115705e8be94bffebde57af9bfc265b998",
      "coingeckoId": "audius",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "9LzCMqDgTKYz9Drzqnpgee3SGa89up3a247ypMj2xrqM",
          "decimals": 8
        },
        "terra": {
          "address": "terra1nc6flp57m5hsr6y5y8aexzszy43ksr0drdr8rp",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "AXSet": {
      "symbol": "AXSet",
      "name": "Axie Infinity Shard (Portal from Ethereum)",
      "sourceAddress": "0xbb0e17ef65f82ab018d8edd776e8dd940327b28b",
      "coingeckoId": "axie-infinity",
      "logo": "https://etherscan.io/token/images/axieinfinityshard_32.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "HysWcbHiYY9888pHbaqhwLYZQeZrcQMXKQWRqS7zcPK5",
          "decimals": 8
        },
        "bsc": {
          "address": "0x556b60c53fbC1518Ad17E03d52E47368dD4d81B3",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "BAT": {
      "symbol": "BAT",
      "name": "Basic Attention Token (Portal)",
      "sourceAddress": "0x0d8775f648430679a709e98d2b0cb6250d2887ef",
      "coingeckoId": "basic-attention-token",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "EPeUFDgHRxs9xxEPVaL6kfGQvCon7jmAWKVUHuux1Tpz",
          "decimals": 8
        },
        "terra": {
          "address": "terra1apxgj5agkkfdm2tprwvykug0qtahxvfmugnhx2",
          "decimals": 8
        },
        "bsc": {
          "address": "0x31C78f583ed0288D67b2b80Dc5C443Bc3b15C661",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "BKN": {
      "symbol": "BKN",
      "name": "Brickken (Portal)",
      "sourceAddress": "0x0A638F07ACc6969abF392bB009f216D22aDEa36d",
      "coingeckoId": "brickken",
      "markets": {
        "eth": ["uniswap"]
      },
      "logo": "https://etherscan.io/token/images/brickken_32.png",
      "destinations": {
        "bsc": {
          "address": "0x0e28bC9B03971E95acF9ae1326E51ecF9C55B498",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "BNT": {
      "symbol": "BNT",
      "name": "Bancor Network Token (Portal)",
      "sourceAddress": "0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c",
      "coingeckoId": "bancor-network",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "EDVVEYW4fPJ6vKw5LZXRGUSPzxoHrv6eWvTqhCr8oShs",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "BUSDet": {
      "symbol": "BUSDet",
      "name": "Binance USD (Portal from Ethereum)",
      "sourceAddress": "0x4fabb145d64652a948d72533023f6e7a623c7c53",
      "coingeckoId": "binance-usd",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/33fsBLA8djQm82RpHmE3SuVrPGtZBWNYExsEUeKX1HXX/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "33fsBLA8djQm82RpHmE3SuVrPGtZBWNYExsEUeKX1HXX",
          "decimals": 8
        },
        "bsc": {
          "address": "0x035de3679E692C471072d1A09bEb9298fBB2BD31",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "CEL": {
      "symbol": "CEL",
      "name": "Celsius (Portal)",
      "sourceAddress": "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d",
      "coingeckoId": "celsius-network",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "nRtfwU9G82CSHhHGJNxFhtn7FLvWP2rqvQvje1WtL69",
          "decimals": 4
        }
      },
      "sourceDecimals": 4
    },
    "CHZ": {
      "symbol": "CHZ",
      "name": "Chiliz (Portal)",
      "sourceAddress": "0x3506424f91fd33084466f402d5d97f05f8e3b4af",
      "coingeckoId": "chiliz",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "5TtSKAamFq88grN1QGrEaZ1AjjyciqnCya1aiMhAgFvG",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "CHAI": {
      "symbol": "CHAI",
      "name": "CHAI (Portal)",
      "sourceAddress": "0x06AF07097C9Eeb7fD685c692751D5C66dB49c215",
      "logo": "https://raw.githubusercontent.com/lucasvo/chui/master/src/assets/logostill.png",
      "markets": {
        "eth": [
          "curve"
        ],
        "sol": [
          "openbook",
          "raydium",
          "jupiter",
        ]
      },
      "destinations": {
        "sol": {
          "address": "3jsFX1tx2Z8ewmamiwSU851GzyzM2DJMq7KWW5DM8Py3",
          "decimals": 8
        },
      },
      "sourceDecimals": 18
    },
    "COMP": {
      "symbol": "COMP",
      "name": "Compound (Portal)",
      "sourceAddress": "0xc00e94cb662c3520282e6f5717214004a7f26888",
      "coingeckoId": "compound",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "AwEauVaTMQRB71WeDnwf1DWSBxaMKjEPuxyLr1uixFom",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "CREAM": {
      "symbol": "CREAM",
      "name": "Cream (Portal)",
      "sourceAddress": "0x2ba592f78db6436527729929aaf6c908497cb200",
      "coingeckoId": "cream",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "HihxL2iM6L6P1oqoSeiixdJ3PhPYNxvSKH9A2dDqLVDH",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "CRO": {
      "symbol": "CRO",
      "name": "Crypto.com Coin (Portal)",
      "sourceAddress": "0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b",
      "coingeckoId": "crypto-com-coin",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "DvjMYMVeXgKxaixGKpzQThLoG98nc7HSU7eanzsdCboA",
          "decimals": 8
        }
      },
      "sourceDecimals": 8
    },
    "CRV": {
      "symbol": "CRV",
      "name": "Curve DAO Token (Portal)",
      "sourceAddress": "0xd533a949740bb3306d119cc777fa900ba034cd52",
      "coingeckoId": "curve-dao-token",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "7gjNiPun3AzEazTZoFEjZgcBMeuaXdpjHq2raZTmTrfs",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "CVX": {
      "symbol": "CVX",
      "name": "Convex Finance (Portal)",
      "sourceAddress": "0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b",
      "coingeckoId": "convex-finance",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "BLvmrccP4g1B6SpiVvmQrLUDya1nZ4B2D1nm9jzKF7sz",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "DAI": {
      "symbol": "DAI",
      "name": "DAI (Portal)",
      "sourceAddress": "0x6b175474e89094c44da98b954eedeac495271d0f",
      "coingeckoId": "dai",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG/logo.png",
      "markets": {
        "eth": [
          "curve"
        ],
        "sol": [
          "saber",
          "mercurial",
          "jupiter",
        ]
      },
      "destinations": {
        "sol": {
          "address": "EjmyN6qEC1Tf1JxiG1ae7UTJhUxSwk1TCWNWqxWV4J6o",
          "decimals": 8
        },
        "bsc": {
          "address": "0x3413a030EF81a3dD5a302F4B4D11d911e12ed337",
          "decimals": 18
        },
        "terra": {
          "address": "terra1zmclyfepfmqvfqflu8r3lv6f75trmg05z7xq95",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "DEXE": {
      "symbol": "DEXE",
      "name": "DeXe (Portal)",
      "sourceAddress": "0xde4EE8057785A7e8e800Db58F9784845A5C2Cbd6",
      "coingeckoId": "dexe",
      "logo": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xde4EE8057785A7e8e800Db58F9784845A5C2Cbd6/logo.png",
      "markets": {},
      "destinations": {
        "bsc": {
          "address": "0x6e88056e8376ae7709496ba64d37fa2f8015ce3e",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "DIMO": {
      "symbol": "DIMO",
      "name": "Dimo",
      "sourceAddress": "0x5fab9761d60419C9eeEbe3915A8FA1ed7e8d2E1B",
      "destinations": {
        "sol": {
            "address": "3vx72dR2UpYSQL2EL2nBv2cyMEnyTs2qmmTwxp6Ffo6v",
            "decimals": 8   
        }
      },
      "markets": {},
      "coingeckoId": "dimo",
      "logo": "https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/src/logogen/base/DIMO.png",
      "sourceDecimals": 18
    },
    "DYDX": {
      "symbol": "DYDX",
      "name": "dYdX (Portal)",
      "sourceAddress": "0x92d6c1e31e14520e676a687f0a93788b716beff5",
      "coingeckoId": "dydx",
      "logo": "https://etherscan.io/token/images/dydx2_32.png",
      "markets": {
        "sol": [
          "raydium",
        ]
      },
      "destinations": {
        "sol": {
          "address": "4Hx6Bj56eGyw8EJrrheM6LBQAvVYRikYCWsALeTrwyRU",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ELON": {
      "symbol": "ELON",
      "name": "Dogelon (Portal)",
      "sourceAddress": "0x9EFe7414D991769282b8c27bb2E53B7a34F60Bc2",
      "coingeckoId": "dogelon-mars",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "7ZCm8WBN9aLa3o47SoYctU6iLdj7wkGG5SV2hE5CgtD5",
          "decimals": 4
        }
      },
      "sourceDecimals": 4
    },
    "ENJ": {
      "symbol": "ENJ",
      "name": "EnjinCoin (Portal)",
      "sourceAddress": "0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c",
      "coingeckoId": "enjin",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "EXExWvT6VyYxEjFzF5BrUxt5GZMPVZnd48y3iWrRefMq",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ENS": {
      "symbol": "ENS",
      "name": "Ethereum Name Service (Portal)",
      "sourceAddress": "0xc18360217d8f7ab5e7c516566761ea12ce7f9d72",
      "coingeckoId": "ethereum-name-service",
      "destinations": {
        "sol": {
          "address": "CLQsDGoGibdNPnVCFp8BAsN2unvyvb41Jd5USYwAnzAg",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ETH": {
      "symbol": "ETH",
      "name": "Ether (Portal)",
      "sourceAddress": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
      "coingeckoId": "ether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs/logo.png",
      "markets": {
        "eth": ["curve"],
        "sol": ["orca", "saber", "tulip", "port", "francium", "raydium","dexlab"],
        "oasis": ["yuzu"],
        "celo": ["ubeswap"],
        "moonbeam": ["stellaswap", "moonwell","beamex"],
        "algorand": ["algofi", "pact"], 
        "aptos": ["hippo", "ariesmarkets"],
      },
      "destinations": {
        "sol": {
          "address": "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs",
          "decimals": 8
        },
        "bsc": {
          "address": "0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA",
          "decimals": 18
        },
        "terra2": {
          "address": "terra15hhqg8gyz04zapynqtk7uvlsp7lzay7etrt9ann0276v94yae63sxygeat",
          "decimals": 8
        },
        "terra": {
          "address": "terra14tl83xcwqjy0ken9peu4pjjuu755lrry2uy25r",
          "decimals": 8
        },
        "matic": {
          "address": "0x11CD37bb86F65419713f30673A480EA33c826872",
          "decimals": 18
        },
        "avax": {
          "address": "0x8b82A291F83ca07Af22120ABa21632088fC92931",
          "decimals": 18
        },
        "oasis": {
          "address": "0x3223f17957Ba502cbe71401D55A0DB26E5F7c68F",
          "decimals": 18
        },
        "aurora": {
          "address": "0x811Cc0d762eA72aC72385d93b98a97263AE37E4C",
          "decimals": 18
        },
        "celo": {
          "address": "0x66803FB87aBd4aaC3cbB3fAd7C3aa01f6F3FB207",
          "decimals": 18
        },
        "moonbeam": {
          "address": "0xab3f0245B83feB11d15AAffeFD7AD465a59817eD",
          "decimals": 18
        },
      },
        "algorand": {
          "address": "887406851",
          "decimals": 8
        },
          "aptos": {
          "address": "0xcc8a89c8dce9693d354449f1f73e60e14e347417854f029db5bc8e7454008abb",
          "decimals": 8
        },
      "sourceDecimals": 18
    },
    "ETHIX": {
      "symbol": "ETHIX",
      "name": "Ethix (Portal)",
      "sourceAddress": "0xFd09911130e6930Bf87F2B0554c44F400bD80D3e",
      "coingeckoId": "ethichub",
      "logo": "https://raw.githubusercontent.com/ethichub/wormhole-token-list/main/src/logogen/base/ETHIX.png",
      "markets": {
        "eth": ["uniswap", "balancer"],
        "celo": ["symmetric", "ubeswap"],
      },
      "destinations": {
        "celo": {
          "address": "0x9995cc8F20Db5896943Afc8eE0ba463259c931ed",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "EURC": {
      "symbol": "EURC",
      "name": "Euro Coin (Portal from Ethereum))",
      "sourceAddress": "0x1aBaEA1f7C830bD89Acc67eC4af516284b1bC33c",
      "coingeckoId": "euro-coin",
      "markets": {},
      "destinations": {},
      "sourceDecimals": 6
    },
    "FRAX": {
      "symbol": "FRAX",
      "name": "Frax (Portal)",
      "sourceAddress": "0x853d955acef822db058eb8505911ed77f175b99e",
      "coingeckoId": "frax",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/FR87nWEUxVgerFGhZM8Y4AggKGLnaXswr1Pd8wZ4kZcp/logo.png",
      "markets": {
        "eth": [
          "curve"
        ],
        "sol": [
          "saber"
        ]
      },
      "destinations": {
        "sol": {
          "address": "FR87nWEUxVgerFGhZM8Y4AggKGLnaXswr1Pd8wZ4kZcp",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "FRONT": {
      "symbol": "FRONT",
      "name": "Frontier (Portal)",
      "sourceAddress": "0xf8c3527cc04340b208c854e985240c02f7b7793f",
      "coingeckoId": "frontier",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "A9ik2NrpKRRG2snyTjofZQcTuav9yH3mNVHLsLiDQmYt",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "FTMet": {
      "symbol": "FTMet",
      "name": "Fantom (Portal from Ethereum)",
      "sourceAddress": "0x4e15361fd6b4bb609fa63c81a2be19d873717870",
      "coingeckoId": "fantom",
      "destinations": {
        "sol": {
          "address": "8gC27rQF4NEDYfyf5aS8ZmQJUum5gufowKGYRRba4ENN",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "FTT": {
      "symbol": "FTT",
      "name": "FTX Token (Portal)",
      "sourceAddress": "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9",
      "coingeckoId": "ftx-token",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/EzfgjvkSwthhgHaceR3LnKXUoRkP6NUhfghdaHAj1tUv/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "EzfgjvkSwthhgHaceR3LnKXUoRkP6NUhfghdaHAj1tUv",
          "decimals": 8
        },
        "bsc": {
          "address": "0x49BA054B9664e99ac335667a917c63bB94332E84",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "FXS": {
      "symbol": "FXS",
      "name": "Frax Share (Portal)",
      "sourceAddress": "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0",
      "coingeckoId": "frax-share",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct/logo.png",
      "destinations": {
        "sol": {
          "address": "6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "GALA": {
      "symbol": "GALA",
      "name": "Gala (Portal)",
      "sourceAddress": "0x15d4c048f83bd7e37d49ea4c83a07267ec4203da",
      "coingeckoId": "gala",
      "destinations": {
        "sol": {
          "address": "AuGz22orMknxQHTVGwAu7e3dJikTJKgcjFwMNDikEKmF",
          "decimals": 8
        }
      },
      "sourceDecimals": 8
    },
    "GRT": {
      "symbol": "GRT",
      "name": "Graph Token (Portal)",
      "sourceAddress": "0xc944E90C64B2c07662A292be6244BDf05Cda44a7",
      "coingeckoId": "the-graph",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "HGsLG4PnZ28L8A4R5nPqKgZd86zUUdmfnkTRnuFJ5dAX",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "GT": {
      "symbol": "GT",
      "name": "GateToken (Portal)",
      "sourceAddress": "0xe66747a101bff2dba3697199dcce5b743b454759",
      "coingeckoId": "gatetoken",
      "destinations": {
        "sol": {
          "address": "ABAq2R9gSpDDGguQxBk4u13s4ZYW6zbwKVBx15mCMG8",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "HBTC": {
      "symbol": "HBTC",
      "name": "Huobi BTC (Portal)",
      "sourceAddress": "0x0316eb71485b0ab14103307bf65a021042c6d380",
      "coingeckoId": "huobi-btc",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/7dVH61ChzgmN9BwG4PkzwRP8PbYwPJ7ZPNF2vamKT2H8/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "7dVH61ChzgmN9BwG4PkzwRP8PbYwPJ7ZPNF2vamKT2H8",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "HGET": {
      "symbol": "HGET",
      "name": "Hedget (Portal)",
      "sourceAddress": "0x7968bc6a03017ea2de509aaa816f163db0f35148",
      "coingeckoId": "hedget",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "2ueY1bLcPHfuFzEJq7yN1V2Wrpu8nkun9xG2TVCE1mhD",
          "decimals": 8
        }
      },
      "sourceDecimals": 6
    },
    "HXRO": {
      "symbol": "HXRO",
      "name": "Hxro (Portal)",
      "sourceAddress": "0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3",
      "coingeckoId": "hxro",
      "markets": {
        "sol": [
          "orca", "raydium"
        ]
      },
      "destinations": {
        "sol": {
          "address": "HxhWkVpk5NS4Ltg5nij2G671CKXFRKPK8vy271Ub4uEK",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "HUSD": {
      "symbol": "HUSD",
      "name": "HUSD Stablecoin (Portal)",
      "sourceAddress": "0xdf574c24545e5ffecb9a659c229253d4111d87e1",
      "coingeckoId": "husd",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/7VQo3HFLNH5QqGtM8eC3XQbPkJUu7nS9LeGWjerRh5Sw/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "7VQo3HFLNH5QqGtM8eC3XQbPkJUu7nS9LeGWjerRh5Sw",
          "decimals": 8
        }
      },
      "sourceDecimals": 8
    },
    "ICE": {
      "symbol": "ICE",
      "name": "PopsicleToken (Portal)",
      "sourceAddress": "0xf16e81dce15b08f326220742020379b855b87df9",
      "coingeckoId": "popsicle-finance",
      "destinations": {
        "sol": {
          "address": "DiJut4U3CU8b3bRgwfyqtJMJ4wjzJHaX6hudamjH46Km",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ILV": {
      "symbol": "ILV",
      "name": "Illuvium (Portal)",
      "sourceAddress": "0x767fe9edc9e0df98e07454847909b5e959d7ca0e",
      "coingeckoId": "illuvium",
      "destinations": {
        "sol": {
          "address": "8UJbtpsEubDVkY53rk7d61hNYKkvouicczB2XmuwiG4g",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "KEEP": {
      "symbol": "KEEP",
      "name": "Keep Network (Portal)",
      "sourceAddress": "0x85eee30c52b0b379b046fb0f85f4f3dc3009afec",
      "coingeckoId": "keep-network",
      "destinations": {
        "sol": {
          "address": "64L6o4G2H7Ln1vN7AHZsUMW4pbFciHyuwn4wUdSbcFxh",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "KIN": {
      "symbol": "KIN",
      "name": "Kin1 Migration (Portal)",
      "sourceAddress": "0x818fc6c2ec5986bc6e2cbf00939d90556ab12ce5",
      "coingeckoId": "kin",
      "logo": "https://etherscan.io/token/images/kin_28_3.png?v=2",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "YdYQS1RK1ZTwCMH69pmpWk3W7eLhf99Nfu9b8Rqd9SD",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "KP3R": {
      "symbol": "KP3R",
      "name": "Keep3rV1 (Portal)",
      "sourceAddress": "0x1ceb5cb57c4d4e2b2433641b95dd330a33185a44",
      "coingeckoId": "keep3rv1",
      "destinations": {
        "sol": {
          "address": "3a2VW9t5N6p4baMW3M6yLH1UJ9imMt7VsyUk6ouXPVLq",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "LDO": {
      "symbol": "LDO",
      "name": "Lido DAO (Portal)",
      "sourceAddress": "0x5a98fcbea516cf06857215779fd812ca3bef1b32",
      "coingeckoId": "lido-dao",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/HZRCwxP2Vq9PCpPXooayhJ2bxTpo5xfpQrwB1svh332p/logo.png",
      "markets": {
        "sol": [
          "jupiter"
        ]
       },
      "destinations": {
        "bsc": {
          "address": "0x986854779804799C1d68867F5E03e601E781e41b",
          "decimals": 18
        },
        "sol": {
          "address": "HZRCwxP2Vq9PCpPXooayhJ2bxTpo5xfpQrwB1svh332p",
          "decimals": 8
        },
        "terra": {
          "address": "terra1jxypgnfa07j6w92wazzyskhreq2ey2a5crgt6z",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "LINK": {
      "symbol": "LINK",
      "name": "Chainlink (Portal)",
      "markets": {
      },
      "sourceAddress": "0x514910771af9ca656af840dff83e8264ecf986ca",
      "coingeckoId": "chainlink",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/2wpTofQ8SkACrkZWrZDjXPitYa8AwWgX8AfxdeBRRVLX/logo.png",
      "destinations": {
        "sol": {
          "address": "2wpTofQ8SkACrkZWrZDjXPitYa8AwWgX8AfxdeBRRVLX",
          "decimals": 8
        },
        "terra": {
          "address": "terra12dfv3f0e6m22z6cnhfn3nxk2en3z3zeqy6ctym",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "LRC": {
      "symbol": "LRC",
      "name": "Loopring (Portal)",
      "sourceAddress": "0xbbbbca6a901c926f240b89eacb641d8aec7aeafd",
      "coingeckoId": "loopring",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "HCTVFTzHL21a1dPzKxAUeWwqbE8QMUyvgChFDL4XYoi1",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "LUA": {
      "symbol": "LUA",
      "name": "LuaSwap (Portal)",
      "sourceAddress": "0xb1f66997a5760428d3a87d68b90bfe0ae64121cc",
      "coingeckoId": "luaswap",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "5Wc4U1ZoQRzF4tPdqKQzBwRSjYe8vEf3EvZMuXgtKUW6",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "MANA": {
      "symbol": "MANA",
      "name": "Decentraland (Portal)",
      "sourceAddress": "0x0F5D2fB29fb7d3CFeE444a200298f468908cC942",
      "coingeckoId": "decentraland",
      "logo": "https://assets.coingecko.com/coins/images/878/thumb/decentraland-mana.png",
      "markets": {
        "sol": [
          "raydium",
        ]
      },
      "destinations": {
        "sol": {
          "address": "7dgHoN8wBZCc5wbnQ2C47TDnBMAxG4Q5L3KjP67z8kNi",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "MATH": {
      "symbol": "MATH",
      "name": "MATH Token (Portal)",
      "sourceAddress": "0x08d967bb0134f2d07f7cfb6e246680c53927dd30",
      "coingeckoId": "math",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "CaGa7pddFXS65Gznqwp42kBhkJQdceoFVT7AQYo8Jr8Q",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "MATICet": {
      "symbol": "MATICet",
      "name": "MATIC (Portal from Ethereum)",
      "sourceAddress": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",
      "coingeckoId": "polygon",
      "destinations": {
        "sol": {
          "address": "C7NNPWuZCNjZBfW5p6JvGsR8pUdsRpEdP1ZAhnoDwj7h",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "MIMet": {
      "symbol": "MIMet",
      "name": "Magic Internet Money (Portal from Ethereum)",
      "sourceAddress": "0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3",
      "coingeckoId": "magic-internet-money",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/HRQke5DKdDo3jV7wnomyiM8AA3EzkVnxMDdo2FQ5XUe1/logo.png",
      "destinations": {
        "sol": {
          "address": "HRQke5DKdDo3jV7wnomyiM8AA3EzkVnxMDdo2FQ5XUe1",
          "decimals": 8
        },
        "terra": {
          "address": "terra15a9dr3a2a2lj5fclrw35xxg9yuxg0d908wpf2y",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "NXM": {
      "symbol": "NXM",
      "name": "Nexus Mutual (Portal)",
      "sourceAddress": "0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b",
      "coingeckoId": "nexus-mutual",
      "destinations": {
        "sol": {
          "address": "Aqs5ydqKXEK2cjotDXxHmk8N9PknqQ5q4ZED4ymY1eeh",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ORION": {
      "symbol": "ORION",
      "name": "Orion Money (Portal)",
      "sourceAddress": "0x727f064a78dc734d33eec18d5370aef32ffd46e4",
      "coingeckoId": "orion-money",
      "logo": "https://assets.coingecko.com/coins/images/18630/small/YtrqPIWc.png",
      "destinations": {
        "terra": {
          "address": "terra1mddcdx0ujx89f38gu7zspk2r2ffdl5enyz2u03",
          "decimals": 8
        },
        "bsc": {
          "address": "0x3dcB18569425930954feb191122e574b87F66abd",
          "decimals": 18
        },
        "matic": {
          "address": "0x5E0294Af1732498C77F8dB015a2d52a76298542B",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "PAXG": {
      "symbol": "PAXG",
      "name": "Paxos Gold (Portal)",
      "markets": {
      },
      "sourceAddress": "0x45804880de22913dafe09f4980848ece6ecbaf78",
      "coingeckoId": "pax-gold",
      "destinations": {
        "sol": {
          "address": "C6oFsE8nXRDThzrMEQ5SxaNFGKoyyfWDDVPw37JKvPTe",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "PENDLE": {
      "symbol": "PENDLE",
      "name": "Pendle",
      "sourceAddress": "0x808507121B80c02388fAd14726482e061B8da827",
      "coingeckoId": "pendle",
      "logo": "https://docs.pendle.finance/img/TokenLogo.png",
      "markets": {
        "bsc": [
          "pancakeswap",
        ]
      },
      "destinations": {
        "bsc": {
          "address": "0xb3Ed0A426155B79B898849803E3B36552f7ED507",
          "decimals": 18
        },
      },
      "sourceDecimals": 18
    },
    "PERP": {
      "symbol": "PERP",
      "name": "Perpetual Protocol (Portal)",
      "sourceAddress": "0xbc396689893d065f41bc2c6ecbee5e0085233447",
      "coingeckoId": "perpetual-protocol",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "9BsnSWDPfbusseZfnXyZ3un14CyPMZYvsKjWY3Y8Gbqn",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "PEOPLE": {
      "symbol": "PEOPLE",
      "name": "ConstitutionDAO (Portal)",
      "sourceAddress": "0x7a58c0be72be218b41c608b7fe7c5bb630736c71",
      "coingeckoId": "constitutiondao",
      "destinations": {
        "sol": {
          "address": "CobcsUrt3p91FwvULYKorQejgsm5HoQdv5T8RUZ6PnLA",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "RGT": {
      "symbol": "RGT",
      "name": "Rari Governance Token (Portal)",
      "sourceAddress": "0xd291e7a03283640fdc51b121ac401383a46cc623",
      "coingeckoId": "rari-governance-token",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "ASk8bss7PoxfFVJfXnSJepj9KupTX15QaRnhdjs6DdYe",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "RPL": {
      "symbol": "RPL",
      "name": "Rocket Pool (Portal)",
      "sourceAddress": "0xd33526068d116ce69f19a9ee46f0bd304f21a51f",
      "coingeckoId": "rocket-pool",
      "destinations": {
        "sol": {
          "address": "HUCyuyqESEUV4YWTKFvvB4JiQLqoovscTBpRXfGzW4Wx",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "RSR": {
      "symbol": "RSR",
      "name": "Reserve Rights (Portal)",
      "sourceAddress": "0x8762db106B2c2A0bccB3A80d1Ed41273552616E8",
      "coingeckoId": "reserve-rights-token",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "DkbE8U4gSRuGHcVMA1LwyZPYUjYbfEbjW8DMR3iSXBzr",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SAND": {
      "symbol": "SAND",
      "name": "The Sandbox (Portal)",
      "sourceAddress": "0x3845badAde8e6dFF049820680d1F14bD3903a5d0",
      "coingeckoId": "the-sandbox",
      "logo": "https://gemini.com/images/currencies/icons/default/sand.svg",
      "markets": {
        "sol": [
          "raydium",
        ]
      },
      "destinations": {
        "sol": {
          "address": "49c7WuCZkQgc3M4qH8WuEUNXfgwupZf1xqWkDQ7gjRGt",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SHIB": {
      "symbol": "SHIB",
      "name": "Shiba Inu (Portal)",
      "sourceAddress": "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce",
      "coingeckoId": "shiba-inu",
      "logo": "https://etherscan.io/token/images/shibatoken_32.png",
      "markets": {
        "sol": [
          "raydium",
        ]
      },
      "destinations": {
        "sol": {
          "address": "CiKu4eHsVrc1eueVQeHn7qhXTcVu95gSQmBpX4utjL9z",
          "decimals": 8
        },
        "bsc": {
          "address": "0xb1547683DA678f2e1F003A780143EC10Af8a832B",
          "decimals": 18
        },
        "terra": {
          "address": "terra1huku2lecfjhq9d00k5a8dh73gw7dwe6vvuf2dd",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SLP": {
      "symbol": "SLP",
      "name": "Smooth Love Potion (Portal)",
      "sourceAddress": "0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25",
      "coingeckoId": "smooth-love-potion",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "4hpngEp1v3CXpeKB81Gw4sv7YvwUVRKvY3SGag9ND8Q4",
          "decimals": 8
        }
      },
      "sourceDecimals": 0
    },
      "SPX6900": {
            "symbol": "SPX",
            "name": "SPX6900",
            "sourceAddress": "0xe0f63a424a4439cbe457d80e4f4b51ad25b2c56c",
            "coingeckoId": "spx6900",
            "logo": "https://assets.coingecko.com/coins/images/31401/standard/sticker_%281%29.jpg?1702371083",
            "markets": {"eth": ["uniswap"], "sol": ["raydium"], "base": ["uniswap"]},
            "destinations": {
                "sol": {
                    "address": "J3NKxxXZcnNiMjKw9hYb2K4LUxgwB6t1FtPtQVsv3KFr",
                    "decimals": 8,
                },
                "base":{
                  "address": "0x50dA645f148798F68EF2d7dB7C1CB22A6819bb2C",
                  "decimals": 8,
                }
            },
            "sourceDecimals": 8,
        },
    "SNX": {
      "symbol": "SNX",
      "name": "Synthetix Network Token (Portal)",
      "sourceAddress": "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f",
      "coingeckoId": "synthetix-network-token",
      "destinations": {
        "sol": {
          "address": "8cTNUtcV2ueC3royJ642uRnvTxorJAWLZc58gxAo7y56",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SOS": {
      "symbol": "SOS",
      "name": "OpenDAO (Portal)",
      "sourceAddress": "0x3b484b82567a09e2588a13d54d032153f0c0aee0",
      "coingeckoId": "opendao",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "6Q5fvsJ6kgAFmisgDqqyaFd9FURYzHf8MCUbpAUaGZnE",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SPELL": {
      "symbol": "SPELL",
      "name": "Spell Token (Portal)",
      "sourceAddress": "0x090185f2135308bad17527004364ebcc2d37e5f6",
      "coingeckoId": "spell-token",
      "destinations": {
        "sol": {
          "address": "BCsFXYm81iqXyYmrLKgAp3AePcgLHnirb8FjTs6sjM7U",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SRMet": {
      "symbol": "SRMet",
      "name": "Serum (Portal from Ethereum)",
      "sourceAddress": "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff",
      "coingeckoId": "serum",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG",
          "decimals": 6
        },
        "bsc": {
          "address": "0xd63CDf02853D759831550fAe7dF8FFfE0B317b39",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "SWAG": {
      "symbol": "SWAG",
      "name": "SWAG Finance (Portal)",
      "sourceAddress": "0x87edffde3e14c7a66c9b9724747a1c5696b742e6",
      "coingeckoId": "swag-finance",
      "destinations": {
        "sol": {
          "address": "5hcdG6NjQwiNhVa9bcyaaDsCyA1muPQ6WRzQwHfgeeKo",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SXP": {
      "symbol": "SXP",
      "name": "Swipe (Portal)",
      "sourceAddress": "0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9",
      "coingeckoId": "swipe",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "3CyiEDRehaGufzkpXJitCP5tvh7cNhRqd9rPBxZrgK5z",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SUSHI": {
      "symbol": "SUSHI",
      "name": "SushiToken (Portal)",
      "sourceAddress": "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2",
      "coingeckoId": "sushi",
      "logo": "https://etherscan.io/token/images/sushitoken_32.png",
      "markets": {
        "sol": [
          "raydium",
        ]
      },
      "destinations": {
        "sol": {
          "address": "ChVzxWRmrTeSgwd3Ui3UumcN8KX7VK3WaD4KGeSKpypj",
          "decimals": 8
        },
        "bsc": {
          "address": "0x3524fd7488fdb1F4723BBc22C9cbD1Bf89f46E3B",
          "decimals": 18
        },
        "terra": {
          "address": "terra1csvuzlf92nyemu6tv25h0l79etpe8hz3h5vn4a",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "T": {
      "symbol": "T",
      "name": "Threshold Network Token",
      "sourceAddress": "0xCdF7028ceAB81fA0C6971208e83fa7872994beE5",
      "coingeckoId": "threshold-network-token",
      "logo": "https://assets.coingecko.com/coins/images/22228/small/nFPNiSbL_400x400.jpg?1641220340",
      "markets": {
          "sol": ['threshold']
      },
      "destinations": {
        "sol": {
          "address": "4Njvi3928U3figEF5tf8xvjLC5GqUN33oe4XTJNe7xXC",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "TBTC": {
      "symbol": "TBTC",
      "name": "Threshold Bitcoin",
      "sourceAddress": "0x18084fbA666a33d37592fA2633fD49a74DD93a88",
      "coingeckoId": "tbtc",
      "logo": "https://assets.coingecko.com/coins/images/11224/small/0x18084fba666a33d37592fa2633fd49a74dd93a88.png?1674474504",
      "markets": {
        "matic": ['threshold'],
        "arbitrum": ['threshold'],
        "optimism": ['threshold'],
        "base": ['threshold'],
        "sol": ['threshold']
      },
      "destinations": {
        "matic": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "arbitrum": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "optimism": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "base": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "sol": {
            "address": "6DNSN2BJsaPFdFFc1zP37kkeNe4Usc1Sqkzr9C9vPWcU",
            "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "TOKE": {
      "symbol": "TOKE",
      "name": "Tokemak (Portal)",
      "sourceAddress": "0x2e9d63788249371f1dfc918a52f8d799f4a38c94",
      "coingeckoId": "tokemak",
      "destinations": {
        "sol": {
          "address": "3EQ6LqLkiFcoxTeGEsHMFpSLWNVPe9yT7XPX2HYSFyxX",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "TRIBE": {
      "symbol": "TRIBE",
      "name": "Tribe (Portal)",
      "sourceAddress": "0xc7283b66eb1eb5fb86327f08e1b5816b0720212b",
      "coingeckoId": "tribe",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "DPgNKZJAG2w1S6vfYHDBT62R4qrWWH5f45CnxtbQduZE",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "UBXT": {
      "symbol": "UBXT",
      "name": "UpBots (Portal)",
      "sourceAddress": "0x8564653879a18c560e7c0ea0e084c516c62f5653",
      "coingeckoId": "upbots",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "FTtXEUosNn6EKG2SQtfbGuYB4rBttreQQcoWn1YDsuTq",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "UFO": {
      "symbol": "UFO",
      "name": "UFO Gaming (Portal)",
      "sourceAddress": "0x249e38ea4102d0cf8264d3701f1a0e39c4f2dc3b",
      "coingeckoId": "ufo-gaming",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "GWdkYFnXnSJAsCBvmsqFLiPPe2tpvXynZcJdxf11Fu3U",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "UNI": {
      "symbol": "UNI",
      "name": "Uniswap (Portal)",
      "sourceAddress": "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
      "coingeckoId": "uniswap",
      "logo": "https://etherscan.io/token/images/uniswap_32.png",
      "markets": {
        "sol": [
          "raydium",
        ]
      },
      "destinations": {
        "sol": {
          "address": "8FU95xFJhUUkyyCLU13HSzDLs7oC4QZdXQHL6SCeab36",
          "decimals": 8
        },
        "terra": {
          "address": "terra1wyxkuy5jq545fn7xfn3enpvs5zg9f9dghf6gxf",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "USDCet": {
      "symbol": "USDCet",
      "name": "USD Coin (Portal from Ethereum)",
      "sourceAddress": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
      "coingeckoId": "usd-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/logo.png",
      "markets": {
        "eth": ["curve"],
        "sol": ["saber", "mercurial", "jupiter"],
#         "bsc": ["pancakeswap"],
#         "matic": ["quickswap"],
        "karura": ["karura"],
        "celo": ["ubeswap"],
        "moonbeam": ["stellaswap", "moonwell","beamswap"],
        "aptos": ["hippo", "liquidswap", "ariesmarkets"]
      },
      "destinations": {
        "sol": {
          "address": "A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM",
          "decimals": 6
        },
        "terra": {
          "address": "terra1pepwcav40nvj3kh60qqgrk8k07ydmc00xyat06",
          "decimals": 6
        },
        "bsc": {
          "address": "0xB04906e95AB5D797aDA81508115611fee694c2b3",
          "decimals": 6
        },
        "avax": {
          "address": "0xB24CA28D4e2742907115fECda335b40dbda07a4C",
          "decimals": 6
        },
        "matic": {
          "address": "0x4318cb63a2b8edf2de971e2f17f77097e499459d",
          "decimals": 6
        },
        "oasis": {
          "address": "0xE8A638b3B7565Ee7c5eb9755E58552aFc87b94DD",
          "decimals": 6
        },
        "ftm": {
          "address": "0x2Ec752329c3EB419136ca5e4432Aa2CDb1eA23e6",
          "decimals": 6
        },
        "celo": {
          "address": "0x37f750B7cC259A2f741AF45294f6a16572CF5cAd",
          "decimals": 6
        },
        "moonbeam": {
          "address": "0x931715FEE2d06333043d11F658C8CE934aC61D0c",
          "decimals": 6
        },
          "aptos": {
          "address": "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea",
          "decimals": 6
        },
      },
      
      "sourceDecimals": 6
    },
    "USDK": {
      "symbol": "USDK",
      "name": "USDK (Portal)",
      "sourceAddress": "0x1c48f86ae57291f7686349f12601910bd8d470bb",
      "coingeckoId": "usdk",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/43m2ewFV5nDepieFjT9EmAQnc1HRtAF247RBpLGFem5F/logo.png",
      "markets": {
        "eth": [
          "curve"
        ],
        "sol": [
          "saber",
        ]
      },
      "destinations": {
        "sol": {
          "address": "43m2ewFV5nDepieFjT9EmAQnc1HRtAF247RBpLGFem5F",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "USDTet": {
      "symbol": "USDTet",
      "name": "Tether USD (Portal from Ethereum)",
      "sourceAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
      "coingeckoId": "tether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB/logo.svg",
      "markets": {
        "eth": ["curve"],
        "sol": ["saber", "mercurial", "jupiter"],
      },
      "destinations": {
        "sol": {
          "address": "Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1",
          "decimals": 6
        },
        "terra": {
          "address": "terra1ce06wkrdm4vl6t0hvc0g86rsy27pu8yadg3dva",
          "decimals": 6
        },
        "bsc": {
          "address": "0x524bC91Dc82d6b90EF29F76A3ECAaBAffFD490Bc",
          "decimals": 6
        },
        "matic": {
          "address": "0x9417669fBF23357D2774e9D421307bd5eA1006d2",
          "decimals": 6
        },
        "oasis": {
          "address": "0xdC19A122e268128B5eE20366299fc7b5b199C8e3",
          "decimals": 6
        },
        "celo": {
          "address": "0x617f3112bf5397D0467D315cC709EF968D9ba546",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "WBTC": {
      "symbol": "WBTC",
      "name": "Wrapped BTC (Portal)",
      "sourceAddress": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
      "coingeckoId": "wrapped-bitcoin",
      "logo": "https://etherscan.io/token/images/wbtc_28.png?v=1",
      "markets": {
        "moonbeam": ["stellaswap", "moonwell","beamex"],
        "sol": ["orca", "raydium"],
        "algorand": ["pact"], 
      },
      "destinations": {
        "sol": {
          "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
          "decimals": 8
        },
        "terra": {
          "address": "terra1aa7upykmmqqc63l924l5qfap8mrmx5rfdm0v55",
          "decimals": 8
        },
        "matic": {
          "address": "0x5D49c278340655B56609FdF8976eb0612aF3a0C3",
          "decimals": 8
        },
        "oasis": {
          "address": "0xd43ce0aa2a29DCb75bDb83085703dc589DE6C7eb",
          "decimals": 8
        },
        "moonbeam": {
          "address": "0xE57eBd2d67B462E9926e04a8e33f01cD0D64346D",
          "decimals": 8
        },
        "algorand": {
          "address": "1058926737",
          "decimals": 8
        }
      },
      "sourceDecimals": 8
    },
    "XCAD": {
      "symbol": "XCAD",
      "name": "XCAD Token",
      "sourceAddress": "0x7659CE147D0e714454073a5dd7003544234b6Aa0",
      "coingeckoId": "xcad-network",
      "markets": {},
      "destinations": {
        "bsc": {
          "address": "0xa026ad2ceda16ca5fc28fd3c72f99e2c332c8a26",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "YFI": {
      "symbol": "YFI",
      "name": "yearn.finance (Portal)",
      "sourceAddress": "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e",
      "coingeckoId": "yearn-finance",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "BXZX2JRJFjvKazM1ibeDFxgAngKExb74MRXzXKvgikxX",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "YGG": {
      "symbol": "YGG",
      "name": "Yield Guild Games (Portal)",
      "sourceAddress": "0x25f8087ead173b73d6e8b84329989a8eea16cf73",
      "coingeckoId": "yield-guild-games",
      "markets": {},
      "destinations": {
        "sol": {
          "address": "EzZp7LRN1xwu3QsB2RJRrWwEGjJGsuWzuMCeQDB3NSPK",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ZRX": {
      "symbol": "ZRX",
      "name": "0x (Portal)",
      "sourceAddress": "0xe41d2489571d322189246dafa5ebde1f4699f498",
      "coingeckoId": "0x",
      "destinations": {
        "sol": {
          "address": "GJa1VeEYLTRoHbaeqcxfzHmjGCGtZGF3CUqxv9znZZAY",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "agEUR": {
      "symbol": "agEUR",
      "name": "agEUR (Portal)",
      "markets": {
      },
      "sourceAddress": "0x1a7e4e63778B4f12a199C062f3eFdD288afCBce8",
      "coingeckoId": "ageur",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/CbNYA9n3927uXUukee2Hf4tm3xxkffJPPZvGazc2EAH1/logo.svg",
      "destinations": {
        "sol": {
          "address": "CbNYA9n3927uXUukee2Hf4tm3xxkffJPPZvGazc2EAH1",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "gOHM": {
      "symbol": "gOHM",
      "name": "Governance OHM (Portal)",
      "sourceAddress": "0x0ab87046fbb341d058f17cbc4c1133f25a20a52f",
      "coingeckoId": "governance-ohm",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/FUGsN8H74WjRBBMfQWcf9Kk32gebA9VnNaGxqwcVvUW7/logo.png",
      "destinations": {
        "sol": {
          "address": "FUGsN8H74WjRBBMfQWcf9Kk32gebA9VnNaGxqwcVvUW7",
          "decimals": 8
        },
        "terra": {
          "address": "terra1fpfn2kkr8mv390wx4dtpfk3vkjx9ch3thvykl3",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "ibBTC": {
      "symbol": "ibBTC",
      "name": "Interest Bearing Bitcoin (Portal)",
      "sourceAddress": "0xc4e15973e6ff2a35cc804c2cf9d2a1b817a8b40f",
      "coingeckoId": "interest-bearing-bitcoin",
      "logo": "https://etherscan.io/token/images/badgeribtc_32.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "Bzq68gAVedKqQkQbsM28yQ4LYpc2VComDUD9wJBywdTi",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "bETH": {
      "symbol": "bETH",
      "name": "Lido bETH (Portal)",
      "sourceAddress": "0x707f9118e33a9b8998bea41dd0d46f38bb963fc8",
      "coingeckoId": "anchor-beth-token",
      "logo": "https://static.lido.fi/bETH/bETH.png",
      "markets": {
      },
      "destinations": {
        "terra": {
          "address": "terra1u5szg038ur9kzuular3cae8hq6q5rk5u27tuvz",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "wstETH": {
      "symbol": "wstETH",
      "name": "Lido wstETH (Portal)",
      "sourceAddress": "0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0",
      "coingeckoId": "wrapped-steth",
      "logo": "https://static.lido.fi/wstETH/wstETH.png",
      "destinations": {
        "terra": {
          "address": "terra133chr09wu8sakfte5v7vd8qzq9vghtkv4tn0ur",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "stETH": {
      "symbol": "stETH",
      "name": "Lido Staked Ether (Portal)",
      "sourceAddress": "0xae7ab96520de3a18e5e111b5eaab095312d7fe84",
      "coingeckoId": "lido-staked-ether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/H2mf9QNdU2Niq6QR7367Ua2trBsvscLyX5bz7R3Pw5sE/logo.png",
      "destinations": {
        "sol": {
          "address": "H2mf9QNdU2Niq6QR7367Ua2trBsvscLyX5bz7R3Pw5sE",
          "decimals": 8
        },
        "terra": {
          "address": "terra1w7ywr6waxtjuvn5svk5wqydqpjj0q9ps7qct4d",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "SD": {
      "symbol": "SD",
      "name": "Stader SD (Portal)",
      "sourceAddress": "0x30D20208d987713f46DFD34EF128Bb16C404D10f",
      "coingeckoId": "stader",
      "logo": "https://raw.githubusercontent.com/stader-labs/assets/fb5f931ead18cea7480aff37c18c203ed3ba8ae3/eth/SD.png",
      "destinations": {
        "terra": {
          "address": "terra1ustvnmngueq0p4jd7gfnutgvdc6ujpsjhsjd02",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "HOOD": {
      "symbol": "HOOD",
      "name": "wagmicatgirlkanye420etfmoon1000x",
      "sourceAddress": "0x04815313E9329e8905A77251A1781CfA7934259a",
      "coingeckoId": "wagmicatgirlkanye420etfmoon1000x",
      "logo": "https://raw.githubusercontent.com/wormhole-foundation/wormhole-token-list/main/src/logogen/base/HOOD.png",
      "markets": {
          "eth": ["uniswap"],
          "sol": ["raydium"]
      },
      "destinations": {
        "sol": {
          "address": "AGyUuFvYGnUUXWG6GUKga4B3MGmBuEZ9hGqY73n76XpJ",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "USDEBT": {
      "symbol": "USDEBT",
      "name": "USDEBT (Wormhole)",
      "sourceAddress": "0x00c5CA160A968f47e7272A0CFCda36428F386CB6",
      "coingeckoId": "usdebt",
      "logo": "https://raw.githubusercontent.com/denysnizamiiev/wormhole-token-list/main/assets/USDEBT_wh.png",
      "markets": {
          "eth": ["uniswap"],
          "sol": ["raydium"]
      },
      "destinations": {
        "sol": {
          "address": "Fm22RbypFLJeR3tjUKK2EGERj78PZVoNwE5wiDYqPHvN",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
  },
  #####################
  # 3. Terra native
  #####################
  "terra": {
    "UST": {
      "symbol": "UST",
      "name": "UST (Portal)",
      "sourceAddress": "uusd",
      "coingeckoId": "terra-usd",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/9vMJfxuKxXBoEa7rM12mYLMwTacLMLDJqHozw96WQL8i/logo.png",
      "markets": {
      },
      "destinations": {
        "terra2": {
          "address": "terra1rwg5kt6kcyxtz69acjgpeut7dgr4y3r7tvntdxqt03dvpqktrfxq4jrvpq",
          "decimals": 6
        },
        "sol": {
          "address": "9vMJfxuKxXBoEa7rM12mYLMwTacLMLDJqHozw96WQL8i",
          "decimals": 6
        },
        "eth": {
          "address": "0xa693B19d2931d498c5B318dF961919BB4aee87a5",
          "decimals": 6
        },
        "bsc": {
          "address": "0x3d4350cD54aeF9f9b2C29435e0fa809957B3F30a",
          "decimals": 6
        },
        "matic": {
          "address": "0xE6469Ba6D2fD6130788E0eA9C0a0515900563b59",
          "decimals": 6
        },
        "avax": {
          "address": "0xb599c3590F42f8F995ECfa0f85D2980B76862fc1",
          "decimals": 6
        },
        "oasis": {
          "address": "0xa1E73c01E0cF7930F5e91CB291031739FE5Ad6C2",
          "decimals": 6
        },
        "aurora": {
          "address": "0x8D07bBb478B84f7E940e97C8e9cF7B3645166b03",
          "decimals": 6
        },
        "ftm": {
          "address": "0x846e4D51d7E2043C1a87E0Ab7490B93FB940357b",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "LUNA": {
      "symbol": "LUNA",
      "name": "LUNA (Portal)",
      "sourceAddress": "uluna",
      "coingeckoId": "terra-luna",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/F6v4wfAdJB8D8p77bMXZgYt8TDKsYxLYxH5AFhUkYx9W/logo.png",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "F6v4wfAdJB8D8p77bMXZgYt8TDKsYxLYxH5AFhUkYx9W",
          "decimals": 6
        },
        "eth": {
          "address": "0xbd31ea8212119f94a611fa969881cba3ea06fa3d",
          "decimals": 6
        },
        "terra2" : {
          "address" : "terra16h7keds26d52xj8rn9jfx6lj2x0ja79lt56yxnmlm4xsttf5mu5smq5f78",
          "decimals" : 6
        },
        "bsc": {
          "address": "0x156ab3346823B651294766e23e6Cf87254d68962",
          "decimals": 6
        },
        "matic": {
          "address": "0x9cd6746665D9557e1B9a775819625711d0693439",
          "decimals": 6
        },
        "avax": {
          "address": "0x70928E5B188def72817b7775F0BF6325968e563B",
          "decimals": 6
        },
        "oasis": {
          "address": "0x4F43717B20ae319Aa50BC5B2349B93af5f7Ac823",
          "decimals": 6
        },
        "aurora": {
          "address": "0x12302fbE05a7e833f87d4B7843F58d19BE4FdE3B",
          "decimals": 6
        },
        "ftm": {
          "address": "0x593AE1d34c8BD7587C11D539E4F42BFf242c82Af",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "aUST": {
      "symbol": "aUST",
      "name": "AnchorUST (Portal)",
      "sourceAddress": "terra1hzh9vpxhsk8253se0vv5jj6etdvxu3nv8z07zu",
      "coingeckoId": "anchorust",
      "markets": {
      },
      "destinations": {
        "sol": {
          "address": "4CsZsUCoKFiaGyU7DEVDayqeVtG8iqgGDR6RjzQmzQao",
          "decimals": 6
        },
        "bsc": {
          "address": "0x8b04E56A8cd5f4D465b784ccf564899F30Aaf88C",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    }
  },
  #####################
  # 4. BSC native
  #####################
  "bsc": {
    "BNB": {
      "symbol": "BNB",
      "name": "Binance Coin (Portal)",
      "sourceAddress": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
      "coingeckoId": "binance-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa/logo.png",
      "markets": {
        "sol": ["mercurial", "jupiter"],
        "bsc": ["pancakeswap"], #revert to native asset
      },
      "destinations": {
        "sol": {
          "address": "9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa",
          "decimals": 8
        },
        "eth": {
          "address": "0x418D75f65a02b3D53B2418FB8E1fe493759c7605",
          "decimals": 18
        },
        "terra2": {
          "address": "terra1xc7ynquupyfcn43sye5pfmnlzjcw2ck9keh0l2w2a4rhjnkp64uq4pr388",
          "decimals": 8
        },
        "terra": {
          "address": "terra1cetg5wruw2wsdjp7j46rj44xdel00z006e9yg8",
          "decimals": 8
        },
        "avax": {
          "address": "0x442F7f22b1EE2c842bEAFf52880d4573E9201158",
          "decimals": 18
        },
        "matic": {
          "address": "0xecdcb5b88f8e3c15f95c720c51c71c9e2080525d",
          "decimals": 18
        },
        "oasis": {
          "address": "0xd79Ef9A91b56c690C7b80570a3c060678667f469",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "BUSDbs": {
      "symbol": "BUSDbs",
      "name": "Binance USD (Portal from BSC)",
      "sourceAddress": "0xe9e7cea3dedca5984780bafc599bd69add087d56",
      "coingeckoId": "binance-usd",
      "logo": "https://etherscan.io/token/images/binanceusd_32.png",
      "markets": {
        "sol": ["saber", "mercurial", "jupiter"],
#         "matic": ["quickswap"],
        "bsc": ["pancakeswap"], #revert to native asset
        "moonbeam":["stellaswap", "moonwell"],
      },
      "destinations": {
        "sol": {
          "address": "5RpUwQ8wtdPCZHhu6MERp2RGrpobsbZ6MH5dDHkUjs2",
          "decimals": 8
        },
        "eth": {
          "address": "0x7B4B0B9b024109D182dCF3831222fbdA81369423",
          "decimals": 18
        },
        "terra": {
          "address": "terra1skjr69exm6v8zellgjpaa2emhwutrk5a6dz7dd",
          "decimals": 8
        },
        "avax": {
          "address": "0xA41a6c7E25DdD361343e8Cb8cFa579bbE5eEdb7a",
          "decimals": 18
        },
        "matic": {
          "address": "0xa8d394fe7380b8ce6145d5f85e6ac22d4e91acde",
          "decimals": 18
        },
        "oasis": {
          "address": "0xf6568FD76f9fcD1f60f73b730F142853c5eF627E",
          "decimals": 18
        },
        "moonbeam": {
          "address": "0x692C57641fc054c2Ad6551Ccc6566EbA599de1BA",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "CAKE": {
      "symbol": "CAKE",
      "name": "PancakeSwap Token (Portal)",
      "sourceAddress": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
      "coingeckoId": "pancakeswap",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/J8LKx7pr9Zxh9nMhhT7X3EBmj5RzuhFrHKyJAe2F2i9S/logo.png",
      "destinations": {
        "sol": {
          "address": "J8LKx7pr9Zxh9nMhhT7X3EBmj5RzuhFrHKyJAe2F2i9S",
          "decimals": 8
        },
        "eth": {
          "address": "0x7c8161545717a334f3196e765d9713f8042EF338",
          "decimals": 18
        },
        "terra": {
          "address": "terra1xvqlpjl2dxyel9qrp6qvtrg04xe3jh9cyxc6av",
          "decimals": 8
        },
        "avax": {
          "address": "0x98a4d09036Cc5337810096b1D004109686E56Afc",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "USDCbs": {
      "symbol": "USDCbs",
      "name": "USD Coin (Portal from BSC)",
      "sourceAddress": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
      "coingeckoId": "usd-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/logo.png",
      "markets": {
        "sol": ["saber", "mercurial", "jupiter"],
        "bsc": ["pancakeswap"], #revert to native asset
      },
      "destinations": {
        "sol": {
          "address": "FCqfQSujuPxy6V42UvafBhsysWtEq1vhjfMN1PUbgaxA",
          "decimals": 8
        },
        "eth": {
          "address": "0x7cd167B101D2808Cfd2C45d17b2E7EA9F46b74B6",
          "decimals": 18
        },
        "terra": {
          "address": "terra1yljlrxvkar0c6ujpvf8g57m5rpcwl7r032zyvu",
          "decimals": 8
        },
        "avax": {
          "address": "0x6145E8a910aE937913426BF32De2b26039728ACF",
          "decimals": 18
        },
        "oasis": {
          "address": "0x4cA2A3De42eabC8fd8b0AC46127E64DB08b9150e",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "USDTbs": {
      "symbol": "USDTbs",
      "name": "Tether USD (Portal from BSC)",
      "sourceAddress": "0x55d398326f99059fF775485246999027B3197955",
      "coingeckoId": "tether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB/logo.svg",
      "markets": {
        "sol": ["saber", "mercurial", "jupiter"],
        "bsc": ["pancakeswap"], #revert to native asset
      },
      "destinations": {
        "sol": {
          "address": "8qJSyQprMC57TWKaYEmetUR3UUiTP2M3hXdcvFhkZdmv",
          "decimals": 8
        },
        "eth": {
          "address": "0xDe60aDfDdAAbaAAC3dAFa57B26AcC91Cb63728c4",
          "decimals": 18
        },
        "terra": {
          "address": "terra1vlqeghv5mt5udh96kt5zxlh2wkh8q4kewkr0dd",
          "decimals": 8
        },
        "avax": {
          "address": "0xA67BCC0D06d7d13A13A2AE30bF30f1B434f5a28B",
          "decimals": 18
        },
        "oasis": {
          "address": "0x366EF31C8dc715cbeff5fA54Ad106dC9c25C6153",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "WOM": {
      "symbol": "WOM",
      "name": "Wombat Exchange",
      "sourceAddress": "0xad6742a35fb341a9cc6ad674738dd8da98b94fb1",
      "coingeckoId": "wombat-exchange",
      "logo": "https://s2.coinmarketcap.com/static/img/coins/64x64/19623.png",
      "markets": {
        "bsc": ["pancakeswap"], #revert to native asset
        "arbitrum": ["uniswap"],
        "eth": ["pancakeswap"]
      },
      "destinations": {
        "arbitrum": {
          "address": "0x7b5eb3940021ec0e8e463d5dbb4b7b09a89ddf96",
          "decimals": 18
        },
        "eth": {
          "address": "0xc0B314a8c08637685Fc3daFC477b92028c540CFB",
          "decimals": 18
        },
        "avax": {
          "address": "0xa15E4544D141aa98C4581a1EA10Eb9048c3b3382",
          "decimals": 18
        },
        "optimism": {
          "address": "0xD2612B256F6f76feA8C6fbca0BF3166D0d13a668",
          "decimals": 18
        },
        "base": {
          "address": "0xD9541B08B375D58ae104EC247d7443D2D7235D64",
          "decimals": 18
        },
        "matic": {
          "address": "0x77749d37A87BFf80060c00152B213F61341A6de5",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "QUO": {
      "symbol": "QUO",
      "name": "Quoll Finance",
      "sourceAddress": "0x08b450e4a48C04CDF6DB2bD4cf24057f7B9563fF",
      "coingeckoId": "quoll-finance",
      "logo": "https://s2.coinmarketcap.com/static/img/coins/64x64/22468.png",
      "markets": {
        "bsc": ["pancakeswap"], #revert to native asset
        "arbitrum": ["uniswap"]
      },
      "destinations": {
        "arbitrum": {
          "address": "0xf00D8790A76ee5A5Dbc10eaCac39151aa2af0331",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "MGP": {
      "symbol": "MGP",
      "name": "Magpie",
      "sourceAddress": "0xD06716E1Ff2E492Cc5034c2E81805562dd3b45fa",
      "coingeckoId": "magpie",
      "logo": "https://assets.coingecko.com/coins/images/27972/small/MagpieLogo.png?1666771448",
      "markets": {
        "bsc": ["pancakeswap"], #revert to native asset
        "arbitrum": ["traderjoe"]
      },
      "destinations": {
        "arbitrum": {
          "address": "0xa61F74247455A40b01b0559ff6274441FAfa22A3",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "WMX": {
      "symbol": "WMX",
      "name": "Wombex Finance",
      "sourceAddress": "0xa75d9ca2a0a1D547409D82e1B06618EC284A2CeD",
      "coingeckoId": "wombex",
      "logo": "https://wombex.finance/logo.png",
      "markets": {
        "bsc": ["pancakeswap"], #revert to native asset
        "arbitrum": ["camelot"]
      },
      "destinations": {
        "arbitrum": {
          "address": "0x5190F06EaceFA2C552dc6BD5e763b81C73293293",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "UNW": {
      "symbol": "UNW",
      "name": "Uniwhale Token",
      "sourceAddress": "0x5b65cd9feb54F1Df3D0C60576003344079f8Dc06",
      "coingeckoId": "uniwhale",
      "logo": "https://assets.coingecko.com/coins/images/29531/small/token-256x256.png?1680260871",
      "markets": {
        "bsc": ["pancakeswap"],
      },
      "destinations": {
        "arbitrum": {
          "address": "0xF73Ce9D8F7BDDCC38Cb3e662Cb93622B2145a47f",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    }
  },
  #####################
  # 5. Polygon native
  #####################
  "matic": {
    "DAIpo": {
      "symbol": "DAIpo",
      "name": "DAI (Portal from Polygon)",
      "sourceAddress": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
      "coingeckoId": "dai",
      "destinations": {
        "sol": {
          "address": "4Fo67MYQpVhZj9R7jQTd63FPAnWbPpaafAUxsMGX2geP",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "MATICpo": {
      "symbol": "MATICpo",
      "name": "MATIC (Portal from Polygon)",
      "sourceAddress": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
      "coingeckoId": "polygon",
      "markets": {
#        "bsc": ["pancakeswap"],
      },
      "destinations": {
        "sol": {
          "address": "Gz7VkD4MacbEB6yC5XD3HcumEiYx2EtDYYrfikGsvopG",
          "decimals": 8
        },
        "eth": {
          "address": "0x7c9f4C87d911613Fe9ca58b579f737911AAD2D43",
          "decimals": 18
        },
        "terra": {
          "address": "terra1dtqlfecglk47yplfrtwjzyagkgcqqngd5lgjp8",
          "decimals": 8
        },
        "bsc": {
          "address": "0xc836d8dC361E44DbE64c4862D55BA041F88Ddd39",
          "decimals": 18
        },
        "avax": {
          "address": "0xf2f13f0B7008ab2FA4A2418F4ccC3684E49D20Eb",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "QUICK": {
      "symbol": "QUICK",
      "name": "Quickswap (Portal)",
      "sourceAddress": "0x831753dd7087cac61ab5644b308642cc1c33dc13",
      "coingeckoId": "quickswap",
      "destinations": {
        "sol": {
          "address": "5njTmK53Ss5jkiHHZvzabVzZj6ztu6WYWpAPYgbVnbjs",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "TBTC": {
      "symbol": "TBTC",
      "name": "Threshold Bitcoin",
      "sourceAddress": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
      "coingeckoId": "tbtc",
      "logo": "https://assets.coingecko.com/coins/images/11224/small/0x18084fba666a33d37592fa2633fd49a74dd93a88.png?1674474504",
      "markets": {
        "eth": ['threshold'],
        "arbitrum": ['threshold'],
        "optimism": ['threshold'],
        "base": ['threshold'],
        "sol": ['threshold']
      },
      "destinations": {
        "eth": {
          "address": "0x18084fbA666a33d37592fA2633fD49a74DD93a88",
          "decimals": 8
        },
        "arbitrum": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "optimism": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "base": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "sol": {
            "address": "6DNSN2BJsaPFdFFc1zP37kkeNe4Usc1Sqkzr9C9vPWcU",
            "decimals": 8
        }
      },
      "sourceDecimals": 18
    },
    "USDCpo": {
      "symbol": "USDCpo",
      "name": "USD Coin (PoS) (Portal from Polygon)",
      "sourceAddress": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
      "coingeckoId": "usd-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/logo.png",
      "markets": {
        "matic": ["quickswap", "sushi"],
        "sol": ["saber", "jupiter"],
        "eth": ["uniswap"],
#         "bsc": ["pancakeswap"],
      },
      "destinations": {
        "sol": {
          "address": "E2VmbootbVCBkMNNxKQgCLMS1X3NoGMaYAsufaAsf7M",
          "decimals": 6
        },
        "eth": {
          "address": "0x566957eF80F9fd5526CD2BEF8BE67035C0b81130",
          "decimals": 6
        },
        "terra": {
          "address": "terra1kkyyh7vganlpkj0gkc2rfmhy858ma4rtwywe3x",
          "decimals": 6
        },
        "bsc": {
          "address": "0x672147dD47674757C457eB155BAA382cc10705Dd",
          "decimals": 6
        },
        "avax": {
          "address": "0x543672E9CBEC728CBBa9C3Ccd99ed80aC3607FA8",
          "decimals": 6
        },
        "oasis": {
          "address": "0x3E62a9c3aF8b810dE79645C4579acC8f0d06a241",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "USDTpo": {
      "symbol": "USDTpo",
      "name": "Tether USD (PoS) (Portal from Polygon)",
      "sourceAddress": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
      "coingeckoId": "tether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1/logo.png",
      "markets": {
        "matic": ["quickswap", "sushi"],
        "sol": ["saber", "jupiter"],
      },
      "destinations": {
        "sol": {
          "address": "5goWRao6a3yNC4d6UjMdQxonkCMvKBwdpubU3qhfcdf1",
          "decimals": 6
        },
        "oasis": {
          "address": "0xFffD69E757d8220CEA60dc80B9Fe1a30b58c94F3",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
    "WOM": {
      "symbol": "WOM",
      "name": "Wombat Exchange",
      "sourceAddress": "0xad6742a35fb341a9cc6ad674738dd8da98b94fb1",
      "coingeckoId": "wombat-exchange",
      "logo": "https://bscscan.com/token/images/wombatex_32.png",
      "markets": {
        "bsc": ["pancakeswap"], #revert to native asset
        "arbitrum": ["uniswap"]
      },
      "destinations": {
        "arbitrum": {
          "address": "0x7b5eb3940021ec0e8e463d5dbb4b7b09a89ddf96",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    }
  },
  #####################
  # 6. Avalanche native
  #####################
  "avax": {
    "AVAX": {
      "symbol": "AVAX",
      "name": "AVAX (Portal)",
      "markets": {
#         "bsc": ["pancakeswap"],
        "avax": ["traderjoe", "pangolin"],
      },
      "sourceAddress": "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
      "coingeckoId": "avalanche",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE/logo.png",
      "destinations": {
        "sol": {
          "address": "KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE",
          "decimals": 8
        },
        "eth": {
          "address": "0x85f138bfEE4ef8e540890CFb48F620571d67Eda3",
          "decimals": 18
        },
        "terra2": {
          "address": "terra1qmnxhecc3vnmhef9q7vap7spx9tgpnw9fqe8ljqfwrlz7rur9y5qu2dlp6",
          "decimals": 8
        },
        "terra": {
          "address": "terra1hj8de24c3yqvcsv9r8chr03fzwsak3hgd8gv3m",
          "decimals": 8
        },
        "bsc": {
          "address": "0x96412902aa9aFf61E13f085e70D3152C6ef2a817",
          "decimals": 18
        },
        "matic": {
          "address": "0x7Bb11E7f8b10E9e571E5d8Eace04735fDFB2358a",
          "decimals": 18
        },
        "oasis": {
          "address": "0x32847e63E99D3a044908763056e25694490082F8",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    },
    "JOE": {
      "symbol": "JOE",
      "name": "JoeToken (Portal)",
      "sourceAddress": "0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd",
      "coingeckoId": "joe",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/CriXdFS9iRAYbGEQiTcUqbWwG9RBmYt5B6LwTnoJ61Sm/logo.png",
      "destinations": {
        "sol": {
          "address": "CriXdFS9iRAYbGEQiTcUqbWwG9RBmYt5B6LwTnoJ61Sm",
          "decimals": 8
        }
      },
      "sourceDecimals": 18
    },

# USDC.e
    "USDCeav": {
      "symbol": "USDCeav",
      "name": "USD.e Coin (Portal from Avalanche)",
      "markets": {
      }, 
      "sourceAddress": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664",
      "coingeckoId": "usd-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/AGqKX7F4mqJ8x2mUQVangJb5pWQJApaKoUfe5gXM53CV/logo.png",
      "destinations": {
        "sol": {
          "address": "AGqKX7F4mqJ8x2mUQVangJb5pWQJApaKoUfe5gXM53CV",
          "decimals": 8
        },
        "terra": {
          "address": "terra1pvel56a2hs93yd429pzv9zp5aptcjg5ulhkz7w",
          "decimals": 6
        },
        "bsc": {
          "address": "0xc1F47175d96Fe7c4cD5370552e5954f384E3C791",
          "decimals": 6
        },
        "oasis": {
          "address": "0x05CbE6319Dcc937BdbDf0931466F4fFd0d392B47",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
# USDT.e
    "USDTeav": {
      "symbol": "USDTeav",
      "name": "Tether USD.e (Portal from Avalanche)",
      "sourceAddress": "0xc7198437980c041c805a1edcba50c1ce5db95118",
      "coingeckoId": "tether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/B2wfeYz5VtBnQVrX4M8F6FeDrprVrzKPws5qg1in8bzR/logo.png",
      "destinations": {
        "sol": {
          "address": "B2wfeYz5VtBnQVrX4M8F6FeDrprVrzKPws5qg1in8bzR",
          "decimals": 8
        },
        "terra": {
          "address": "terra1eqvq3thjhye7anv6f6mhxpjhyvww8zjvqcdgjx",
          "decimals": 6
        },
        "bsc": {
          "address": "0x2B90E061a517dB2BbD7E39Ef7F733Fd234B494CA",
          "decimals": 6
        },
        "oasis": {
          "address": "0x05832a0905E516f29344ADBa1c2052a788B10129",
          "decimals": 6
        }
      },
      "sourceDecimals": 6
    },
#USDC
    "USDCav": {
      "symbol": "USDCav",
      "name": "USD Coin (Portal from Avalanche)",
      "markets": {
      }, 
      "sourceAddress": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
      "coingeckoId": "usd-coin",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/AGqKX7F4mqJ8x2mUQVangJb5pWQJApaKoUfe5gXM53CV/logo.png",
      "destinations": {
        "sol": {
          "address": "FHfba3ov5P3RjaiLVgh8FTv4oirxQDoVXuoUUDvHuXax",
          "decimals": 8
        },
      },
      "sourceDecimals": 6
    },
#USDT
    "USDTav": {
      "symbol": "USDTav",
      "name": "Tether USD (Portal from Avalanche)",
      "sourceAddress": "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
      "coingeckoId": "tether",
      "logo": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/B2wfeYz5VtBnQVrX4M8F6FeDrprVrzKPws5qg1in8bzR/logo.png",
      "destinations": {
        "sol": {
          "address": "Kz1csQA91WUGcQ2TB3o5kdGmWmMGp8eJcDEyHzNDVCX",
          "decimals": 8
        },
      },
      "sourceDecimals": 6
    },
  },
  #################
  # 7. Oasis native
  #################
  "oasis": {
    "ROSE": {
      "symbol": "ROSE",
      "name": "ROSE (Portal)",
      "markets": {},
      "sourceAddress": "0x21C718C22D52d0F3a789b752D4c2fD5908a8A733",
      "coingeckoId": "oasis-network",
      "logo": "https://assets.coingecko.com/coins/images/13162/small/rose.png",
      "destinations": {
        "sol": {
          "address": "S3SQfD6RheMXQ3EEYn1Z5sJsbtwfXdt7tSAVXPQFtYo",
          "decimals": 8
        },
        "eth": {
          "address": "0x26B80FBfC01b71495f477d5237071242e0d959d7",
          "decimals": 18
        },
        "bsc": {
          "address": "0x6c6D604D3f07aBE287C1A3dF0281e999A83495C0",
          "decimals": 18
        },
        "avax": {
          "address": "0x12AF5C1a232675f62F405b5812A80e7a6F75D746",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    }
  },
  #################
  # 8. Algorand native
  #################
  "algorand": {
  },
  #################
  # 9. Aurora native
  #################
  "aurora": {
  },
  #################
  # 10. Fantom native
  #################
  "ftm": {
    "FTM": {
      "symbol": "FTM",
      "name": "Fantom (Portal)",
      "markets": {},
      "sourceAddress": "0x21be370d5312f44cb42ce377bc9b8a0cef1a4c83",
      "coingeckoId": "fantom",
      "logo": "https://assets.coingecko.com/coins/images/4001/small/Fantom.png",
      "destinations": {},
      "sourceDecimals": 18
    }
  },
  #################
  # 11. Karura native
  #################
  "karura": {
  },
  #################
  # 12. Acala native
  #################
  "acala": {
  },
  #################
  # 13. Klaytn native
  #################
  "klaytn": {
  },
  #################
  # 14. Celo native
  #################
  "celo": {
    "cUSD": {
      "symbol": "cUSD",
      "name": "Celo Dollar (Wormhole)",
      "sourceAddress": "0x765DE816845861e75A25fCA122bb6898B8B1282a",
      "coingeckoId": "celo-dollar",
      "logo": "https://assets.coingecko.com/coins/images/13161/small/icon-celo-dollar-color-1000-circle-cropped.png?1605771134",
      "markets": {
        "eth": ["curve"],
      },
      "destinations": {
        "eth": {
          "address": "0xC22956c3CFeC3Ee9A9925abeE044F05Bc47f6632",
          "decimals": 18
        },
      },
    },
    "cEUR": {
      "symbol": "cEUR",
      "name": "Celo Euro (Wormhole)",
      "sourceAddress": "0xd8763cba276a3738e6de85b4b3bf5fded6d6ca73",
      "coingeckoId": "celo-euro",
      "logo": "https://assets.coingecko.com/coins/images/16756/small/CEUR.png?1624947266",
      "markets": {
        "eth": ["curve"],
      },
      "destinations": {
        "eth": {
          "address": "0xEE586e7Eaad39207F0549BC65f19e336942C992f",
          "decimals": 18
        },
      },
    },
    "celo": {
      "symbol": "CELO",
      "name": "Celo (Wormhole)",
      "sourceAddress": "0x471EcE3750Da237f93B8E339c536989b8978a438",
      "coingeckoId": "celo",
      "logo": "https://assets.coingecko.com/coins/images/11090/small/InjXBNx9_400x400.jpg?1674707499",
      "markets": {
        "eth": ["uniswap"],
      },
      "destinations": {
        "eth": {
          "address": "0x3294395e62F4eB6aF3f1Fcf89f5602D90Fb3Ef69",
          "decimals": 18
        },
      },
    },
  },
  #################
  # 15. Near native
  #################
  "near": {
    "SWEAT": {
      "symbol": "SWEAT",
      "name": "Sweat Economy",
      "markets": {
        "eth": ["uniswap"],
        "near": ["reffinance"],
      },
      "sourceAddress": "token.sweat",
      "coingeckoId": "sweatcoin",
      "logo": "https://assets.coingecko.com/coins/images/25057/small/fhD9Xs16_400x400.jpg?1649947000",
      "destinations": {
        "eth": {
          "address": "0xB4b9DC1C77bdbb135eA907fd5a08094d98883A35",
          "decimals": 18
        },
        "bsc": {
          "address": "0x510Ad22d8C956dCC20f68932861f54A591001283",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    }
  },
  #################
  # 16. Moonbeam native
  #################
  "moonbeam": {
    "WELL": {
      "symbol": "WELL",
      "name": "Moonwell",
      "markets": {
        "base": ["balancer"],
      },
      "sourceAddress": "0x511ab53f793683763e5a8829738301368a2411e3",
      "coingeckoId": "moonwell",
      "logo": "https://assets.coingecko.com/coins/images/26133/small/WELL.png?1690178473",
      "destinations": {
        "base": {
          "address": "0xff8adec2221f9f4d8dfbafa6b9a297d17603493d",
          "decimals": 18
        }
      },
      "sourceDecimals": 18
    }
  },
  #################
  # 18. Terra2 native
  #################
  "terra2": {
  },
  #################
  # 19. Injective native
  #################
  "injective": {
  },
  #################
  # 22. Aptos native
  #################
  "aptos": {
  },
  #################
  # 23. Arbitrum native
  #################
  "arbitrum": {
    "TBTC": {
      "symbol": "TBTC",
      "name": "Threshold Bitcoin",
      "sourceAddress": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
      "coingeckoId": "tbtc",
      "logo": "https://assets.coingecko.com/coins/images/11224/small/0x18084fba666a33d37592fa2633fd49a74dd93a88.png?1674474504",
      "markets": {
        "eth": ['threshold'],
        "matic": ['threshold'],
        "optimism": ['threshold'],
        "base": ['threshold'],
        "sol": ['threshold']
      },
      "destinations": {
        "eth": {
          "address": "0x18084fbA666a33d37592fA2633fD49a74DD93a88",
          "decimals": 8
        },
        "matic": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "optimism": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "base": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "sol": {
            "address": "6DNSN2BJsaPFdFFc1zP37kkeNe4Usc1Sqkzr9C9vPWcU",
            "decimals": 8
        }
      },
      "sourceDecimals": 18
    }
  },
  #################
  # 24. Optimism native
  #################
  "optimism": {
    "TBTC": {
      "symbol": "TBTC",
      "name": "Threshold Bitcoin",
      "sourceAddress": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
      "coingeckoId": "tbtc",
      "logo": "https://assets.coingecko.com/coins/images/11224/small/0x18084fba666a33d37592fa2633fd49a74dd93a88.png?1674474504",
      "markets": {
        "eth": ['threshold'],
        "matic": ['threshold'],
        "arbitrum": ['threshold'],
        "base": ['threshold'],
        "sol": ['threshold']
      },
      "destinations": {
        "eth": {
          "address": "0x18084fbA666a33d37592fA2633fD49a74DD93a88",
          "decimals": 8
        },
        "matic": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "arbitrum": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "base": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "sol": {
            "address": "6DNSN2BJsaPFdFFc1zP37kkeNe4Usc1Sqkzr9C9vPWcU",
            "decimals": 8
        }
      },
      "sourceDecimals": 18
    }
  },
  #################
  # 28. XPLA native
  #################
  "xpla": {
  },
  #################
  # 30. Base native
  #################
  "base": {
    "TBTC": {
      "symbol": "TBTC",
      "name": "Threshold Bitcoin",
      "sourceAddress": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
      "coingeckoId": "tbtc",
      "logo": "https://assets.coingecko.com/coins/images/11224/small/0x18084fba666a33d37592fa2633fd49a74dd93a88.png?1674474504",
      "markets": {
        "eth": ['threshold'],
        "matic": ['threshold'],
        "arbitrum": ['threshold'],
        "sol": ['threshold']
      },
      "destinations": {
        "eth": {
          "address": "0x18084fbA666a33d37592fA2633fD49a74DD93a88",
          "decimals": 8
        },
        "matic": {
          "address": "0x236aa50979D5f3De3Bd1Eeb40E81137F22ab794b",
          "decimals": 8
        },
        "arbitrum": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "optimism": {
          "address": "0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40",
          "decimals": 8
        },
        "sol": {
            "address": "6DNSN2BJsaPFdFFc1zP37kkeNe4Usc1Sqkzr9C9vPWcU",
            "decimals": 8
        }
      },
      "sourceDecimals": 18
    }
  }
}
