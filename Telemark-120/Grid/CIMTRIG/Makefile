JSON = $(wildcard ../CIMJSON-LD/*.jsonld ../CIMJSON-LD/*/*.jsonld)
TRIG = $(patsubst ../CIMJSON-LD/%.jsonld,%.trig, $(JSON))

all: $(TRIG)

%.trig: ../CIMJSON-LD/%.jsonld
	riot.bat --syntax jsonld --formatted trig $^ > $@

