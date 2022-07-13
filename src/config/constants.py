from collections import OrderedDict


CHAIN_IDS_TO_NAMES = OrderedDict([
  (1, 'sol'),
  (2, 'eth'),
  (3, 'terra'),
  (4, 'bsc'),
  (5, 'matic'),
  (6, 'avax'),
  (7, 'oasis'),
  (9, 'aurora'),
  (10, 'ftm'),
  (11, 'karura'),
  (12, 'celo'),
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
  ('ftm', ('Fantom', 'ft', "https://ftmscan.com", "https://ftmscan.com/address/0x7C9Fc5741288cDFdD83CeB07f3ea7e22618D79D2")),
  ('aurora', ('Aurora', 'au', "https://aurorascan.dev", "https://aurorascan.dev/address/0x51b5123a7b0F9b2bA265f9c4C8de7D78D52f510F")),
  ('karura', ('Karura', 'ka', "https://blockscout.karura.network", "https://blockscout.karura.network/address/0x0000000000000000000100000000000000000080")),
  ('celo', ('Celo', 'ce', "https://celoscan.io", "https://celoscan.io/address/0x796dff6d74f3e27060b71255fe517bfb23c93eed")),
])

SUFFIXES = [x[1] for x in SOURCE_INFO.values()]
ABBREVS_TO_CHAINS = {y[1]: x for (x, y) in SOURCE_INFO.items()}
