from kwic5 import *

result = kwic("Qesign is hard\nSuper hard\nLet's just implement")

#test for line numbers
for r in result:
    print r
    assert type(r[1]) is int
