JSON1 = $(wildcard ../CIMJSON-LD/*.geojson)
TTL1  = $(patsubst ../CIMJSON-LD/%.geojson,%.ttl, $(JSON1))
TRIG1 = $(patsubst ../CIMJSON-LD/%.geojson,%.trig,$(JSON1))

JSON2 = $(wildcard ../CIMJSON-LD/*.jsonld)
TRIG2 = $(patsubst ../CIMJSON-LD/%.jsonld,%.trig, $(JSON2))


all: $(TTL1) $(TRIG1) $(TRIG2)

%.ttl: ../CIMJSON-LD/%.geojson
	riot.bat --syntax jsonld --formatted trig $^ > $*.trig
#	owl.bat write $*.trig $*.ttl

%.trig: ../CIMJSON-LD/%.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

