from kwic6 import *

result = kwic("Design is hard.\nLet's just implement.\nAnd not use comments, either.", ["and"])

for i in result:
    print i
    assert i[0][0].lower() != "and"
