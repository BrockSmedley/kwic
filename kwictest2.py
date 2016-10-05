from kwic2 import *

sentences = "Design is hard\nLet's just implement"

result = kwic(sentences)
print result

length = len(result[0])
print length

assert(result[0][0] == result[1][length-1])
