from kwic8 import *

result = kwic("hard design is hard. design is hard is hard design\nand hard design is hard design bro", ['hard'], True, True)

hardcodedLengths = [4, 6, 7]

#test the lengths of the new sub-sentences; the new list's word list lengths should match the hardcoded values, if that makes any sense
for r in result:
    for l in range(3):
        if (r[1] == l):
            assert len(r[0]) == hardcodedLengths[l]

for r in result:
    print r
