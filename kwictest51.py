from kwic5 import *

result = kwic("Qesign is hard\nSuper hard\nLet's just implement")

for r in result:
    assert type(r[1]) is int
