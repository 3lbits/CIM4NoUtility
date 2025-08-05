This folder `CIMTRIG` is the result ofconverting `CIMJSON-LD` to Turtle (ttl) and Turtle with graphs (trig).
- The source has 20 `jsonld` files: they are converted to `trig`.
- It also has 3 `geojson` files: they are converted to `ttl`
  - `Telemark-120-LV1_GL.geojson, Telemark-120-MV1_GL.geojson` are also present as `jsonld` so we convert them to `ttl` to ensure they don't conflict with the other 2 sources
  - `Telemark-120-WattApp-GL.geojson` is converted only to `ttl`
