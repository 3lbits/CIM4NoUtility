JSON = $(wildcard ../CIMJSON-LD/*.jsonld)
TRIG = $(patsubst ../CIMJSON-LD/%.jsonld,raw/%.trig, $(JSON)) raw/Telemark-120_AO.trig

all: $(TRIG) Telemark-asset.patch

raw/%.trig: ../CIMJSON-LD/%.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

raw/Telemark-120_AO.trig: ../CIMJSON-LD/AviationObstacle/Telemark-120_AO.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

Telemark-asset.patch: $(TRIG)
	diff -bu1 --from-file=raw *.trig > $@
