JSON = $(wildcard ../CIMJSON-LD/*.jsonld)
TRIG = $(patsubst ../CIMJSON-LD/%.jsonld,raw/%.trig, $(JSON))

all: $(TRIG) Telemark-asset.patch

raw/%.trig: ../CIMJSON-LD/%.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

Telemark-asset.patch: $(TRIG)
	diff -bu1 --from-file=raw *.trig > $@
