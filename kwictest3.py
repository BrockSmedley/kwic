from kwic3 import *

result = kwic("Design is hard\nLet's just implement")
print result

assert(type(result[0][1]) is int)
