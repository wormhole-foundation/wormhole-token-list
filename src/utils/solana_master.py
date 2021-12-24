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
    "coingeckoId": "1inch",
    "serumV3Usdc": "EQcNRGwogvYJDizG9Ek1qf6syi5UghkYDcUwgmycawYU",
    "sourceAddress": "0x111111111117dC0aa78b770fA6A738034120C302",
    "sourceContract": "https://etherscan.io/address/0x111111111117dC0aa78b770fA6A738034120C302"
  },
  "AAVE": {
    "symbol": "AAVE",
    "name": "Aave Token (Wormhole)",
    "address": "3vAs4D1WE6Na4tCgt4BApgFfENbm8WY7q4cSPD1yM4Cg",
    "origin": "ethereum",
    "coingeckoId": "aave",
    "serumV3Usdc": "8WZrmdpLckptiVKd2fPHPjewRVYQGQkjxi9vzRYG1sfs",
    "sourceAddress": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
    "sourceContract": "https://etherscan.io/address/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
  },
  "AKRO": {
    "symbol": "AKRO",
    "name": "Akropolis (Wormhole)",
    "address": "12uHjozDVgyGWeLqQ8DMCRbig8amW5VmvZu3FdMMdcaG",
    "origin": "ethereum",
    "coingeckoId": "akropolis",
    "serumV3Usdc": "G3h8NZgJozk9crme2me6sKDJuSQ12mNCtvC9NbSWqGuk",
    "sourceAddress": "0x8ab7404063ec4dbcfd4598215992dc3f8ec853d7",
    "sourceContract": "https://etherscan.io/address/0x8ab7404063ec4dbcfd4598215992dc3f8ec853d7"
  },
  "ALEPH": {
    "symbol": "ALEPH",
    "name": "Aleph.im (Wormhole)",
    "address": "3UCMiSnkcnkPE1pgQ5ggPCBv6dXgVUy16TmMUe1WpG9x",
    "origin": "ethereum",
    "coingeckoId": "aleph-im",
    "serumV3Usdc": "Fw4mvuE7KZmTjQPxP2sRpHwPDfRMWnKBupFZGyW9CAQH",
    "sourceAddress": "0x27702a26126e0B3702af63Ee09aC4d1A084EF628",
    "sourceContract": "https://etherscan.io/address/0x27702a26126e0B3702af63Ee09aC4d1A084EF628"
  },
  "AUDIO": {
    "symbol": "AUDIO",
    "name": "Audius (Wormhole)",
    "address": "9LzCMqDgTKYz9Drzqnpgee3SGa89up3a247ypMj2xrqM",
    "origin": "ethereum",
    "coingeckoId": "audius",
    "sourceAddress": "0x18aAA7115705e8be94bfFEBDE57Af9BFc265B998",
    "sourceContract": "https://etherscan.io/address/0x18aAA7115705e8be94bfFEBDE57Af9BFc265B998"
  },
  "AVAX": {
    "symbol": "AVAX",
    "name": "AVAX (Wormhole)",
    "address": "KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE",
    "origin": "avalanche",
    "coingeckoId": "avalanche",
    "serumV3Usdc": "E8JQstcwjuqN5kdMyUJLNuaectymnhffkvfg1j286UCr",
    "sourceAddress": "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
    "sourceContract": "https://snowtrace.io/token/0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7"
  },
  "BAT": {
    "symbol": "BAT",
    "name": "Basic Attention Token (Wormhole)",
    "address": "EPeUFDgHRxs9xxEPVaL6kfGQvCon7jmAWKVUHuux1Tpz",
    "origin": "ethereum",
    "coingeckoId": "basic-attention-token",
    "sourceAddress": "0x0D8775F648430679A709E98d2b0Cb6250d2887EF",
    "sourceContract": "https://etherscan.io/address/0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
  },
  "BNB": {
    "symbol": "BNB",
    "name": "Binance Coin (Wormhole)",
    "address": "9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa",
    "origin": "bsc",
    "coingeckoId": "binance-coin",
    "serumV3Usdc": "4UPUurKveNEJgBqJzqHPyi8DhedvpYsMXi7d43CjAg2f",
    "sourceAddress": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
    "sourceContract": "https://bscscan.com/address/0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
  },
  "BUSDbs": {
    "symbol": "BUSDbs",
    "name": "BUSD Token (Wormhole from BSC)",
    "address": "5RpUwQ8wtdPCZHhu6MERp2RGrpobsbZ6MH5dDHkUjs2",
    "origin": "bsc",
    "coingeckoId": "binance-usd",
    "sourceAddress": "0xe9e7cea3dedca5984780bafc599bd69add087d56",
    "sourceContract": "https://bscscan.com/address/0xe9e7cea3dedca5984780bafc599bd69add087d56"
  },
  "BUSDet": {
    "symbol": "BUSDet",
    "name": "Binance USD (Wormhole from Ethereum)",
    "address": "33fsBLA8djQm82RpHmE3SuVrPGtZBWNYExsEUeKX1HXX",
    "origin": "ethereum",
    "coingeckoId": "binance-usd",
    "sourceAddress": "0x4fabb145d64652a948d72533023f6e7a623c7c53",
    "sourceContract": "https://etherscan.io/address/0x4fabb145d64652a948d72533023f6e7a623c7c53"
  },
  "CAKE": {
    "symbol": "CAKE",
    "name": "PancakeSwap Token (Wormhole)",
    "address": "J8LKx7pr9Zxh9nMhhT7X3EBmj5RzuhFrHKyJAe2F2i9S",
    "origin": "bsc",
    "coingeckoId": "pancakeswap",
    "sourceAddress": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
    "sourceContract": "https://bscscan.com/address/0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"
  },
  "CEL": {
    "symbol": "CEL",
    "name": "Celsius (Wormhole)",
    "address": "nRtfwU9G82CSHhHGJNxFhtn7FLvWP2rqvQvje1WtL69",
    "origin": "ethereum",
    "coingeckoId": "celsius-network-token",
    "serumV3Usdc": "79ESpYSb2hM14KTRXPZUwDkxUGC5irE2esd1vxdXfnZz",
    "sourceAddress": "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d",
    "sourceContract": "https://etherscan.io/address/0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d"
  },
  "COMP": {
    "symbol": "COMP",
    "name": "Compound (Wormhole)",
    "address": "CU5L8JC83hyYZdf1phzy6a7X58eTtPjs7mHL3QKCcLfh",
    "origin": "ethereum",
    "coingeckoId": "compound-governance-token",
    "serumV3Usdc": "CU5L8JC83hyYZdf1phzy6a7X58eTtPjs7mHL3QKCcLfh",
    "sourceAddress": "0xc00e94Cb662C3520282E6f5717214004A7f26888",
    "sourceContract": "https://etherscan.io/address/0xc00e94Cb662C3520282E6f5717214004A7f26888"
  },
  "CREAM": {
    "symbol": "CREAM",
    "name": "Cream (Wormhole)",
    "address": "HihxL2iM6L6P1oqoSeiixdJ3PhPYNxvSKH9A2dDqLVDH",
    "origin": "ethereum",
    "coingeckoId": "cream",
    "serumV3Usdc": "4pdQ2D4gehMhGu4z9jeQbEPUFbTxB5qcPr3zCynjJGyp",
    "sourceAddress": "0x2ba592f78db6436527729929aaf6c908497cb200",
    "sourceContract": "https://etherscan.io/address/0x2ba592f78db6436527729929aaf6c908497cb200"
  },
  "DAI": {
    "symbol": "DAI",
    "name": "Dai Stablecoin (Wormhole)",
    "address": "EjmyN6qEC1Tf1JxiG1ae7UTJhUxSwk1TCWNWqxWV4J6o",
    "origin": "ethereum",
    "coingeckoId": "dai",
    "sourceAddress": "0x6b175474e89094c44da98b954eedeac495271d0f",
    "sourceContract": "https://etherscan.io/address/0x6b175474e89094c44da98b954eedeac495271d0f"
  },
  "DAIpo": {
    "symbol": "DAIpo",
    "name": "Dai Stablecoin (Wormhole from Polygon)",
    "address": "4Fo67MYQpVhZj9R7jQTd63FPAnWbPpaafAUxsMGX2geP",
    "origin": "polygon",
    "coingeckoId": "dai",
    "sourceAddress": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
    "sourceContract": "https://polygonscan.com/token/0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"
  },
  "ETH": {
    "symbol": "ETH",
    "name": "Ether (Wormhole)",
    "address": "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs",
    "origin": "ethereum",
    "coingeckoId": "ethereum",
    "serumV3Usdc": "8Gmi2HhZmwQPVdCwzS7CM66MGstMXPcTVHA7jF19cLZz",
    "sourceAddress": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "sourceContract": "https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
  },
  "FRAX": {
    "symbol": "FRAX",
    "name": "Frax (Wormhole)",
    "address": "FR87nWEUxVgerFGhZM8Y4AggKGLnaXswr1Pd8wZ4kZcp",
    "origin": "ethereum",
    "coingeckoId": "frax",
    "sourceAddress": "0x853d955acef822db058eb8505911ed77f175b99e",
    "sourceContract": "https://etherscan.io/address/0x853d955acef822db058eb8505911ed77f175b99e"
  },
  "FRONT": {
    "symbol": "FRONT",
    "name": "Frontier Token (Wormhole)",
    "address": "A9ik2NrpKRRG2snyTjofZQcTuav9yH3mNVHLsLiDQmYt",
    "origin": "ethereum",
    "coingeckoId": "frontier",
    "serumV3Usdc": "B95oZN5HCLGmFAhbzReWBA9cuSGPFQAXeuhm2FfpdrML",
    "sourceAddress": "0xf8C3527CC04340b208C854E985240c02F7B7793f",
    "sourceContract": "https://etherscan.io/address/0xf8C3527CC04340b208C854E985240c02F7B7793f"
  },
  "FTT": {
    "symbol": "FTT",
    "name": "FTX Token (Wormhole)",
    "address": "EzfgjvkSwthhgHaceR3LnKXUoRkP6NUhfghdaHAj1tUv",
    "origin": "ethereum",
    "coingeckoId": "ftx-token",
    "serumV3Usdc": "2wteg25ch227n4Rh1CN4WNrDZXBpRBpWJ48mEC2K7f4r",
    "sourceAddress": "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9",
    "sourceContract": "https://etherscan.io/address/0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9"
  },
  "FXS": {
    "symbol": "FXS",
    "name": "Frax Share (Wormhole)",
    "address": "6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct",
    "origin": "ethereum",
    "coingeckoId": "frax-share",
    "sourceAddress": "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0",
    "sourceContract": "https://etherscan.io/address/0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0"
  },
  "GRT": {
    "symbol": "GRT",
    "name": "Graph Token (Wormhole)",
    "address": "HGsLG4PnZ28L8A4R5nPqKgZd86zUUdmfnkTRnuFJ5dAX",
    "origin": "ethereum",
    "coingeckoId": "the-graph",
    "serumV3Usdc": "4PD799gihM2SdM8g7PxfSWgQR8cWGNiuzmNzcL2RgpSu",
    "sourceAddress": "0xc944E90C64B2c07662A292be6244BDf05Cda44a7",
    "sourceContract": "https://etherscan.io/address/0xc944E90C64B2c07662A292be6244BDf05Cda44a7"
  },
  "HBTC": {
    "symbol": "HBTC",
    "name": "Huobi BTC (Wormhole)",
    "address": "7dVH61ChzgmN9BwG4PkzwRP8PbYwPJ7ZPNF2vamKT2H8",
    "origin": "ethereum",
    "coingeckoId": "huobi-btc",
    "sourceAddress": "0x0316eb71485b0ab14103307bf65a021042c6d380",
    "sourceContract": "https://etherscan.io/address/0x0316eb71485b0ab14103307bf65a021042c6d380"
  },
  "HGET": {
    "symbol": "HGET",
    "name": "Hedget (Wormhole)",
    "address": "2ueY1bLcPHfuFzEJq7yN1V2Wrpu8nkun9xG2TVCE1mhD",
    "origin": "ethereum",
    "coingeckoId": "hedget",
    "serumV3Usdc": "27e1mB6UoPohbc3MmwMXu5QM7b2E3k5Mbhwv6JguwyXg",
    "sourceAddress": "0x7968bc6a03017eA2de509AAA816F163Db0f35148",
    "sourceContract": "https://etherscan.io/address/0x7968bc6a03017eA2de509AAA816F163Db0f35148"
  },
  "HUSD": {
    "symbol": "HUSD",
    "name": "HUSD (Wormhole)",
    "address": "7VQo3HFLNH5QqGtM8eC3XQbPkJUu7nS9LeGWjerRh5Sw",
    "origin": "ethereum",
    "coingeckoId": "husd",
    "sourceAddress": "0xdf574c24545e5ffecb9a659c229253d4111d87e1",
    "sourceContract": "https://etherscan.io/address/0xdf574c24545e5ffecb9a659c229253d4111d87e1"
  },
  "HXRO": {
    "symbol": "HXRO",
    "name": "Hxro (Wormhole)",
    "address": "HxhWkVpk5NS4Ltg5nij2G671CKXFRKPK8vy271Ub4uEK",
    "origin": "ethereum",
    "coingeckoId": "hxro",
    "serumV3Usdc": "CBb5zXwNRB73WVjs2m21P5prcEZa6SWmej74Vzxh8dRm",
    "sourceAddress": "0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3",
    "sourceContract": "https://etherscan.io/address/0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3"
  },
  "LINK": {
    "symbol": "LINK",
    "name": "ChainLink Token (Wormhole)",
    "address": "2wpTofQ8SkACrkZWrZDjXPitYa8AwWgX8AfxdeBRRVLX",
    "origin": "ethereum",
    "coingeckoId": "chainlink",
    "serumV3Usdc": "FJMjxMCiDKn16TLhXUdEbVDH5wC6k9EHYJTcrH6NcbDE",
    "sourceAddress": "0x514910771af9ca656af840dff83e8264ecf986ca",
    "sourceContract": "https://etherscan.io/address/0x514910771af9ca656af840dff83e8264ecf986ca"
  },
  "LUA": {
    "symbol": "LUA",
    "name": "LuaToken (Wormhole)",
    "address": "5Wc4U1ZoQRzF4tPdqKQzBwRSjYe8vEf3EvZMuXgtKUW6",
    "origin": "ethereum",
    "coingeckoId": "luaswap",
    "serumV3Usdc": "J9imTcEeahZqKuaoQaPcCeSGCMWL8qSACpK4B7bC8NN4",
    "sourceAddress": "0xb1f66997a5760428d3a87d68b90bfe0ae64121cc",
    "sourceContract": "https://etherscan.io/address/0xb1f66997a5760428d3a87d68b90bfe0ae64121cc"
  },
  "LUNA": {
    "symbol": "LUNA",
    "name": "LUNA (Wormhole)",
    "address": "F6v4wfAdJB8D8p77bMXZgYt8TDKsYxLYxH5AFhUkYx9W",
    "origin": "terra",
    "coingeckoId": "terra-luna",
    "serumV3Usdc": "HBTu8hNaoT3VyiSSzJYa8jwt9sDGKtJviSwFa11iXdmE",
    "sourceAddress": "uluna"
  },
  "MATH": {
    "symbol": "MATH",
    "name": "MATH Token (Wormhole)",
    "address": "CaGa7pddFXS65Gznqwp42kBhkJQdceoFVT7AQYo8Jr8Q",
    "origin": "ethereum",
    "coingeckoId": "math",
    "serumV3Usdc": "G8L1YLrktaG1t8YBMJs3CwV96nExvJJCSpw3DARPDjE2",
    "sourceAddress": "0x08d967bb0134f2d07f7cfb6e246680c53927dd30",
    "sourceContract": "https://etherscan.io/address/0x08d967bb0134f2d07f7cfb6e246680c53927dd30"
  },
  "MATICet": {
    "symbol": "MATICet",
    "name": "Matic (Wormhole from Ethereum)",
    "address": "C7NNPWuZCNjZBfW5p6JvGsR8pUdsRpEdP1ZAhnoDwj7h",
    "origin": "ethereum",
    "coingeckoId": "polygon",
    "sourceAddress": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",
    "sourceContract": "https://etherscan.io/address/0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"
  },
  "MATICpo": {
    "symbol": "MATICpo",
    "name": "Matic (Wormhole from Polygon)",
    "address": "Gz7VkD4MacbEB6yC5XD3HcumEiYx2EtDYYrfikGsvopG",
    "origin": "polygon",
    "coingeckoId": "polygon",
    "serumV3Usdc": "5WRoQxE59966N2XfD2wYy1uhuyKeoVJ9NBMH6r6RNYEF",
    "sourceAddress": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
    "sourceContract": "https://polygonscan.com/address/0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
  },
  "PAXG": {
    "symbol": "PAXG",
    "name": "Paxos Gold (Wormhole)",
    "address": "C6oFsE8nXRDThzrMEQ5SxaNFGKoyyfWDDVPw37JKvPTe",
    "origin": "ethereum",
    "coingeckoId": "pax-gold",
    "serumV3Usdc": "BeyB6W2iNsH9qSfb7icLTmSPDu8oUGkarMZed4Unrnsr",
    "sourceAddress": "0x45804880de22913dafe09f4980848ece6ecbaf78",
    "sourceContract": "https://etherscan.io/address/0x45804880de22913dafe09f4980848ece6ecbaf78"
  },
  "PERP": {
    "symbol": "PERP",
    "name": "Perpetual (Wormhole)",
    "address": "9BsnSWDPfbusseZfnXyZ3un14CyPMZYvsKjWY3Y8Gbqn",
    "origin": "ethereum",
    "coingeckoId": "perpetual-protocol",
    "serumV3Usdc": "Ao8HgYFCT2BJHxSusZbpJCPhvFMFXZApqN2uy2trbQRa",
    "sourceAddress": "0xbC396689893D065F41bc2C6EcbeE5e0085233447",
    "sourceContract": "https://etherscan.io/address/0xbC396689893D065F41bc2C6EcbeE5e0085233447"
  },
  "QUICK": {
    "symbol": "QUICK",
    "name": "Quickswap (Wormhole)",
    "address": "5njTmK53Ss5jkiHHZvzabVzZj6ztu6WYWpAPYgbVnbjs",
    "origin": "polygon",
    "coingeckoId": "quickswap",
    "sourceAddress": "0x831753dd7087cac61ab5644b308642cc1c33dc13",
    "sourceContract": "https://polygonscan.com/address/0x831753dd7087cac61ab5644b308642cc1c33dc13"
  },
  "RSR": {
    "symbol": "RSR",
    "name": "Reserve Rights (Wormhole)",
    "address": "DkbE8U4gSRuGHcVMA1LwyZPYUjYbfEbjW8DMR3iSXBzr",
    "origin": "ethereum",
    "coingeckoId": "reserve-rights-token",
    "serumV3Usdc": "GqgkxEswUwHBntmzb5GpUhKrVpJhzreSruZycuJwdNwB",
    "sourceAddress": "0x8762db106B2c2A0bccB3A80d1Ed41273552616E8",
    "sourceContract": "https://etherscan.io/address/0x8762db106B2c2A0bccB3A80d1Ed41273552616E8"
  },
  "SRMet": {
    "symbol": "SRMet",
    "name": "Serum (Wormhole from Ethereum)",
    "address": "xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG",
    "origin": "ethereum",
    "coingeckoId": "serum",
    "sourceAddress": "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff",
    "sourceContract": "https://etherscan.io/address/0x476c5e26a75bd202a9683ffd34359c0cc15be0ff"
  },
  "SUSHI": {
    "symbol": "SUSHI",
    "name": "SushiToken (Wormhole)",
    "address": "ChVzxWRmrTeSgwd3Ui3UumcN8KX7VK3WaD4KGeSKpypj",
    "origin": "ethereum",
    "coingeckoId": "sushi",
    "serumV3Usdc": "3uWVMWu7cwMnYMAAdtsZNwaaqeeeZHARGZwcExnQiFay",
    "sourceAddress": "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2",
    "sourceContract": "https://etherscan.io/address/0x6b3595068778dd592e39a122f4f5a5cf09c90fe2"
  },
  "SWAG": {
    "symbol": "SWAG",
    "name": "Swag Token (Wormhole)",
    "address": "5hcdG6NjQwiNhVa9bcyaaDsCyA1muPQ6WRzQwHfgeeKo",
    "origin": "ethereum",
    "coingeckoId": "swag-finance",
    "serumV3Usdc": "wSkeLMv3ktJyLm51bvQWxY2saGKqGxbnUFimPxbgEvQ",
    "sourceAddress": "0x87eDfFDe3E14c7a66c9b9724747a1C5696b742e6",
    "sourceContract": "https://etherscan.io/address/0x87eDfFDe3E14c7a66c9b9724747a1C5696b742e6"
  },
  "SXP": {
    "symbol": "SXP",
    "name": "Swipe (Wormhole)",
    "address": "3CyiEDRehaGufzkpXJitCP5tvh7cNhRqd9rPBxZrgK5z",
    "origin": "ethereum",
    "coingeckoId": "swipe",
    "serumV3Usdc": "G5F84rfqmWqzZv5GBpSn8mMwW8zJ2B4Y1GpGupiwjHNM",
    "sourceAddress": "0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9",
    "sourceContract": "https://etherscan.io/address/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9"
  },
  "UBXT": {
    "symbol": "UBXT",
    "name": "UpBots (Wormhole)",
    "address": "FTtXEUosNn6EKG2SQtfbGuYB4rBttreQQcoWn1YDsuTq",
    "origin": "ethereum",
    "coingeckoId": "upbots",
    "serumV3Usdc": "Hh4p7tJpqkGW6xsHM2LiPPMpJg43fwn5TbmVmfrURdLY",
    "sourceAddress": "0x8564653879a18C560E7C0Ea0E084c516C62F5653",
    "sourceContract": "https://etherscan.io/address/0x8564653879a18C560E7C0Ea0E084c516C62F5653"
  },
  "UNI": {
    "symbol": "UNI",
    "name": "Uniswap (Wormhole)",
    "address": "8FU95xFJhUUkyyCLU13HSzDLs7oC4QZdXQHL6SCeab36",
    "origin": "ethereum",
    "coingeckoId": "uniswap",
    "serumV3Usdc": "B7b5rjQuqQCuGqmUBWmcCTqaL3Z1462mo4NArqty6QFR",
    "sourceAddress": "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
    "sourceContract": "https://etherscan.io/address/0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
  },
  "USDCbs": {
    "symbol": "USDCbs",
    "name": "USD Coin (Wormhole from BSC)",
    "address": "FCqfQSujuPxy6V42UvafBhsysWtEq1vhjfMN1PUbgaxA",
    "origin": "bsc",
    "coingeckoId": "usd-coin",
    "sourceAddress": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
    "sourceContract": "https://bscscan.com/address/0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"
  },
  "USDCet": {
    "symbol": "USDCet",
    "name": "USD Coin (Wormhole from Ethereum)",
    "address": "A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM",
    "origin": "ethereum",
    "coingeckoId": "usd-coin",
    "sourceAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "sourceContract": "https://etherscan.io/address/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
  },
  "USDCpo": {
    "symbol": "USDCpo",
    "name": "USD Coin (Wormhole from Polygon)",
    "address": "E2VmbootbVCBkMNNxKQgCLMS1X3NoGMaYAsufaAsf7M",
    "origin": "polygon",
    "coingeckoId": "usd-coin",
    "sourceAddress": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "sourceContract": "https://polygonscan.com/token/0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
  },
  "USDK": {
    "symbol": "USDK",
    "name": "USDK (Wormhole)",
    "address": "43m2ewFV5nDepieFjT9EmAQnc1HRtAF247RBpLGFem5F",
    "origin": "ethereum",
    "coingeckoId": "usdk",
    "sourceAddress": "0x1c48f86ae57291f7686349f12601910bd8d470bb",
    "sourceContract": "https://etherscan.io/address/0x1c48f86ae57291f7686349f12601910bd8d470bb"
  },
  "USDTbs": {
    "symbol": "USDTbs",
    "name": "Tether USD (Wormhole from BSC)",
    "address": "8qJSyQprMC57TWKaYEmetUR3UUiTP2M3hXdcvFhkZdmv",
    "origin": "bsc",
    "coingeckoId": "tether",
    "sourceAddress": "0x55d398326f99059ff775485246999027b3197955",
    "sourceContract": "https://bscscan.com/address/0x55d398326f99059ff775485246999027b3197955"
  },
  "USDTet": {
    "symbol": "USDTet",
    "name": "Tether USD (Wormhole from Ethereum)",
    "address": "Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1",
    "origin": "ethereum",
    "coingeckoId": "tether",
    "sourceAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "sourceContract": "https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7"
  },
  "USDTpo": {
    "symbol": "USDTpo",
    "name": "Tether USD (Wormhole from Polygon)",
    "address": "5goWRao6a3yNC4d6UjMdQxonkCMvKBwdpubU3qhfcdf1",
    "origin": "polygon",
    "coingeckoId": "tether",
    "sourceAddress": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
    "sourceContract": "https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
  },
  "UST": {
    "symbol": "UST",
    "name": "UST (Wormhole)",
    "address": "9vMJfxuKxXBoEa7rM12mYLMwTacLMLDJqHozw96WQL8i",
    "origin": "terra",
    "coingeckoId": "terra-usd",
    "sourceAddress": "uusd"
  },
  "WBTC": {
    "symbol": "WBTC",
    "name": "Wrapped BTC (Wormhole)",
    "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
    "origin": "ethereum",
    "coingeckoId": "wrapped-bitcoin",
    "sourceAddress": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "sourceContract": "https://etherscan.io/address/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"
  },
  "YFI": {
    "symbol": "YFI",
    "name": "yearn.finance (Wormhole)",
    "address": "BXZX2JRJFjvKazM1ibeDFxgAngKExb74MRXzXKvgikxX",
    "origin": "ethereum",
    "coingeckoId": "yearn-finance",
    "serumV3Usdc": "BiJXGFc1c4gyPpv9HLRJoKbZewWQrTCHGuxYKjYMQJpC",
    "sourceAddress": "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e",
    "sourceContract": "https://etherscan.io/address/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e"
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
  df['serumV3Usdc'] = ['' if pd.isna(x) else x for x in df['serumV3Usdc'].values]
  df['sourceAddress'] = [_link_source_address(x, y) for (x,y) in
                         zip(df['sourceAddress'].values, df['sourceContract'].values)]

  df = df.drop(['coingeckoId', 'sourceContract'], axis=1)

  txt = df.to_markdown(index=False)
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
