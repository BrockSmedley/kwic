#breaks strings down by lines
def kwic0(string):
    #break string into lines (list)
    lines = break_lines(string)
    print lines
    return(lines)

#kwic0 + breaks lines into individual words
def kwic1(string):
    #break string into lines (list)
    lines = (break_lines(string))

    #break lines into lists of words
    sentence_list = []
    for l in lines:
        sentence_list.append(break_words(l))

    #now we have an array (word_list) of arrays containing words
    #return those arrays
    return sentence_list
    
    
#input: multi-line multi-word string
#output: list of multi-word strings separated by line
def break_lines(string):
    return string.split('\n')


#input: multi-word string
#output: array of words
def break_words(line):
    return line.split()
