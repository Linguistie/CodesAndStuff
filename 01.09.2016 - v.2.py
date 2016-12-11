print("Servus!")
print()
print()



print("input sentence")
sentence1=str(input())
print("Your sentence is:")
print(sentence1)
print()
sentence=sentence1.rstrip('.')
numberOfCharacters=0
numberOfWords=0
for word in sentence.split():
    numberOfWords+=1
    for character in word:
        numberOfCharacters+=1
average=float(numberOfCharacters/numberOfWords)
print(sentence)
print("Number of words:",numberOfWords)
print("Number of characters:",numberOfCharacters)
print("Average: this sentence has about %s characters per word"%average)



print()
print()
print("Servus!")
