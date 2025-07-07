JSON = $(wildcard ../CIMJSON-LD/*.jsonld)
TRIG = $(patsubst ../CIMJSON-LD/%.jsonld,%.trig, $(JSON)) Telemark-120_AO.trig

all: $(TRIG)

%.trig: ../CIMJSON-LD/%.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

Telemark-120_AO.trig: ../CIMJSON-LD/AviationObstacle/Telemark-120_AO.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

