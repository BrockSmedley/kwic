from kwic4 import *

result = kwic("Design is hard\nLet's just implement")
print result

for i in range(len(result)-1):
    assert result[i][0][0] < result[i+1][0][0]
