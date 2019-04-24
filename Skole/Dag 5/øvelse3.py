numlines = 0
numwords = 0 
numchars = 0
with open("text.txt", "r") as f:
    for line in f:
        
        wordlist = line.split()
        numlines += 1
        numwords += len(wordlist)
        numchars += len(line)

print("number of lines", numlines)
print("number of words", numwords)
print("number of chars", numchars)