import sys
import re
import os
import subprocess




if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <Input text file> <Output file>")
    exit()

inputText = sys.argv[1]
outputText = sys.argv[2]


#Come back to make sure that the files exist and the program



wordTotal = 0
words = {}


with open(inputText, 'r') as inputFile:
    for line in inputFile:

        line = line.strip()

        word = re.split('[ \t]',line)
        #print(word)

        for string in word:
            if string not in words:
                words[string] = 1
            else:
                words[string] +=1
        
        wordTotal+=1

sortedWords = sorted(words.items())

outFile = open("outputText.txt","a")
for word in sortedWords:
    outFile.write(word[0])
    outFile.write(" ")
    outFile.write(str(word[1]))
    outFile.write("\n")
outFile.close()
