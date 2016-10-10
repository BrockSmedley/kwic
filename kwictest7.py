from kwic7 import *

result = kwic("hard design is hard design\nbuddy guy o buddy guy", ['hard'], True)

#check that the last value contains appropriate pair matches
assert ('buddy', 'guy') in result[len(result)-1][0]

for r in result:
    print r
