
KSC = kaitai-struct-compiler
KSC_FLAGS := -t python

SCHEMAS := \
    dbi_stream.ksy \
    msf_small_superblock.ksy \
    msf_small_directory.ksy \
    tpi_stream.ksy

.PHONY: all clean

all: $(SCHEMAS:.ksy=.py)

%.py: %.ksy
	$(KSC) $(KSC_FLAGS) $<

clean:
	rm -f $(SCHEMAS:.ksy=.py)
