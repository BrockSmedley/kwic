from kwic4 import *

result = kwic("Design is hard\nIt really is hard\nLet's just implement")
for i in result:
    print i


for i in range(len(result)-1):    
    assert result[i][0][0].lower() <= result[i+1][0][0].lower()
