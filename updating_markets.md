Updating `markets.json`
========================

> If you need to validate addresses between chains, use the [Token Origin Verifier](https://wormholebridge.com/#/token-origin-verifier)

In `markets.json` add an entry to the corresponding source chain, target chain, and address in `tokenMarkets`.

For example, if there were new Raydium and Tulip pools for (Ethereum) SHIB on Solana, I would go to:

```javascript
"tokenMarkets": { // <-- this key is already in the file
    "2": { // <-- source chain (may already be in the file)
        "1": { // <-- target chain (may already be in the file)
            "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE": { // <-- asset address on source chain, corresponds to a key in "tokens" -> "2" (the source chain}
                "markets": ["raydium", "tulip"] // <-- list of markets, corresponds to the keys in "markets"
            }
        }
    }
}
```

All addresses must have a corresponding entry in `tokens` and all markets must have a corresponding entry in `markets`. (The tests should ensure this.)

For this example, I might have to add:

```javascript
"markets": { // <-- this key is already in the file
    "raydium": {
      "name": "Raydium",
      "link": "https://raydium.io/swap/"
    }
}
```

and

```javascript
"tokens": { // <-- this key is already in the file
    "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE": {
        "symbol": "SHIB",
        "logo": "https://etherscan.io/token/images/shibatoken_32.png"
    }
}
```
