#breaks strings down by lines
def kwic0(sentences):
    print "kwic0"
    #break string into lines (list)
    lines = break_lines(sentences, "\n")
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

    #TODO: Something with this function

    return antList

#kwic5 + ignoreWords arg
def kwic6(sentences, ignoreWords = []):
    print "ignoreWords:"
    print ignoreWords
    lines = kwic5(sentences)
    lines = ignore_words(ignoreWords, lines)

    return lines

#kwic6 + listPairs arg
def kwic7(sentences, ignoreWords = [], listPairs=False):
    result = kwic6(sentences, ignoreWords)

    if (listPairs == True):
        pairs = find_pairs(result)
        result.append(pairs)
    
    return result

#kwic7 + periodsToBreaks
def kwic8(sentences, ignoreWords = [], listPairs=False, periodsToBreaks=False):
    #"x. " as delimiter

    if (periodsToBreaks == True):
        #break sentences by new delimiter
        alpha = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        removeMe = []
        
        for c in range(len(sentences)-1):
            for a in alpha:
                if (sentences[c] == a and sentences[c+1] == "." and sentences[c+2] == " "):
                    removeMe.append(a)
        
        for r in removeMe:
            sentences = (r + "\n").join(sentences.split(r + ". "))
    result = kwic7(sentences, ignoreWords, listPairs)


    return result
    
    
#input: multi-line multi-word string
#output: list of multi-word strings separated by line
def break_lines(string, delimiter):
    return string.split(delimiter)

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
    if (tupleList != []):
        return sorted(tupleList, key=lambda x: (x[0][0]).lower())
    else:
        return tupleList
    #thanks http://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column

#input: list of ignored words, list of tuples: (["strings"...], int)
#output: list of tuples missing ones that start with an ignored word
def ignore_words(ignoredWords, lines):
    newIgnored = []
    for a in ignoredWords:
        a = strip_punctuation(a)
        newIgnored.append(a)

    newLines = []
    i = 0
    for l in lines:
        wordList = []
        for w in l[0]:
            w = strip_punctuation(w)
            wordList.append(w)
        newTuple = (wordList, lines[i][1])
        newLines.append(newTuple)
        i += 1

    lines = newLines

    linesToRemove = []
    
    if (newIgnored == []):
        return lines
    else:
        for word in newIgnored:
            for line in lines:
                if (line[0][0].lower() == word.lower()):
                    linesToRemove.append(line)

        for rm in linesToRemove:
            lines.remove(rm)
        
        return lines

def strip_punctuation(word):
    ignoredChars = ['.', '?', ',', '!', ':']
    
    return "".join(x for x in word if x not in ignoredChars)

#input: return from kwic6
#output: kwic6 values + appended list of pairs & their line numbers
def find_pairs(result):
    lines = result
    
    #holds ((a,b), x) where a & b are words and x is a line number
    duplicatePairs = []
    numPairs = 0 #for indexing

    #for each word and the word next to it
        #   test if that pair of words appears again on the line
        #       if it does, append that pair to the list of pairs to return in a tuple with its line number
    
    for line in lines:
        words = line[0]
        lineNum = line[1]

        for i in range(len(words)-1):
            #make a tuple of pairs of words to test
            pair = (words[i], words[i+1])

            #test pair against other pairs on line
            for j in range(i+1, len(words)-1):
                p = (words[j], words[j+1])
                #if we find a matching pair
                if (pair == p):
                    #if the pair is already in the duplicates list & line number is not
                    plIndex = pairPresentIndex(duplicatePairs, p, lineNum)
                    if (plIndex >= 0):
                        #add the line number by assigning a new tuple
                        if (str(lineNum) not in duplicatePairs[plIndex][1]):
                            duplicatePairs[plIndex] = (duplicatePairs[plIndex][0], duplicatePairs[plIndex][1] + str(lineNum))
                    else:
                        #add the new item
                        duplicatePairs.append((p, str(lineNum)))
        
    return duplicatePairs

def pairPresentIndex(duplicatePairs, pair, lineNum):
    for pi in range(len(duplicatePairs)):
        if (pair in duplicatePairs[pi]):
            return pi
    
    return -1
