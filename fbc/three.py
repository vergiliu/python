# Author: Vergiliu
# Date: ongoing
# fbc breathalyzer

#    def get(self, letter):
#        return self.children[letter]
#    def add(self, word, wordLength=-1, index=0): 
#        if wordLength < 0: wordLength = len(word)
#        if index >= wordLength: return
#        letter = word[index]
#        if letter in self.children:
#            child = self.children[letter]
#            child.add(word, wordLength, index+1)
#        else:
#            child = Cop(letter, index==wordLength-1)
#            self.children[letter] = child
#            child.add(word, wordLength, index+1)

import string


class Trie(object):

    result = False

    def __init__(self, letter, final=False):
        self.letter = letter
        self.final = final
        self.children = {}

    def __contains__(self, letter):
        return letter in self.children
    
    def add(self, word):
        isFinal=False
        if len(word) == 1:
            isFinal=True
        if word[0] in self.children:
            self.children[word[0]].add(word[1:])
        else:
            newLetter = Trie(word[0], final=isFinal)
            self.children[word[0]] = newLetter
            if len(word[1:]) != 0:
                self.children[word[0]].add(word[1:])

    def find(self, key):
        curr_node = self.children
        for ch in key:
            try:
                curr_node = curr_node[1][ch]
            except KeyError:
                return None
        return curr_node[0]
        
    def get(self, word):
        if word[0] in self.children:
            if len(word) == 1:
 #               print self.children[word[0]].letter, 
                if self.children[word[0]].final == True:
                    return 0
                else:
                    return 1
            elif word[1] in self.children[word[0]]:
                return 0 + self.children[word[0]].get(word[1:])
            else:
                return len(word)-1
        else:
#            print "3.%s(%d) " % (word[0], len(word))
            return int(len(word))


    def get_new(self, word):
        pass
        
#            return self.children[word[0]].final
###            return str(len(word))

def getMinimumValue(aTrie, word):
    minimumLength = aTrie.get(word)
    if  minimumLength == 0:
#        minimumLength = len(word)
        print "minimum = %s(%d)" % (word, minimumLength)

    elif minimumLength != 0:
        if len(word) >= 2:
            for aWord in removeLetter(word):
                newMinimum = aTrie.get(aWord)
                print "remove lettter = %s(%d)" % (aWord, newMinimum)
                if newMinimum < minimumLength:
                    minimumLength = newMinimum
                    if minimumLength == 0:
                        return 1
                        break

    if minimumLength != 0:
        for aWord in addLetter(word):
            newMinimum = aTrie.get(aWord)
            print "add letter = %s(%d)" % (aWord, newMinimum)
            if newMinimum < minimumLength:
                minimumLength = newMinimum
                if minimumLength == 0:
                    return 1
                    break

    if minimumLength != 0:
        for aWord in swapLetter(word):
            newMinimum = aTrie.get(aWord)
            print "swap letter = %s(%d)" % (aWord, newMinimum)
            if newMinimum < minimumLength:
                minimumLength = newMinimum
                if minimumLength == 0:
                    return 1
                    break
    return minimumLength
#    elif int(minimum) == 0:
#        print "aaa=", minimum

def addLetter(word):
    wordsWithNewLetter = []
    for aLetter in xrange(1, len(word)+1):
        for letter in string.ascii_lowercase:
            wordsWithNewLetter.append(word[0:aLetter]+letter+word[aLetter:])
    return wordsWithNewLetter 
    
def removeLetter(word):
    wordsWithoutALetter = []
    for aLetter in xrange(1, len(word)+1):
        wordsWithoutALetter.append(word[0:aLetter-1]+word[aLetter:])
    return wordsWithoutALetter 

def swapLetter(word):
    wordsWithSwappedLetters = []
    for firstLetter in xrange(0, len(word)):
        for secondLetter in xrange(firstLetter+1, len(word)):
            newWord = word[0:firstLetter] + \
                word[secondLetter] + \
                word[firstLetter+1:secondLetter] + \
                word[firstLetter] + \
                word[secondLetter+1:]
            wordsWithSwappedLetters.append(newWord)
    return wordsWithSwappedLetters

if __name__ == "__main__":
   
    allWords = Trie('')
    fisier = open('/var/tmp/twl.txt')
#    fisier = open('/var/tmp/twl06.txt')
    cuvinteCitite=0
    for cuvant in fisier:
        allWords.add(cuvant.strip().lower())
        cuvinteCitite += 1
    fisier.close()
    print "cuvinteCitite = %d " % cuvinteCitite

    # read input file
    
    #debug
    while True:
        word = raw_input("word [xxx] to exit: ")
        if word == "xxx":
            break
        
        processWord = word.strip().lower()
        minimumForWord = getMinimumValue(allWords, processWord) #
        print "Minimum for [%s] was [%d]" % (processWord, minimumForWord)

