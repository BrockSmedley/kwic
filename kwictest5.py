from kwic5 import *

result = kwic("Qesign is hard\nSuper hard\nLet's just implement")


for i in range(len(result)-1):
    print result[i]
    assert result[i][0][0].lower() <= result[i+1][0][0].lower()
