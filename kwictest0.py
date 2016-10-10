from kwic0 import *

result = kwic("Design is hard\nLet's just implement")

#testing for whether these words are in the result, on the right line
assert ("Design" in s for s in result[0])
assert ("is" in s for s in result[0])
assert ("hard" in s for s in result[0])

assert ("Let's" in s for s in result[1])
assert ("just" in s for s in result[1])
assert ("implement" in s for s in result[1])

print result
