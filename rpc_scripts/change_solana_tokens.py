import json

f = open('decimals_output.json')
output_decimals = json.load(f)
f.close()

# add decimals for solana wormhole tokens
# read the json file
f = open('src/utils/solana_wormhole_tokens.json')
solana_wormhole_tokens = json.load(f)
f.close()

# iterate over the keys
for token in solana_wormhole_tokens.keys():
    output_decimals_key = 'sol_' + solana_wormhole_tokens[token]['address']
    decimals = output_decimals[output_decimals_key]
    solana_wormhole_tokens[token]['decimals'] = decimals

# output new json file
f = open('solana_wormhole_tokens_new.json', 'w')
json.dump(solana_wormhole_tokens, f)
f.close()
