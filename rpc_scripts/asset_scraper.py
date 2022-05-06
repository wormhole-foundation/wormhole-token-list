# python 3.8.1

from web3 import Web3
import pandas as pd
import json
import sys
import requests
from terra_sdk.client.lcd import LCDClient


if len(sys.argv) == 1:
    print('Please pass csv file of (chain,address) to read')
    sys.exit(0)

# hardcoded erc20 abi for reading ERC20 contracts
erc20_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": True,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]

# default dev RPCs
web3_evm_providers = {
    'eth': Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/demo')),
    'avax': Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc')),
    'ftm': Web3(Web3.HTTPProvider('https://rpc.ftm.tools')),
    'matic': Web3(Web3.HTTPProvider('https://polygon-rpc.com')),
    'oasis': Web3(Web3.HTTPProvider('https://emerald.oasis.dev')),
    'bsc': Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org')),
    'aurora': Web3(Web3.HTTPProvider('https://mainnet.aurora.dev')),
}
terra_client = LCDClient(chain_id="columbus-5", url="https://lcd.terra.dev")

# solana tokens
r = requests.get('https://raw.githubusercontent.com/solana-labs/token-list/main/src/tokens/solana.tokenlist.json')
solana_tokens = r.json()
print(solana_tokens)

# to store decimals for all contracts
output_decimals = {}

def evmDecimals(origin, sourceAddrRaw):
    sourceAddr = Web3.toChecksumAddress(sourceAddrRaw)

    output_key = origin + '_' + sourceAddr
    if output_key in output_decimals:
        return

    originProvider = web3_evm_providers[origin]
    originContract = originProvider.eth.contract(sourceAddr, abi=erc20_abi)
    symbol = originContract.functions.symbol().call()
    decimals = originContract.functions.decimals().call()

    print(origin, symbol, decimals)
    output_decimals[output_key] = decimals


def solDecimals(sourceAddr):
    output_key = 'sol_' + sourceAddr
    if output_key in output_decimals:
        return

    for token_data in solana_tokens['tokens']:
        if token_data['address'] == sourceAddr:
            print('sol', token_data['symbol'], token_data['decimals'])
            output_decimals[output_key] = token_data['decimals']
            break


def terraDecimals(sourceAddr):
    output_key = 'terra_' + sourceAddr
    if output_key in output_decimals:
        return

    if sourceAddr == 'uusd' or sourceAddr == 'uluna':
        print('terra', sourceAddr, 6)
        output_decimals['terra_' + sourceAddr] = 6
        return

    contract_info = terra_client.wasm.contract_info(sourceAddr)
    decimals = contract_info['init_msg']['decimals']
    symbol = contract_info['init_msg']['symbol']
    print('terra', symbol, decimals)
    output_decimals['terra_' + sourceAddr] = decimals


def getTokenData(chain, raw_addr):
    if chain == 'sol':
        solDecimals(raw_addr)
    elif chain == 'terra':
        terraDecimals(raw_addr)
    else:
        evmDecimals(chain, raw_addr)

# given an input csv file of format (chain, address), where address is assumed to be a contract
# iterate through and get token data for the contract at each address
# see example_input.csv
df = pd.read_csv(sys.argv[1], header=None)
for _, row in df.iterrows():
    getTokenData(row[0], row[1])

# output as decimals_output.json with the decimals from RPC
f = open('decimals_output.json', 'w')
json.dump(output_decimals, f)
f.close()
