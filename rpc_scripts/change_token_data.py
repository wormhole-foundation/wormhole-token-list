from web3 import Web3
from src.config.token_data import TOKENS
import json

f = open('decimals_output.json')
output_decimals = json.load(f)
f.close()

def get_decimals(chain, addr):
    output_key = chain + '_' + addr

    if output_key == 'sol_Bzq68gAVedKqQkQbsM28yQ4LYpc2VComDUD9wJBywdTi':
        return 8
    if output_key == 'sol_4CsZsUCoKFiaGyU7DEVDayqeVtG8iqgGDR6RjzQmzQao':
        return 6

    # try normal addr. If that doesn't work try checksum
    if output_key in output_decimals:
        return output_decimals[output_key]

    checksummed_output_key = chain + '_' + Web3.toChecksumAddress(addr)
    if checksummed_output_key == 'ftm_0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83':
        return 18

    return output_decimals[checksummed_output_key]

# read the tokens thing
# for each key in the tokens (key is native asset)
#     iterate over the keys in this dict (these keys are the tokens)
#     for each of these keys, we want to change destAddresses to just be "destinations". "destinations" is a dict keyed by chain, where values are { address, decimals }
#     we also want to add the decimals for the token itself (this is top level)
for chain, chain_tokens in TOKENS.items():
    for symbol, data in chain_tokens.items():
        # decimals for the token itself
        data['sourceDecimals'] = get_decimals(chain, data['sourceAddress'])
        del data['decimals']

        # decimals for each destination
        # destinations = {}
        # for dest_chain, dest_addr in data['destAddresses'].items():
            # dest_decimals = get_decimals(dest_chain, dest_addr)
            # destinations[dest_chain] = {
                # "address": dest_addr,
                # "decimals": dest_decimals
            # }
        # del data['destAddresses']
        # data['destinations'] = destinations

f = open('new_tokens.json', 'w')
json.dump(TOKENS, f)
f.close()
