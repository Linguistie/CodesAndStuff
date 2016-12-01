print("Servus!")
print()
print()


sentence1="Sentence one"
sentence2='Sentence two'
sentence3="Sentence'three"
sentence4='Sentence"four'
sentence5=("SENTENCE( '' '' '' )FIVE")
miniText=[sentence1,sentence2,sentence3,sentence4,sentence5]
numberOfSentences=len(miniText)
print("Number of sentences: ", numberOfSentences)
for currentSentence in miniText:
    numberOfCharacters=0
    for character in currentSentence:
        numberOfCharacters+=1
        numberOfWords=0
        for word in currentSentence.split():
            numberOfWords+=1
    average=float(numberOfCharacters/numberOfWords)
    print(currentSentence)
    print("Number of words: ",numberOfWords)
    print("Number of characters: ",numberOfCharacters)
    print("Average: this sentence has about %s characters per word"%average)
    print()
    
##sentence=sentence1.rstrip('.')
##for word in sentence.split():
##    numberOfWords+=1
##    for character in word:
##        numberOfCharacters+=1
##average=float(numberOfCharacters/numberOfWords)




print()
print("Servus!")
