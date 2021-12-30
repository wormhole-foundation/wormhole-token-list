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
Base logos for token `TOK` should be supplied either by adding `TOK.png` to [src/logogen/base/](base/),
or by adding a `"logo"` entry to the appropriate block for `TOK` in [src/config/token_data.py](../config/token_data.py).
If both are present, we'll use the one in [src/logogen/base/](base/),

### Generating new logos
Run:
```
npm run gen-logos
```

This won't write over any existing images in [assets](../../assets].  To overwrite the existing assets:
```
npm run gen-logos-overwrite
```

### Linking to logos
```
https://raw.githubusercontent.com/certusone/wormhole-token-list/main/assets/CAKE_wh.png
```

## Styling

A few style choices are included (with examples):

thick_gray (default):

![CAKE](examples/CAKE_wh_thick_gray.png)
![UST](examples/UST_wh_thick_gray.png)

thin_gray:

![CAKE](examples/CAKE_wh_thin_gray.png)
![UST](examples/UST_wh_thin_gray.png)

color:

![CAKE](examples/CAKE_wh_color.png)
![UST](examples/UST_wh_color.png)

barecolor:

![CAKE](examples/CAKE_wh_barecolor.png)
![UST](examples/UST_wh_barecolor.png)

These variants are in [src/logogen/components](components/).

To generate all the outputs with a different style from the default, run:
```
python3 gen_logos.py --overwrite --style STYLE
```

To update the default style, copy one of them to [src/logogen/components/wormhole.png](components/wormhole.png).