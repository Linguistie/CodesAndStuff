print("Servus!")
print()
print()



miniText=[]
print("Input your number of sentences: ")
numberOfSentences=int(input())
##numberOfSentences=len(miniText)
print("You have chosen: ", numberOfSentences)
for i in range(numberOfSentences):
##    print("Input a sentence: ")
    newSentence=str(input("Input a sentence: "))
    miniText.append(newSentence)
print("Your sentences:")
for i in range(numberOfSentences):
    print(miniText[i])
    print("Number of sentences:", numberOfSentences)
    print()
for i in miniText:
    numberOfCharacters=0
    numberOfWords=0
    for word in i.split():
        numberOfWords+=1
        for character in word:
            numberOfCharacters+=1

##for currentSentence in miniText:
##    numberOfCharacters=0
##    for character in currentSentence:
##        numberOfCharacters+=1
##        numberOfWords=0
##        for word in currentSentence.split():
##            numberOfWords+=1
            
    average=float(numberOfCharacters/numberOfWords)
    print(i)
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
