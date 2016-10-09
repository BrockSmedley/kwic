from kwic8 import *

result = kwic("hard design is hard. design is hard is hard", ['hard'], True)

for r in result:
    print r
