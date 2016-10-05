from kwic1 import *

result = kwic("Design is hard\nLet's just implement")

assert (not(" " in result[0]))
