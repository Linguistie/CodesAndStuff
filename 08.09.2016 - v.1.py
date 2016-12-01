print("Servus!")
print()
print()

text=str(input("Напишите текст: "))
print()
print ("Ваш текст: ", text)
print()
miniText=[]
#sentence - параметр цикла, которая будет менятся, text - из текста, .split - каким путем разделяем.
for sentence in text.split('.'):
    if len(sentence)>0:
#Список.добавить_в_список(выделенное_предложение.разделенное_пробелами)=
        miniText.append(sentence.strip(' '))
numberOfSentences=len(miniText)
print("Ваши %s предложений: "%numberOfSentences)
#Вывод предложений по очереди:
for i in range(numberOfSentences):
    print("Предложение: "+str(i+1)+":")
    print(miniText[i])
print()
wordsOfText=0
sentencesOfText=0
charactersOfText=0
for i in miniText:
    numberOfCharacters=0
    numberOfWords=0
    sentencesOfText+=1
    for word in i.split():
        numberOfWords+=1
        for character in word:
            numberOfCharacters+=1
            charactersOfText=charactersOfText+numberOfCharacters
            wordsOfText=wordsOfText+numberOfWords

    average=float(numberOfCharacters/numberOfWords)
    print("Предложение: "+str(sentencesOfText)+(":"))
    print(i)
    print("Количество слов: ",numberOfWords)
    print("Количество символов: ",numberOfCharacters)
    print("Среднее: в этом тексте около %s символов на слово"%average)
    print()
print("Итог:")
print("Количество предложений в тексте: ", numberOfSentences)
print("Количество слов в тексте: ", wordsOfText)
print("Количество символов в тексте: ", charactersOfText)
averageLen=float(charactersOfText/wordsOfText)
print("В тексте около %s символов на слово" %averageLen)

print()
print()
print("Servus!")
