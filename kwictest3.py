from kwic3 import *

result = kwic("Design is hard\nLet's just implement")

for r in result:
    print r

assert(type(result[0][1]) is int)
