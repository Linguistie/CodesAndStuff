def Input():
    print("input sentence")
    sentence1=str(input())
    print("Your sentence is:")
    print(sentence1)
    print()
    return(sentence1)
def Body(sentence1):
    sentence=sentence1.rstrip('.')
    numberOfCharacters=0
    numberOfWords=0
    for word in sentence.split():
        numberOfWords+=1
        for character in word:
            numberOfCharacters+=1
    average=float(numberOfCharacters/numberOfWords)
    return(numberOfWords, numberOfCharacters, sentence, average)
def Output(numberOfWords, numberOfCharacters, sentence, average):
    print(sentence)
    print("Number of words:",numberOfWords)
    print("Number of characters:",numberOfCharacters)
    print("Average: this sentence has about %s characters per word"%average)
    return()
sentence1=Input()
numberOfWords, numberOfCharacters, sentence, average=Body(sentence1)
Output(numberOfWords, numberOfCharacters, sentence, average)
