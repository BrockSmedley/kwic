from kwic2 import *
from kwic1 import kwic as kwic1

sentences = "Design is hard\nLet's just implement"

result = kwic(sentences)

print result


#testing all shifts to see if the first word was moved to the last position of the next array entry
i = 0
for r in kwic1(sentences):
    length = len(r)

    for w in range(i, i + length-1):
        assert result[w][0] == result[w+1][len(result[w])-1]
    i += length
