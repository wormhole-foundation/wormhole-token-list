Logo generation
=================

## Logo properties
* adds a wormhole logo at the bottom right
* if symbol has multiple source chains (e.g. USDC), adds a chain logo at the bottom left

Examples:

CAKE:

![CAKE](../../assets/CAKE_wh.png)

USDTpo:

![USDTpo](../../assets/USDTpo_wh.png)

## Instructions

### Base logos
Base logos should be supplied either by adding png files to [src/logogen/base/](base/),
or by adding a logo component to [src/config/token_data.py](../config/token_data.py).
If both are present, we'll use the one in [src/logogen/base/](base/),

### Generating new logos
```
npm run genlogos
```

### Linking to logos
```
https://raw.githubusercontent.com/certusone/wormhole-token-list/main/assets/CAKE_wh.png
```