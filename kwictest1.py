from kwic1 import *

result = kwic("Design is hard\nLet's just implement")
print result

#testing to make sure that no spaces are in the result
#this would mean that all spaces have been stripped and we have a list of lone words
assert (not(" " in result[0]))
