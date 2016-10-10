from kwic3 import *

result = kwic("Design is hard\nLet's just implement")

#test to see if second element in each entry is an integer
for i in range(len(result)):
    assert(type(result[i][1]) is int)
