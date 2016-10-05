from kwic1 import *

result = kwic("Design is hard\nLet's just implement")
print result

assert (not(" " in result[0]))
