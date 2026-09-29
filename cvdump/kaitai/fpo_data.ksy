meta:
  endian: le
  id: fpo_data
doc: 'FPO_DATA (winnt.h)'
seq:
  - id: offset
    type: u4
    doc: ulOffStart
  - id: proc_size
    type: u4
    doc: cbProcSize
  - id: count_locals
    type: u4
    doc: cdwLocals
  - id: count_params
    type: u2
    doc: cdwParams
  - id: flags
    type: u2
    doc: |
      WORD cbProlog : 8;
      WORD cbRegs : 3;
      WORD fHasSEH : 1;
      WORD fUseBP : 1;
      WORD reserved : 1;
      WORD cbFrame : 2;
types:
  fpo_datas:
    seq:
      - id: items
        type: fpo_data
        repeat: eos
