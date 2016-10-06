#breaks strings down by lines
def kwic0(sentences):
    print "kwic0"
    #break string into lines (list)
    lines = break_lines(sentences)
    return(lines)

#kwic0 + breaks lines into individual words
def kwic1(sentences):
    print "kwic1"
    
    #break string into lines (list)
    lines = kwic0(sentences)

    #break lines into lists of words
    sentenceList = []
    for l in lines:
        sentenceList.append(break_words(l))

    #now we have an array (word_list) of arrays containing words
    #return those arrays
    return sentenceList

#kwic1 + circular shifts
def kwic2(sentences):
    print "kwic2"
    sentenceList = kwic1(sentences)
    
    #print shifts on their own lines
    shifts = []
    for s in sentenceList:
        shifts.append(s)
        for c in circ_shift(s):
            shifts.append(c)

    return shifts

#kwic2 + numbered tuples
def kwic3(sentences):
    print "kwic3"
    
    #list of sencentes broken up by word
    sentenceList = kwic1(sentences)
    
    #list of shifted sentences
    shiftedSentenceList = kwic2(sentences)

    numberedTupleList = []
    n = 0
    for sentence in sentenceList:
        numTuple = (sentence, n)
        n += 1
        numberedTupleList.append(numTuple)

    #now we have a sentence list with numbered lines
    #shift the sentence, numbering each line
    n = 0
    k = 0
    shiftedNumberedTupleList = []
    
    for sentence in sentenceList:
        for word in sentence:
            stuple = (shiftedSentenceList[k], n)
            shiftedNumberedTupleList.append(stuple)
            k += 1
        n += 1

    return shiftedNumberedTupleList

#kwic3 + alphabetization
def kwic4(sentences):
    print "kwic4"
    numberedTupleList = kwic3(sentences)

    return alphabetize(numberedTupleList)

#kwic4 + line indices
def kwic5(sentences):
    print "kwic5"
    
    #ant = alphabetizedNumberedTuple
    antList = kwic4(sentences)

    return antList

#kwic5 + ignoreWords arg
def kwic6(sentences, ignoredWords = []):
    lines = kwic5(sentences)
    lines = ignore_words(ignoredWords, lines)

    return lines
    
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

#input: list of tuples; first item: list of strings; second item: integer
#output: same type of list in alphabetical order
def alphabetize(tupleList):
    return sorted(tupleList, key=lambda x: (x[0][0]).lower())
    #thanks http://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column

#input: list of ignored words, list of tuples: (["strings"...], int)
#output: list of tuples missing ones that start with an ignored word
def ignore_words(ignoredWords, lines):
    if (ignoredWords == []):
        return lines
    else:
        for line in lines:
            for word in ignoredWords:
                if (line[0][0].lower() == word.lower()):
                    lines.remove(line)
                    break
        return lines
