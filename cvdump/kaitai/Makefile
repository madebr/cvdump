
KSC = kaitai-struct-compiler
KSC_FLAGS := -t python --python-package cvdump.kaitai

SCHEMAS := \
    dbi_stream.ksy \
    info_stream.ksy \
    modi_stream.ksy \
    msf.ksy \
    names_stream.ksy \
    numeric.ksy \
    tpi_stream.ksy

.PHONY: all clean

all: $(SCHEMAS:.ksy=.py)

%.py: %.ksy
	$(KSC) $(KSC_FLAGS) $<

clean:
	rm -f $(SCHEMAS:.ksy=.py)
