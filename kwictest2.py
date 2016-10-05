from kwic2 import *

sentences = "Design is hard\nLet's just implement"

result = kwic(sentences)

length = len(result[0])

print result

assert(result[0][0] == result[1][length-1])
