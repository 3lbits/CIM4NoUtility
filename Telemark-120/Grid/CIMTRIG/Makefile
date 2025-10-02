JSON1 = $(wildcard ../CIMJSON-LD/*.geojson)
TTL   = $(patsubst ../CIMJSON-LD/%.geojson,%.ttl, $(JSON1))

JSON2 = $(wildcard ../CIMJSON-LD/*.jsonld)
TRIG  = $(patsubst ../CIMJSON-LD/%.jsonld,raw/%.trig, $(JSON2))


all: $(TTL) $(TRIG) Telemark-grid.patch

%.ttl: ../CIMJSON-LD/%.geojson
	riot.bat --syntax jsonld --formatted ttl $^ > temp.ttl
	owl.bat write temp.ttl $*.ttl
	rm temp.ttl

raw/%.trig: ../CIMJSON-LD/%.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

Telemark-grid.patch: $(TRIG)
	diff -bu1 --from-file=raw *.trig > $@
