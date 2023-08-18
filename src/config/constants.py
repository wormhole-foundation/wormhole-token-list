from collections import OrderedDict


CHAIN_IDS_TO_NAMES = OrderedDict([
  (1, 'sol'),
  (2, 'eth'),
  (3, 'terra'),
  (4, 'bsc'),
  (5, 'matic'),
  (6, 'avax'),
  (7, 'oasis'),
  (8, 'algorand'),
  (9, 'aurora'),
  (10, 'ftm'),
  (11, 'karura'),
  (12, 'acala'),
  (13, 'klaytn'),
  (14, 'celo'),
  (15, 'near'),
  (16, 'moonbeam'),
  (18, 'terra2'),
  (19, 'injective'),
  (22, 'aptos'),
  (23, 'arbitrum'),
  (24, 'optimism'),
  (28, 'xpla'),
  (30, 'base'),
])
CHAIN_NAMES_TO_IDS = OrderedDict([(v, k) for (k, v) in CHAIN_IDS_TO_NAMES.items()])

SOURCE_INFO = OrderedDict([
  ('sol', ('Solana', 'so', "https://solscan.io", "https://solscan.io/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb")),
  ('eth', ('Ethereum', 'et', "https://etherscan.io", "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585")),
  ('bsc', ('BSC', 'bs', "https://bscscan.com", "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7")),
  ('terra', ('Terra', 'te', "https://finder.terra.money/columbus-5", "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf")),
  ('matic', ('Polygon', 'po', "https://polygonscan.com", "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde")),
  ('avax', ('Avalanche', 'av', "https://snowtrace.io", "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052")),
  ('oasis', ('Oasis', 'oa', "https://explorer.oasis.updev.si", "https://explorer.oasis.updev.si/address/0x5848C791e09901b40A9Ef749f2a6735b418d7564")),
  ('algorand', ('Algorand', 'al', "https://algoexplorer.io/", "https://algoexplorer.io/asset/31566704")),
  ('ftm', ('Fantom', 'ft', "https://ftmscan.com", "https://ftmscan.com/address/0x7C9Fc5741288cDFdD83CeB07f3ea7e22618D79D2")),
  ('aurora', ('Aurora', 'au', "https://aurorascan.dev", "https://aurorascan.dev/address/0x51b5123a7b0F9b2bA265f9c4C8de7D78D52f510F")),
  ('karura', ('Karura', 'ka', "https://blockscout.karura.network", "https://blockscout.karura.network/address/0x0000000000000000000100000000000000000080")),
  ('acala', ('Acala', 'ac', "https://blockscout.acala.network", "https://blockscout.acala.network/address/0x0000000000000000000100000000000000000000")),
  ('klaytn', ('Klaytn', 'kl', "https://scope.klaytn.com/", "https://scope.klaytn.com/token/0xe4f05a66ec68b54a58b17c22107b02e0232cc817")),
  ('celo', ('Celo', 'ce', "https://celoscan.io", "https://celoscan.io/address/0x796dff6d74f3e27060b71255fe517bfb23c93eed")),
  ('near', ('Near', 'ne', "https://explorer.near.org/", "https://explorer.near.org/accounts/token.sweat")),
  ('moonbeam', ('Moonbeam', 'mo', "https://moonscan.io", "https://moonscan.io/token/0xacc15dc74880c9944775448304b263d191c6077f")),
  ('terra2', ('Terra2', 't2', "https://finder.terra.money", "https://finder.terra.money/mainnet/address/terra153366q50k7t8nn7gec00hg66crnhkdggpgdtaxltaq6xrutkkz3s992fw9")),
  ('injective', ('Injective', 'in', "https://explorer.injective.network", "https://explorer.injective.network/contract/inj1sthrn5ep8ls5vzz8f9gp89khhmedahhdkqa8z3")),
  ('xpla', ('XPLA', 'xp', "https://explorer.xpla.io/", "https://explorer.xpla.io/mainnet/address/xpla137w0wfch2dfmz7jl2ap8pcmswasj8kg06ay4dtjzw7tzkn77ufxqfw7acv")),
  ('optimism', ('Optimism', 'op', "https://optimistic.etherscan.io/", "https://optimistic.etherscan.io/token/0x94b008aa00579c1307b0ef2c499ad98a8ce58e58")),
  ('arbitrum', ('Arbitrum', 'ab', "https://arbiscan.io/", "https://arbiscan.io/token/0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9")),
  ('aptos', ('Aptos', 'ap', "https://explorer.aptoslabs.com/", "https://explorer.aptoslabs.com/account/0x576410486a2da45eee6c949c995670112ddf2fbeedab20350d506328eefc9d4f")),
  ('base', ('Base', 'ba', "https://basescan.org/", "https://basescan.org/address/0x8d2de8d2f73f1f4cab472ac9a881c9b123c79627")),
])

SUFFIXES = [x[1] for x in SOURCE_INFO.values()]
ABBREVS_TO_CHAINS = {y[1]: x for (x, y) in SOURCE_INFO.items()}
