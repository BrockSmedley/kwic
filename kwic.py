#breaks strings down by lines
def kwic0(string):
    #break string into lines (list)
    lines = break_lines(string)
    return(lines)

#kwic0 + breaks lines into individual words
def kwic1(string):
    #break string into lines (list)
    lines = kwic0(string)

    #break lines into lists of words
    sentence_list = []
    for l in lines:
        sentence_list.append(break_words(l))

    #now we have an array (word_list) of arrays containing words
    #return those arrays
    return sentence_list

def kwic2(sentence_list):
    #print shifts on their own lines
    for s in sentenceList:
        shifts.append(s)
        for c in circ_shift(s):
            shifts.append(c)

    return shifts
    

    
#input: multi-line multi-word string
#output: list of multi-word strings separated by line
def break_lines(string):
    return string.split('\n')


#input: multi-word string
#output: array of words
def break_words(line):
    return line.split()


#input: array of words
#output: shifted array of words where the first item in input becomes last item in output
def circ_shift(wordsArray):
    numWords = len(wordsArray)
    wordShiftList = []
    sentenceShiftList = []

    for h in range(numWords-1):
        #shift first word to last
        for i in range(numWords):
            if(i < numWords-1):
                wordShiftList.append(wordsArray[i+1])
            else:
                wordShiftList.append(wordsArray[0])
                
        sentenceShiftList.append(wordShiftList)
        wordsArray = wordShiftList
        wordShiftList = []

    return sentenceShiftList
