"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""

import pandas as pd
import os


dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


TOKENS = {
  "1INCH": {
    "symbol": "1INCH",
    "name": "1INCH Token (Wormhole)",
    "address": "AjkPkq3nsyDe1yKcbyZT7N4aK4Evv9om9tzhQD3wsRC",
    "origin": "ethereum",
    "sourceAddress": "0x111111111117dC0aa78b770fA6A738034120C302",
    "sourceContract": "https://etherscan.io/address/0x111111111117dC0aa78b770fA6A738034120C302",
    "coingeckoId": "1inch",
    "serumV3Usdc": "EQcNRGwogvYJDizG9Ek1qf6syi5UghkYDcUwgmycawYU",
    "serumV3Usdt": "B3UpqhaGZc9yXhELknAAXuAoKzCk4QAoqaiVUffgMQBH"
  },
  "AAVE": {
    "symbol": "AAVE",
    "name": "Aave Token (Wormhole)",
    "address": "3vAs4D1WE6Na4tCgt4BApgFfENbm8WY7q4cSPD1yM4Cg",
    "origin": "ethereum",
    "sourceAddress": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
    "sourceContract": "https://etherscan.io/address/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
    "coingeckoId": "aave",
    "serumV3Usdc": "8WZrmdpLckptiVKd2fPHPjewRVYQGQkjxi9vzRYG1sfs",
    "serumV3Usdt": "LghsMERQWQFK3zWMTrUkoyAJARQw2wSmcYZjexeN3zy"
  },
  "AKRO": {
    "symbol": "AKRO",
    "name": "Akropolis (Wormhole)",
    "address": "12uHjozDVgyGWeLqQ8DMCRbig8amW5VmvZu3FdMMdcaG",
    "origin": "ethereum",
    "sourceAddress": "0x8ab7404063ec4dbcfd4598215992dc3f8ec853d7",
    "sourceContract": "https://etherscan.io/address/0x8ab7404063ec4dbcfd4598215992dc3f8ec853d7",
    "coingeckoId": "akropolis",
    "serumV3Usdc": "G3h8NZgJozk9crme2me6sKDJuSQ12mNCtvC9NbSWqGuk",
    "serumV3Usdt": "DvbiPxKzuXZPcmUcYDqBz1tvUrXYPsNrRAjSeuwHtmEA"
  },
  "ALEPH": {
    "symbol": "ALEPH",
    "name": "Aleph.im (Wormhole)",
    "address": "3UCMiSnkcnkPE1pgQ5ggPCBv6dXgVUy16TmMUe1WpG9x",
    "origin": "ethereum",
    "sourceAddress": "0x27702a26126e0B3702af63Ee09aC4d1A084EF628",
    "sourceContract": "https://etherscan.io/address/0x27702a26126e0B3702af63Ee09aC4d1A084EF628",
    "coingeckoId": "aleph-im",
    "serumV3Usdc": "Fw4mvuE7KZmTjQPxP2sRpHwPDfRMWnKBupFZGyW9CAQH",
    "serumV3Usdt": "GZeHR8uCTVoHVDZFRVXTgm386DK1EKehy9yMS3BFChcL"
  },
  "ALICE": {
    "symbol": "ALICE",
    "name": "My Neighbor Alice (Wormhole)",
    "address": "9ARQsBfAn65q522cEqSJuse3cLhA31jgWDBGQHeiq7Mg",
    "origin": "ethereum",
    "sourceAddress": "0xac51066d7bec65dc4589368da368b212745d63e8",
    "sourceContract": "https://etherscan.io/address/0xac51066d7bec65dc4589368da368b212745d63e8",
    "coingeckoId": "my-neighbor-alice"
  },
  "AMP": {
    "symbol": "AMP",
    "name": "Amp (Wormhole)",
    "address": "D559HwgjYGDYsXpmFUKxhFTEwutvS9sya1kXiyCVogCV",
    "origin": "ethereum",
    "sourceAddress": "0xff20817765cb7f73d4bde2e66e067e58d11095c2",
    "sourceContract": "https://etherscan.io/address/0xff20817765cb7f73d4bde2e66e067e58d11095c2",
    "coingeckoId": "amp"
  },
  "AMPL": {
    "symbol": "AMPL",
    "name": "Ampleforth (Wormhole)",
    "address": "EHKQvJGu48ydKA4d3RivrkNyTJTkSdoS32UafxSX1yak",
    "origin": "ethereum",
    "sourceAddress": "0xd46ba6d942050d489dbd938a2c909a5d5039a161",
    "sourceContract": "https://etherscan.io/address/0xd46ba6d942050d489dbd938a2c909a5d5039a161",
    "coingeckoId": "ampleforth"
  },
  "AUDIO": {
    "symbol": "AUDIO",
    "name": "Audius (Wormhole)",
    "address": "9LzCMqDgTKYz9Drzqnpgee3SGa89up3a247ypMj2xrqM",
    "origin": "ethereum",
    "sourceAddress": "0x18aAA7115705e8be94bfFEBDE57Af9BFc265B998",
    "sourceContract": "https://etherscan.io/address/0x18aAA7115705e8be94bfFEBDE57Af9BFc265B998",
    "coingeckoId": "audius"
  },
  "AVAX": {
    "symbol": "AVAX",
    "name": "AVAX (Wormhole)",
    "address": "KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE",
    "origin": "avalanche",
    "sourceAddress": "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
    "sourceContract": "https://snowtrace.io/token/0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
    "coingeckoId": "avalanche",
    "serumV3Usdc": "E8JQstcwjuqN5kdMyUJLNuaectymnhffkvfg1j286UCr"
  },
  "AXSet": {
    "symbol": "AXSet",
    "name": "Axie Infinity Shard (Wormhole from Ethereum)",
    "address": "HysWcbHiYY9888pHbaqhwLYZQeZrcQMXKQWRqS7zcPK5",
    "origin": "ethereum",
    "sourceAddress": "0xbb0e17ef65f82ab018d8edd776e8dd940327b28b",
    "sourceContract": "https://etherscan.io/address/0xbb0e17ef65f82ab018d8edd776e8dd940327b28b",
    "coingeckoId": "axie-infinity"
  },
  "BAT": {
    "symbol": "BAT",
    "name": "Basic Attention Token (Wormhole)",
    "address": "EPeUFDgHRxs9xxEPVaL6kfGQvCon7jmAWKVUHuux1Tpz",
    "origin": "ethereum",
    "sourceAddress": "0x0D8775F648430679A709E98d2b0Cb6250d2887EF",
    "sourceContract": "https://etherscan.io/address/0x0D8775F648430679A709E98d2b0Cb6250d2887EF",
    "coingeckoId": "basic-attention-token"
  },
  "BNB": {
    "symbol": "BNB",
    "name": "Binance Coin (Wormhole)",
    "address": "9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa",
    "origin": "bsc",
    "sourceAddress": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
    "sourceContract": "https://bscscan.com/address/0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
    "coingeckoId": "binance-coin",
    "serumV3Usdc": "4UPUurKveNEJgBqJzqHPyi8DhedvpYsMXi7d43CjAg2f",
    "serumV3Usdt": "FjbKNZME5yVSC1R3HJM99kB3yir3q3frS5MteMFD72sV"
  },
  "BNT": {
    "symbol": "BNT",
    "name": "Bancor (Wormhole)",
    "address": "EDVVEYW4fPJ6vKw5LZXRGUSPzxoHrv6eWvTqhCr8oShs",
    "origin": "ethereum",
    "sourceAddress": "0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c",
    "sourceContract": "https://etherscan.io/address/0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c",
    "coingeckoId": "bancor-network"
  },
  "BUSDbs": {
    "symbol": "BUSDbs",
    "name": "BUSD Token (Wormhole from BSC)",
    "address": "5RpUwQ8wtdPCZHhu6MERp2RGrpobsbZ6MH5dDHkUjs2",
    "origin": "bsc",
    "sourceAddress": "0xe9e7cea3dedca5984780bafc599bd69add087d56",
    "sourceContract": "https://bscscan.com/address/0xe9e7cea3dedca5984780bafc599bd69add087d56",
    "coingeckoId": "binance-usd"
  },
  "BUSDet": {
    "symbol": "BUSDet",
    "name": "Binance USD (Wormhole from Ethereum)",
    "address": "33fsBLA8djQm82RpHmE3SuVrPGtZBWNYExsEUeKX1HXX",
    "origin": "ethereum",
    "sourceAddress": "0x4fabb145d64652a948d72533023f6e7a623c7c53",
    "sourceContract": "https://etherscan.io/address/0x4fabb145d64652a948d72533023f6e7a623c7c53",
    "coingeckoId": "binance-usd"
  },
  "CAKE": {
    "symbol": "CAKE",
    "name": "PancakeSwap Token (Wormhole)",
    "address": "J8LKx7pr9Zxh9nMhhT7X3EBmj5RzuhFrHKyJAe2F2i9S",
    "origin": "bsc",
    "sourceAddress": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
    "sourceContract": "https://bscscan.com/address/0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
    "coingeckoId": "pancakeswap"
  },
  "CEL": {
    "symbol": "CEL",
    "name": "Celsius (Wormhole)",
    "address": "nRtfwU9G82CSHhHGJNxFhtn7FLvWP2rqvQvje1WtL69",
    "origin": "ethereum",
    "sourceAddress": "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d",
    "sourceContract": "https://etherscan.io/address/0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d",
    "coingeckoId": "celsius-network-token",
    "serumV3Usdc": "79ESpYSb2hM14KTRXPZUwDkxUGC5irE2esd1vxdXfnZz",
    "serumV3Usdt": "J9ww1yufRNDDbUbDXmew2mW2ozkx7cme7dMvKjMQVHrL"
  },
  "CHZ": {
    "symbol": "CHZ",
    "name": "Chiliz (Wormhole)",
    "address": "5TtSKAamFq88grN1QGrEaZ1AjjyciqnCya1aiMhAgFvG",
    "origin": "ethereum",
    "sourceAddress": "0x3506424f91fd33084466f402d5d97f05f8e3b4af",
    "sourceContract": "https://etherscan.io/address/0x3506424f91fd33084466f402d5d97f05f8e3b4af",
    "coingeckoId": "chiliz"
  },
  "COMP": {
    "symbol": "COMP",
    "name": "Compound (Wormhole)",
    "address": "AwEauVaTMQRB71WeDnwf1DWSBxaMKjEPuxyLr1uixFom",
    "origin": "ethereum",
    "sourceAddress": "0xc00e94Cb662C3520282E6f5717214004A7f26888",
    "sourceContract": "https://etherscan.io/address/0xc00e94Cb662C3520282E6f5717214004A7f26888",
    "coingeckoId": "compound-governance-token",
    "serumV3Usdc": "CU5L8JC83hyYZdf1phzy6a7X58eTtPjs7mHL3QKCcLfh",
    "serumV3Usdt": "9gA6T3HRCMTVTULte5pJsXjMDUGRtygTKLbMny6eRcyM"
  },
  "CREAM": {
    "symbol": "CREAM",
    "name": "Cream (Wormhole)",
    "address": "HihxL2iM6L6P1oqoSeiixdJ3PhPYNxvSKH9A2dDqLVDH",
    "origin": "ethereum",
    "sourceAddress": "0x2ba592f78db6436527729929aaf6c908497cb200",
    "sourceContract": "https://etherscan.io/address/0x2ba592f78db6436527729929aaf6c908497cb200",
    "coingeckoId": "cream",
    "serumV3Usdc": "4pdQ2D4gehMhGu4z9jeQbEPUFbTxB5qcPr3zCynjJGyp",
    "serumV3Usdt": "6fspxMfBmYFTGFBDN5MU33A55i2MkGr7eSjBLPCAU6y9"
  },
  "CRO": {
    "symbol": "CRO",
    "name": "Crypto.com Coin (Wormhole)",
    "address": "DvjMYMVeXgKxaixGKpzQThLoG98nc7HSU7eanzsdCboA",
    "origin": "ethereum",
    "sourceAddress": "0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b",
    "sourceContract": "https://etherscan.io/address/0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b",
    "coingeckoId": "crypto-com-coin"
  },
  "CRV": {
    "symbol": "CRV",
    "name": "Curve DAO Token (Wormhole)",
    "address": "7gjNiPun3AzEazTZoFEjZgcBMeuaXdpjHq2raZTmTrfs",
    "origin": "ethereum",
    "sourceAddress": "0xd533a949740bb3306d119cc777fa900ba034cd52",
    "sourceContract": "https://etherscan.io/address/0xd533a949740bb3306d119cc777fa900ba034cd52",
    "coingeckoId": "curve-dao-token"
  },
  "CVX": {
    "symbol": "CVX",
    "name": "Convex Token (Wormhole)",
    "address": "BLvmrccP4g1B6SpiVvmQrLUDya1nZ4B2D1nm9jzKF7sz",
    "origin": "ethereum",
    "sourceAddress": "0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b",
    "sourceContract": "https://etherscan.io/address/0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b",
    "coingeckoId": "convex-finance"
  },
  "DAI": {
    "symbol": "DAI",
    "name": "Dai Stablecoin (Wormhole)",
    "address": "EjmyN6qEC1Tf1JxiG1ae7UTJhUxSwk1TCWNWqxWV4J6o",
    "origin": "ethereum",
    "sourceAddress": "0x6b175474e89094c44da98b954eedeac495271d0f",
    "sourceContract": "https://etherscan.io/address/0x6b175474e89094c44da98b954eedeac495271d0f",
    "coingeckoId": "dai"
  },
  "DAIpo": {
    "symbol": "DAIpo",
    "name": "Dai Stablecoin (Wormhole from Polygon)",
    "address": "4Fo67MYQpVhZj9R7jQTd63FPAnWbPpaafAUxsMGX2geP",
    "origin": "polygon",
    "sourceAddress": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
    "sourceContract": "https://polygonscan.com/token/0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
    "coingeckoId": "dai"
  },
  "DYDX": {
    "symbol": "DYDX",
    "name": "dYdX (Wormhole)",
    "address": "4Hx6Bj56eGyw8EJrrheM6LBQAvVYRikYCWsALeTrwyRU",
    "origin": "ethereum",
    "sourceAddress": "0x92d6c1e31e14520e676a687f0a93788b716beff5",
    "sourceContract": "https://etherscan.io/address/0x92d6c1e31e14520e676a687f0a93788b716beff5",
    "coingeckoId": "dydx"
  },
  "ELON": {
    "symbol": "ELON",
    "name": "Dogelon Mars (Wormhole)",
    "address": "6nKUU36URHkewHg5GGGAgxs6szkE4VTioGUT5txQqJFU",
    "origin": "ethereum",
    "sourceAddress": "0x761d38e5ddf6ccf6cf7c55759d5210750b5d60f3",
    "sourceContract": "https://etherscan.io/address/0x761d38e5ddf6ccf6cf7c55759d5210750b5d60f3",
    "coingeckoId": "dogelon-mars"
  },
  "ENJ": {
    "symbol": "ENJ",
    "name": "Enjin (Wormhole)",
    "address": "EXExWvT6VyYxEjFzF5BrUxt5GZMPVZnd48y3iWrRefMq",
    "origin": "ethereum",
    "sourceAddress": "0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c",
    "sourceContract": "https://etherscan.io/address/0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c",
    "coingeckoId": "enjin-coin"
  },
  "ETH": {
    "symbol": "ETH",
    "name": "Ether (Wormhole)",
    "address": "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs",
    "origin": "ethereum",
    "sourceAddress": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "sourceContract": "https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "coingeckoId": "ethereum",
    "serumV3Usdc": "8Gmi2HhZmwQPVdCwzS7CM66MGstMXPcTVHA7jF19cLZz",
    "serumV3Usdt": "ch7kmPrtoQUSEPBggcNAvLGiMQkJagVwd3gDYfd8m7Q"
  },
  "FRAX": {
    "symbol": "FRAX",
    "name": "Frax (Wormhole)",
    "address": "FR87nWEUxVgerFGhZM8Y4AggKGLnaXswr1Pd8wZ4kZcp",
    "origin": "ethereum",
    "sourceAddress": "0x853d955acef822db058eb8505911ed77f175b99e",
    "sourceContract": "https://etherscan.io/address/0x853d955acef822db058eb8505911ed77f175b99e",
    "coingeckoId": "frax"
  },
  "FRONT": {
    "symbol": "FRONT",
    "name": "Frontier Token (Wormhole)",
    "address": "A9ik2NrpKRRG2snyTjofZQcTuav9yH3mNVHLsLiDQmYt",
    "origin": "ethereum",
    "sourceAddress": "0xf8C3527CC04340b208C854E985240c02F7B7793f",
    "sourceContract": "https://etherscan.io/address/0xf8C3527CC04340b208C854E985240c02F7B7793f",
    "coingeckoId": "frontier",
    "serumV3Usdc": "B95oZN5HCLGmFAhbzReWBA9cuSGPFQAXeuhm2FfpdrML",
    "serumV3Usdt": "DZTYyy1L5Pr6DmTtYY5bEuU9g3LQ4XGvuYiN3zS25yG7"
  },
  "FTMet": {
    "symbol": "FTMet",
    "name": "Fantom Token (Wormhole from Ethereum)",
    "address": "8gC27rQF4NEDYfyf5aS8ZmQJUum5gufowKGYRRba4ENN",
    "origin": "ethereum",
    "sourceAddress": "0x4e15361fd6b4bb609fa63c81a2be19d873717870",
    "sourceContract": "https://etherscan.io/address/0x4e15361fd6b4bb609fa63c81a2be19d873717870",
    "coingeckoId": "fantom"
  },
  "FTT": {
    "symbol": "FTT",
    "name": "FTX Token (Wormhole)",
    "address": "EzfgjvkSwthhgHaceR3LnKXUoRkP6NUhfghdaHAj1tUv",
    "origin": "ethereum",
    "sourceAddress": "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9",
    "sourceContract": "https://etherscan.io/address/0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9",
    "coingeckoId": "ftx-token",
    "serumV3Usdc": "2wteg25ch227n4Rh1CN4WNrDZXBpRBpWJ48mEC2K7f4r",
    "serumV3Usdt": "BoHojHESAv4McZx9gXd1bWTZMq25JYyGz4qL1m5C3nvk"
  },
  "FXS": {
    "symbol": "FXS",
    "name": "Frax Share (Wormhole)",
    "address": "6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct",
    "origin": "ethereum",
    "sourceAddress": "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0",
    "sourceContract": "https://etherscan.io/address/0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0",
    "coingeckoId": "frax-share"
  },
  "GALA": {
    "symbol": "GALA",
    "name": "Gala (Wormhole)",
    "address": "AuGz22orMknxQHTVGwAu7e3dJikTJKgcjFwMNDikEKmF",
    "origin": "ethereum",
    "sourceAddress": "0x15d4c048f83bd7e37d49ea4c83a07267ec4203da",
    "sourceContract": "https://etherscan.io/address/0x15d4c048f83bd7e37d49ea4c83a07267ec4203da",
    "coingeckoId": "gala"
  },
  "GRT": {
    "symbol": "GRT",
    "name": "Graph Token (Wormhole)",
    "address": "HGsLG4PnZ28L8A4R5nPqKgZd86zUUdmfnkTRnuFJ5dAX",
    "origin": "ethereum",
    "sourceAddress": "0xc944E90C64B2c07662A292be6244BDf05Cda44a7",
    "sourceContract": "https://etherscan.io/address/0xc944E90C64B2c07662A292be6244BDf05Cda44a7",
    "coingeckoId": "the-graph",
    "serumV3Usdc": "4PD799gihM2SdM8g7PxfSWgQR8cWGNiuzmNzcL2RgpSu",
    "serumV3Usdt": "5bzmeSmiCzeyDQvaSsQhEega7e2jhH39cFCkT4eqSDSx"
  },
  "HBTC": {
    "symbol": "HBTC",
    "name": "Huobi BTC (Wormhole)",
    "address": "7dVH61ChzgmN9BwG4PkzwRP8PbYwPJ7ZPNF2vamKT2H8",
    "origin": "ethereum",
    "sourceAddress": "0x0316eb71485b0ab14103307bf65a021042c6d380",
    "sourceContract": "https://etherscan.io/address/0x0316eb71485b0ab14103307bf65a021042c6d380",
    "coingeckoId": "huobi-btc"
  },
  "HGET": {
    "symbol": "HGET",
    "name": "Hedget (Wormhole)",
    "address": "2ueY1bLcPHfuFzEJq7yN1V2Wrpu8nkun9xG2TVCE1mhD",
    "origin": "ethereum",
    "sourceAddress": "0x7968bc6a03017eA2de509AAA816F163Db0f35148",
    "sourceContract": "https://etherscan.io/address/0x7968bc6a03017eA2de509AAA816F163Db0f35148",
    "coingeckoId": "hedget",
    "serumV3Usdc": "27e1mB6UoPohbc3MmwMXu5QM7b2E3k5Mbhwv6JguwyXg",
    "serumV3Usdt": "BdRzTEKb7Qdu4tWts5zXjwcpQErZxEzvShKZ5QcthMag"
  },
  "HUSD": {
    "symbol": "HUSD",
    "name": "HUSD (Wormhole)",
    "address": "7VQo3HFLNH5QqGtM8eC3XQbPkJUu7nS9LeGWjerRh5Sw",
    "origin": "ethereum",
    "sourceAddress": "0xdf574c24545e5ffecb9a659c229253d4111d87e1",
    "sourceContract": "https://etherscan.io/address/0xdf574c24545e5ffecb9a659c229253d4111d87e1",
    "coingeckoId": "husd"
  },
  "HXRO": {
    "symbol": "HXRO",
    "name": "Hxro (Wormhole)",
    "address": "HxhWkVpk5NS4Ltg5nij2G671CKXFRKPK8vy271Ub4uEK",
    "origin": "ethereum",
    "sourceAddress": "0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3",
    "sourceContract": "https://etherscan.io/address/0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3",
    "coingeckoId": "hxro",
    "serumV3Usdc": "CBb5zXwNRB73WVjs2m21P5prcEZa6SWmej74Vzxh8dRm",
    "serumV3Usdt": "3BScwNxtMrEcQ5VTHyXHYQR98dTaxfyXGaLkuSjBY1dW"
  },
  "ICE": {
    "symbol": "ICE",
    "name": "IceToken (Wormhole)",
    "address": "DiJut4U3CU8b3bRgwfyqtJMJ4wjzJHaX6hudamjH46Km",
    "origin": "ethereum",
    "sourceAddress": "0xf16e81dce15b08f326220742020379b855b87df9",
    "sourceContract": "https://etherscan.io/address/0xf16e81dce15b08f326220742020379b855b87df9",
    "coingeckoId": "popsicle-finance"
  },
  "ILV": {
    "symbol": "ILV",
    "name": "Illuvium (Wormhole)",
    "address": "8UJbtpsEubDVkY53rk7d61hNYKkvouicczB2XmuwiG4g",
    "origin": "ethereum",
    "sourceAddress": "0x767fe9edc9e0df98e07454847909b5e959d7ca0e",
    "sourceContract": "https://etherscan.io/address/0x767fe9edc9e0df98e07454847909b5e959d7ca0e",
    "coingeckoId": "illuvium"
  },
  "JOE": {
    "symbol": "JOE",
    "name": "JoeToken (Wormhole)",
    "address": "CriXdFS9iRAYbGEQiTcUqbWwG9RBmYt5B6LwTnoJ61Sm",
    "origin": "avalanche",
    "sourceAddress": "0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd",
    "sourceContract": "https://snowtrace.io/address/0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd",
    "coingeckoId": "joe"
  },
  "KEEP": {
    "symbol": "KEEP",
    "name": "Keep Network (Wormhole)",
    "address": "64L6o4G2H7Ln1vN7AHZsUMW4pbFciHyuwn4wUdSbcFxh",
    "origin": "ethereum",
    "sourceAddress": "0x85eee30c52b0b379b046fb0f85f4f3dc3009afec",
    "sourceContract": "https://etherscan.io/address/0x85eee30c52b0b379b046fb0f85f4f3dc3009afec",
    "coingeckoId": "keep-network"
  },
  "KP3R": {
    "symbol": "KP3R",
    "name": "Keep3rV1 (Wormhole)",
    "address": "3a2VW9t5N6p4baMW3M6yLH1UJ9imMt7VsyUk6ouXPVLq",
    "origin": "ethereum",
    "sourceAddress": "0x1ceb5cb57c4d4e2b2433641b95dd330a33185a44",
    "sourceContract": "https://etherscan.io/address/0x1ceb5cb57c4d4e2b2433641b95dd330a33185a44",
    "coingeckoId": "keep3rv1"
  },
  "LINK": {
    "symbol": "LINK",
    "name": "ChainLink Token (Wormhole)",
    "address": "2wpTofQ8SkACrkZWrZDjXPitYa8AwWgX8AfxdeBRRVLX",
    "origin": "ethereum",
    "sourceAddress": "0x514910771af9ca656af840dff83e8264ecf986ca",
    "sourceContract": "https://etherscan.io/address/0x514910771af9ca656af840dff83e8264ecf986ca",
    "coingeckoId": "chainlink",
    "serumV3Usdc": "FJMjxMCiDKn16TLhXUdEbVDH5wC6k9EHYJTcrH6NcbDE",
    "serumV3Usdt": "Gr2KmhK7Upr4uW56B1QQrJuhhgmot6zAHJeZALTMStiX"
  },
  "LRC": {
    "symbol": "LRC",
    "name": "LoopringCoin V2 (Wormhole)",
    "address": "HCTVFTzHL21a1dPzKxAUeWwqbE8QMUyvgChFDL4XYoi1",
    "origin": "ethereum",
    "sourceAddress": "0xbbbbca6a901c926f240b89eacb641d8aec7aeafd",
    "sourceContract": "https://etherscan.io/address/0xbbbbca6a901c926f240b89eacb641d8aec7aeafd",
    "coingeckoId": "loopring"
  },
  "LUA": {
    "symbol": "LUA",
    "name": "LuaToken (Wormhole)",
    "address": "5Wc4U1ZoQRzF4tPdqKQzBwRSjYe8vEf3EvZMuXgtKUW6",
    "origin": "ethereum",
    "sourceAddress": "0xb1f66997a5760428d3a87d68b90bfe0ae64121cc",
    "sourceContract": "https://etherscan.io/address/0xb1f66997a5760428d3a87d68b90bfe0ae64121cc",
    "coingeckoId": "luaswap",
    "serumV3Usdc": "J9imTcEeahZqKuaoQaPcCeSGCMWL8qSACpK4B7bC8NN4",
    "serumV3Usdt": "BMJ3CvQZ57cNnuc3Lz5Pb6cW6Sr9kZGz3qz2bJQTE24A"
  },
  "LUNA": {
    "symbol": "LUNA",
    "name": "LUNA (Wormhole)",
    "address": "F6v4wfAdJB8D8p77bMXZgYt8TDKsYxLYxH5AFhUkYx9W",
    "origin": "terra",
    "sourceAddress": "uluna",
    "coingeckoId": "terra-luna",
    "serumV3Usdc": "HBTu8hNaoT3VyiSSzJYa8jwt9sDGKtJviSwFa11iXdmE"
  },
  "MANA": {
    "symbol": "MANA",
    "name": "Decentraland (Wormhole)",
    "address": "7dgHoN8wBZCc5wbnQ2C47TDnBMAxG4Q5L3KjP67z8kNi",
    "origin": "ethereum",
    "sourceAddress": "0x0f5d2fb29fb7d3cfee444a200298f468908cc942",
    "sourceContract": "https://etherscan.io/address/0x0f5d2fb29fb7d3cfee444a200298f468908cc942",
    "coingeckoId": "decentraland"
  },
  "MATH": {
    "symbol": "MATH",
    "name": "MATH Token (Wormhole)",
    "address": "CaGa7pddFXS65Gznqwp42kBhkJQdceoFVT7AQYo8Jr8Q",
    "origin": "ethereum",
    "sourceAddress": "0x08d967bb0134f2d07f7cfb6e246680c53927dd30",
    "sourceContract": "https://etherscan.io/address/0x08d967bb0134f2d07f7cfb6e246680c53927dd30",
    "coingeckoId": "math",
    "serumV3Usdc": "G8L1YLrktaG1t8YBMJs3CwV96nExvJJCSpw3DARPDjE2",
    "serumV3Usdt": "CkvNfATB7nky8zPLuwS9bgcFbVRkQdkd5zuKEovyo9rs"
  },
  "MATICet": {
    "symbol": "MATICet",
    "name": "Matic (Wormhole from Ethereum)",
    "address": "C7NNPWuZCNjZBfW5p6JvGsR8pUdsRpEdP1ZAhnoDwj7h",
    "origin": "ethereum",
    "sourceAddress": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",
    "sourceContract": "https://etherscan.io/address/0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",
    "coingeckoId": "polygon"
  },
  "MATICpo": {
    "symbol": "MATICpo",
    "name": "Matic (Wormhole from Polygon)",
    "address": "Gz7VkD4MacbEB6yC5XD3HcumEiYx2EtDYYrfikGsvopG",
    "origin": "polygon",
    "sourceAddress": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
    "sourceContract": "https://polygonscan.com/address/0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
    "coingeckoId": "polygon",
    "serumV3Usdc": "5WRoQxE59966N2XfD2wYy1uhuyKeoVJ9NBMH6r6RNYEF"
  },
  "MIMet": {
    "symbol": "MIMet",
    "name": "Magic Internet Money (Wormhole from Ethereum)",
    "address": "HRQke5DKdDo3jV7wnomyiM8AA3EzkVnxMDdo2FQ5XUe1",
    "origin": "ethereum",
    "sourceAddress": "0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3",
    "sourceContract": "https://etherscan.io/address/0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3",
    "coingeckoId": "magic-internet-money"
  },
  "NXM": {
    "symbol": "NXM",
    "name": "Nexus Mutual (Wormhole)",
    "address": "Aqs5ydqKXEK2cjotDXxHmk8N9PknqQ5q4ZED4ymY1eeh",
    "origin": "ethereum",
    "sourceAddress": "0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b",
    "sourceContract": "https://etherscan.io/address/0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b",
    "coingeckoId": "nexus-mutual"
  },
  "OHM": {
    "symbol": "OHM",
    "name": "Olympus (Wormhole)",
    "address": "Afe9gSG8NcWicJtC58tUPGWG6pUcdK29d59BJuSAsePJ",
    "origin": "ethereum",
    "sourceAddress": "0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5",
    "sourceContract": "https://etherscan.io/address/0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5",
    "coingeckoId": "olympus"
  },
  "PAXG": {
    "symbol": "PAXG",
    "name": "Paxos Gold (Wormhole)",
    "address": "C6oFsE8nXRDThzrMEQ5SxaNFGKoyyfWDDVPw37JKvPTe",
    "origin": "ethereum",
    "sourceAddress": "0x45804880de22913dafe09f4980848ece6ecbaf78",
    "sourceContract": "https://etherscan.io/address/0x45804880de22913dafe09f4980848ece6ecbaf78",
    "coingeckoId": "pax-gold",
    "serumV3Usdc": "BeyB6W2iNsH9qSfb7icLTmSPDu8oUGkarMZed4Unrnsr",
    "serumV3Usdt": "9SQcpBFAs6ZiLAGUC9azYCN1kv89uTRmFR83sX1FTeh4"
  },
  "PERP": {
    "symbol": "PERP",
    "name": "Perpetual (Wormhole)",
    "address": "9BsnSWDPfbusseZfnXyZ3un14CyPMZYvsKjWY3Y8Gbqn",
    "origin": "ethereum",
    "sourceAddress": "0xbC396689893D065F41bc2C6EcbeE5e0085233447",
    "sourceContract": "https://etherscan.io/address/0xbC396689893D065F41bc2C6EcbeE5e0085233447",
    "coingeckoId": "perpetual-protocol",
    "serumV3Usdc": "Ao8HgYFCT2BJHxSusZbpJCPhvFMFXZApqN2uy2trbQRa",
    "serumV3Usdt": "5EoZqJZrmKmq1yeRkYAerbJhcs92DZbCtW86EhPYCio2"
  },
  "QUICK": {
    "symbol": "QUICK",
    "name": "Quickswap (Wormhole)",
    "address": "5njTmK53Ss5jkiHHZvzabVzZj6ztu6WYWpAPYgbVnbjs",
    "origin": "polygon",
    "sourceAddress": "0x831753dd7087cac61ab5644b308642cc1c33dc13",
    "sourceContract": "https://polygonscan.com/address/0x831753dd7087cac61ab5644b308642cc1c33dc13",
    "coingeckoId": "quickswap"
  },
  "RGT": {
    "symbol": "RGT",
    "name": "Rari Governance Token (Wormhole)",
    "address": "ASk8bss7PoxfFVJfXnSJepj9KupTX15QaRnhdjs6DdYe",
    "origin": "ethereum",
    "sourceAddress": "0xd291e7a03283640fdc51b121ac401383a46cc623",
    "sourceContract": "https://etherscan.io/address/0xd291e7a03283640fdc51b121ac401383a46cc623",
    "coingeckoId": "rari-governance-token"
  },
  "RPL": {
    "symbol": "RPL",
    "name": "Rocket Pool (Wormhole)",
    "address": "HUCyuyqESEUV4YWTKFvvB4JiQLqoovscTBpRXfGzW4Wx",
    "origin": "ethereum",
    "sourceAddress": "0xd33526068d116ce69f19a9ee46f0bd304f21a51f",
    "sourceContract": "https://etherscan.io/address/0xd33526068d116ce69f19a9ee46f0bd304f21a51f",
    "coingeckoId": "rocket-pool"
  },
  "RSR": {
    "symbol": "RSR",
    "name": "Reserve Rights (Wormhole)",
    "address": "DkbE8U4gSRuGHcVMA1LwyZPYUjYbfEbjW8DMR3iSXBzr",
    "origin": "ethereum",
    "sourceAddress": "0x8762db106B2c2A0bccB3A80d1Ed41273552616E8",
    "sourceContract": "https://etherscan.io/address/0x8762db106B2c2A0bccB3A80d1Ed41273552616E8",
    "coingeckoId": "reserve-rights-token",
    "serumV3Usdc": "GqgkxEswUwHBntmzb5GpUhKrVpJhzreSruZycuJwdNwB",
    "serumV3Usdt": "2j2or38X2FUbpkK4gkgvjDtqN3ibkKw3v5yn7o2gHqPc"
  },
  "SHIB": {
    "symbol": "SHIB",
    "name": "SHIBA INU (Wormhole)",
    "address": "CiKu4eHsVrc1eueVQeHn7qhXTcVu95gSQmBpX4utjL9z",
    "origin": "ethereum",
    "sourceAddress": "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce",
    "sourceContract": "https://etherscan.io/address/0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce",
    "coingeckoId": "shiba-inu"
  },
  "SLP": {
    "symbol": "SLP",
    "name": "Smooth Love Potion (Wormhole)",
    "address": "4hpngEp1v3CXpeKB81Gw4sv7YvwUVRKvY3SGag9ND8Q4",
    "origin": "ethereum",
    "sourceAddress": "0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25",
    "sourceContract": "https://etherscan.io/address/0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25",
    "coingeckoId": "smooth-love-potion"
  },
  "SNX": {
    "symbol": "SNX",
    "name": "Synthetix Network Token (Wormhole)",
    "address": "8cTNUtcV2ueC3royJ642uRnvTxorJAWLZc58gxAo7y56",
    "origin": "ethereum",
    "sourceAddress": "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f",
    "sourceContract": "https://etherscan.io/address/0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f",
    "coingeckoId": "synthetix-network-token"
  },
  "SPELL": {
    "symbol": "SPELL",
    "name": "Spell Token (Wormhole)",
    "address": "BCsFXYm81iqXyYmrLKgAp3AePcgLHnirb8FjTs6sjM7U",
    "origin": "ethereum",
    "sourceAddress": "0x090185f2135308bad17527004364ebcc2d37e5f6",
    "sourceContract": "https://etherscan.io/address/0x090185f2135308bad17527004364ebcc2d37e5f6",
    "coingeckoId": "spell-token"
  },
  "SRMet": {
    "symbol": "SRMet",
    "name": "Serum (Wormhole from Ethereum)",
    "address": "xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG",
    "origin": "ethereum",
    "sourceAddress": "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff",
    "sourceContract": "https://etherscan.io/address/0x476c5e26a75bd202a9683ffd34359c0cc15be0ff",
    "coingeckoId": "serum"
  },
  "SUSHI": {
    "symbol": "SUSHI",
    "name": "SushiToken (Wormhole)",
    "address": "ChVzxWRmrTeSgwd3Ui3UumcN8KX7VK3WaD4KGeSKpypj",
    "origin": "ethereum",
    "sourceAddress": "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2",
    "sourceContract": "https://etherscan.io/address/0x6b3595068778dd592e39a122f4f5a5cf09c90fe2",
    "coingeckoId": "sushi",
    "serumV3Usdc": "3uWVMWu7cwMnYMAAdtsZNwaaqeeeZHARGZwcExnQiFay",
    "serumV3Usdt": "T3aC6qcPAJtX1gqkckfSxBPdPWziz5fLYRt5Dz3Nafq"
  },
  "SWAG": {
    "symbol": "SWAG",
    "name": "Swag Token (Wormhole)",
    "address": "5hcdG6NjQwiNhVa9bcyaaDsCyA1muPQ6WRzQwHfgeeKo",
    "origin": "ethereum",
    "sourceAddress": "0x87eDfFDe3E14c7a66c9b9724747a1C5696b742e6",
    "sourceContract": "https://etherscan.io/address/0x87eDfFDe3E14c7a66c9b9724747a1C5696b742e6",
    "coingeckoId": "swag-finance",
    "serumV3Usdc": "wSkeLMv3ktJyLm51bvQWxY2saGKqGxbnUFimPxbgEvQ",
    "serumV3Usdt": "6URQ4zFWvPm1fhJCKKWorrh8X3mmTFiDDyXEUmSf8Rb2"
  },
  "SXP": {
    "symbol": "SXP",
    "name": "Swipe (Wormhole)",
    "address": "3CyiEDRehaGufzkpXJitCP5tvh7cNhRqd9rPBxZrgK5z",
    "origin": "ethereum",
    "sourceAddress": "0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9",
    "sourceContract": "https://etherscan.io/address/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9",
    "coingeckoId": "swipe",
    "serumV3Usdc": "G5F84rfqmWqzZv5GBpSn8mMwW8zJ2B4Y1GpGupiwjHNM",
    "serumV3Usdt": "2FQbPW1ticJz2SMMbEXxbKWJKmw1wLc6ggSP2HyzdMen"
  },
  "TOKE": {
    "symbol": "TOKE",
    "name": "Tokemak (Wormhole)",
    "address": "3EQ6LqLkiFcoxTeGEsHMFpSLWNVPe9yT7XPX2HYSFyxX",
    "origin": "ethereum",
    "sourceAddress": "0x2e9d63788249371f1dfc918a52f8d799f4a38c94",
    "sourceContract": "https://etherscan.io/address/0x2e9d63788249371f1dfc918a52f8d799f4a38c94",
    "coingeckoId": "tokemak"
  },
  "TRIBE": {
    "symbol": "TRIBE",
    "name": "Tribe (Wormhole)",
    "address": "DPgNKZJAG2w1S6vfYHDBT62R4qrWWH5f45CnxtbQduZE",
    "origin": "ethereum",
    "sourceAddress": "0xc7283b66eb1eb5fb86327f08e1b5816b0720212b",
    "sourceContract": "https://etherscan.io/address/0xc7283b66eb1eb5fb86327f08e1b5816b0720212b",
    "coingeckoId": "tribe"
  },
  "UBXT": {
    "symbol": "UBXT",
    "name": "UpBots (Wormhole)",
    "address": "FTtXEUosNn6EKG2SQtfbGuYB4rBttreQQcoWn1YDsuTq",
    "origin": "ethereum",
    "sourceAddress": "0x8564653879a18C560E7C0Ea0E084c516C62F5653",
    "sourceContract": "https://etherscan.io/address/0x8564653879a18C560E7C0Ea0E084c516C62F5653",
    "coingeckoId": "upbots",
    "serumV3Usdc": "Hh4p7tJpqkGW6xsHM2LiPPMpJg43fwn5TbmVmfrURdLY",
    "serumV3Usdt": "5xhjc3ZtAwnBK3qsaro28VChL7WrxY9N4SG6UZpYxpGc"
  },
  "UFO": {
    "symbol": "UFO",
    "name": "UFO Gaming (Wormhole)",
    "address": "GWdkYFnXnSJAsCBvmsqFLiPPe2tpvXynZcJdxf11Fu3U",
    "origin": "ethereum",
    "sourceAddress": "0x249e38ea4102d0cf8264d3701f1a0e39c4f2dc3b",
    "sourceContract": "https://etherscan.io/address/0x249e38ea4102d0cf8264d3701f1a0e39c4f2dc3b",
    "coingeckoId": "ufo-gaming"
  },
  "UNI": {
    "symbol": "UNI",
    "name": "Uniswap (Wormhole)",
    "address": "8FU95xFJhUUkyyCLU13HSzDLs7oC4QZdXQHL6SCeab36",
    "origin": "ethereum",
    "sourceAddress": "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
    "sourceContract": "https://etherscan.io/address/0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
    "coingeckoId": "uniswap",
    "serumV3Usdc": "B7b5rjQuqQCuGqmUBWmcCTqaL3Z1462mo4NArqty6QFR",
    "serumV3Usdt": "FrKM6kJtAjXknHPEpkrQtJSXZwUxV5dq26wDpc4YjQST"
  },
  "USDCbs": {
    "symbol": "USDCbs",
    "name": "USD Coin (Wormhole from BSC)",
    "address": "FCqfQSujuPxy6V42UvafBhsysWtEq1vhjfMN1PUbgaxA",
    "origin": "bsc",
    "sourceAddress": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
    "sourceContract": "https://bscscan.com/address/0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
    "coingeckoId": "usd-coin"
  },
  "USDCet": {
    "symbol": "USDCet",
    "name": "USD Coin (Wormhole from Ethereum)",
    "address": "A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM",
    "origin": "ethereum",
    "sourceAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "sourceContract": "https://etherscan.io/address/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "coingeckoId": "usd-coin"
  },
  "USDCpo": {
    "symbol": "USDCpo",
    "name": "USD Coin (Wormhole from Polygon)",
    "address": "E2VmbootbVCBkMNNxKQgCLMS1X3NoGMaYAsufaAsf7M",
    "origin": "polygon",
    "sourceAddress": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "sourceContract": "https://polygonscan.com/token/0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "coingeckoId": "usd-coin"
  },
  "USDK": {
    "symbol": "USDK",
    "name": "USDK (Wormhole)",
    "address": "43m2ewFV5nDepieFjT9EmAQnc1HRtAF247RBpLGFem5F",
    "origin": "ethereum",
    "sourceAddress": "0x1c48f86ae57291f7686349f12601910bd8d470bb",
    "sourceContract": "https://etherscan.io/address/0x1c48f86ae57291f7686349f12601910bd8d470bb",
    "coingeckoId": "usdk"
  },
  "USDTbs": {
    "symbol": "USDTbs",
    "name": "Tether USD (Wormhole from BSC)",
    "address": "8qJSyQprMC57TWKaYEmetUR3UUiTP2M3hXdcvFhkZdmv",
    "origin": "bsc",
    "sourceAddress": "0x55d398326f99059ff775485246999027b3197955",
    "sourceContract": "https://bscscan.com/address/0x55d398326f99059ff775485246999027b3197955",
    "coingeckoId": "tether"
  },
  "USDTet": {
    "symbol": "USDTet",
    "name": "Tether USD (Wormhole from Ethereum)",
    "address": "Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1",
    "origin": "ethereum",
    "sourceAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "sourceContract": "https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7",
    "coingeckoId": "tether"
  },
  "USDTpo": {
    "symbol": "USDTpo",
    "name": "Tether USD (Wormhole from Polygon)",
    "address": "5goWRao6a3yNC4d6UjMdQxonkCMvKBwdpubU3qhfcdf1",
    "origin": "polygon",
    "sourceAddress": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
    "sourceContract": "https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
    "coingeckoId": "tether"
  },
  "UST": {
    "symbol": "UST",
    "name": "UST (Wormhole)",
    "address": "9vMJfxuKxXBoEa7rM12mYLMwTacLMLDJqHozw96WQL8i",
    "origin": "terra",
    "sourceAddress": "uusd",
    "coingeckoId": "terra-usd"
  },
  "WBTC": {
    "symbol": "WBTC",
    "name": "Wrapped BTC (Wormhole)",
    "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
    "origin": "ethereum",
    "sourceAddress": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "sourceContract": "https://etherscan.io/address/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "coingeckoId": "wrapped-bitcoin"
  },
  "YFI": {
    "symbol": "YFI",
    "name": "yearn.finance (Wormhole)",
    "address": "BXZX2JRJFjvKazM1ibeDFxgAngKExb74MRXzXKvgikxX",
    "origin": "ethereum",
    "sourceAddress": "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e",
    "sourceContract": "https://etherscan.io/address/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e",
    "coingeckoId": "yearn-finance",
    "serumV3Usdc": "BiJXGFc1c4gyPpv9HLRJoKbZewWQrTCHGuxYKjYMQJpC",
    "serumV3Usdt": "9sue9TZAeUhNtNAPPGb9dke7rkJeXktGD3u8ZC37GWnQ"
  },
  "YGG": {
    "symbol": "YGG",
    "name": "Yield Guild Games Token (Wormhole)",
    "address": "EzZp7LRN1xwu3QsB2RJRrWwEGjJGsuWzuMCeQDB3NSPK",
    "origin": "ethereum",
    "sourceAddress": "0x25f8087ead173b73d6e8b84329989a8eea16cf73",
    "sourceContract": "https://etherscan.io/address/0x25f8087ead173b73d6e8b84329989a8eea16cf73",
    "coingeckoId": "yield-guild-games"
  },
  "ZRX": {
    "symbol": "ZRX",
    "name": "ZRX (Wormhole)",
    "address": "GJa1VeEYLTRoHbaeqcxfzHmjGCGtZGF3CUqxv9znZZAY",
    "origin": "ethereum",
    "sourceAddress": "0xe41d2489571d322189246dafa5ebde1f4699f498",
    "sourceContract": "https://etherscan.io/address/0xe41d2489571d322189246dafa5ebde1f4699f498",
    "coingeckoId": "0x"
  }
}


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
