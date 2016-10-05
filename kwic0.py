#breaks strings down by lines
def kwic(string):
    #break string into lines (list)
    lines = break_lines(string)
    print lines
    return(lines)
    
    
#input: multi-line multi-word string
#output: list of multi-word strings separated by line
def break_lines(string):
    return string.split('\n')
