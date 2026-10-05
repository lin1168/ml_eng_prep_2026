counts = set()                              # top level, column 0
with open("../data/raw/secom.data") as f:      # ':' opens a block
    for line in f:                          # 4 spaces in = inside the 'with'
        counts.add(len(line.split()))       # 8 spaces in = inside the 'for'
print(counts)                               # back to column 0 = both blocks closed