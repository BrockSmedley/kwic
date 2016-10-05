from kwic4 import *

result = kwic("Design is hard\nDesign is hard\nLet's just implement")
print result

print result[0][0][0][0].lower()
print result[1][0][0][0].lower()

for i in range(len(result)-1):
    print i
    print result[i][0][0][0].lower()
    print result[i+1][0][0][0].lower()
    
    assert result[i][0][0].lower() <= result[i+1][0][0].lower()
