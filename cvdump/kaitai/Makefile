
KSC = kaitai-struct-compiler
KSC_FLAGS := -t python

SCHEMAS := \
    msf.ksy \
    info_stream.ksy \
    names_stream.ksy \
    dbi_stream.ksy \
    tpi_stream.ksy

.PHONY: all clean

all: $(SCHEMAS:.ksy=.py)

%.py: %.ksy
	$(KSC) $(KSC_FLAGS) $<

clean:
	rm -f $(SCHEMAS:.ksy=.py)
