from kwic7 import *

result = kwic("hard design is hard design\nbuddy guy o buddy guy", ['hard'], True)

assert result[len(result)-1] == [(('buddy', 'guy'), 1), (('hard', 'design'), 0)]

for r in result:
    print r
