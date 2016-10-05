from kwic5 import *

result = kwic("Design is hard\nLet's just implement")
print result
assert result[0][1] == 0 and "Design" in result[0][0] and result[1][1] == 1 and "Let's" in result[1][0]
