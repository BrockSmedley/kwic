from kwic6 import *

result = kwic("Design! is hard.\nLet's just implement.\nAnd. not use comments, either.", ["and.", "nOt"])

#test all items in result to make sure our word was ignored
for i in result:
    print i
    assert i[0][0].lower() != "and"
    assert i[0][0].lower() != "not"

