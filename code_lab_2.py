print("Servus!\n")


def f_load():
    #Файл для чтения внизу
    fileForReading=open('txt_r.txt','r')
    #Информацию из открытого файла перекидуем в переменную, указаную ниже
    StorageForTextFromReading=fileForReading.read()
    StorageForTextFromReading=StorageForTextFromReading.replace(". ", ".")
    fileForReading.close()
    return(StorageForTextFromReading)

def f_process(StorageForTextFromReading):
    fileForWriting=open('txt_w.txt',"w")
    ListForWordAmmountInCurrentSentence=[]
    kol=0
    o=0
    CHARECTERSAMMOUNT=0
    for element in StorageForTextFromReading.split("."):
        if len(element)>1:
            ListForWordAmmountInCurrentSentence.append(element)
        for word in element.split(" "):
            kol+=1

    for i in range(len(ListForWordAmmountInCurrentSentence)):
        KOLVO=0
        o+=1
        for word in ListForWordAmmountInCurrentSentence[i].split():
            KOLVO+=1
        n=str(o)
        m=str(KOLVO)
        print("Количество слов в предложении #%s:"%n, m)
        fileForWriting.write("\nTotal number of words in the sentence#%s: "%n)
        fileForWriting.write(m)
    
##    fileForWriting=open('txt_w.txt',"w")
    print("Состав текстового файла:", StorageForTextFromReading)
    fileForWriting.write("\n\nFile content: \n")
    fileForWriting.write(StorageForTextFromReading)
    fileForWriting.write("\n")
    SummaSimv=0
    SentenceList=[]
    WordList=[]
    SamoeDlinnoeSlovo=0
    a=0
    b=0
    i=0
    LongestWordLen=0
    CurrWord="*N/A*"
##############
    for currentSentence in StorageForTextFromReading.split("."):
        a+=1
        for word in currentSentence.split():
            if len(currentSentence)>1:print("Первое cлово из предложения #%s:"%a, word)
            if len(currentSentence)>1:
                fileForWriting.write("\nSentence #%s: "%a)
                fileForWriting.write(word)
                
            if len(currentSentence)>1:
                if len(word)>LongestWordLen:
                    LongestWordLen=len(word)       
##            print("Слово %s имеет максимальную длинну"%word)
            break
    for currentSentence in StorageForTextFromReading.split("."):
##        print(LongestWordLen)
        for word in currentSentence.split():
            if len(currentSentence)>1:
                if LongestWordLen==len(word):
                    print("Первое слово имеющее максимальную длинну:",word)
                    KO=str(word)
                    fileForWriting.write("\n\nLongest word out of first ones: ")
                    fileForWriting.write(word)
            break
                
##############
    for sentence in StorageForTextFromReading.split("."):
        #Если символов в предложении больше одного, то это предложение добавляется в список
        if len(sentence)>1:SentenceList.append(sentence.split("."))
        for word in sentence.split():
            WordList.append(word.split(" "))
            DannoeKolvoSimv=len(word)
            SummaSimv+=DannoeKolvoSimv
    a=len(SentenceList)
    b=len(WordList)
    c=str(a)
    d=str(b)
    e=str(SummaSimv)
    print("Количество предложений:                               ", c)
    fileForWriting.write("\n\nSentences amount:")
    fileForWriting.write(c)
    print("Общее количество слов:                                ", d)
    fileForWriting.write("\nTotal words amount:")
    fileForWriting.write(d)
##    print("Общее количество символов:                      ", e)
##    fileForWriting.write("\nTotal characters amount:")
##    fileForWriting.write(e)
##    print (SentenceList)
    #join помогает перевести содержимое списка в строку, '' - разделитель между элементами списка соответственно
##    FirstSentenceString=' '.join(SentenceList[0])
##    print(FirstSentenceString)
##    for word in FirstSentenceString.split():
##        DlinnaDannogoSlova=len(word)
##        if DlinnaDannogoSlova>SamoeDlinnoeSlovo:
##            SamoeDlinnoeSlovo=DlinnaDannogoSlova
##    print("Максимальная длинна слова в первом предложении: ",SamoeDlinnoeSlovo)
##    fileForWriting.write("\nMaximum word length of the first sentence:")
##    f=str(SamoeDlinnoeSlovo)
##    fileForWriting.write(f)
##    return()
    
##def f_write(StorageForTextFromReading):
##    #Файл для записи внизу
##    fileForWriting=open('txt_w.txt',"w")
##    fileForWriting.write("File content:")
##    fileForWriting.write(StorageForTextFromReading)
##    fileForWriting.close()
##    return()

    StorageForTextFromReading=''.join(ListForWordAmmountInCurrentSentence)
##    print(ListForWordAmmountInCurrentSentence)
    
    StorageForTextFromReading=StorageForTextFromReading.replace(" ","")
    for word in StorageForTextFromReading.split(" "):
        CHARECTERSAMMOUNT+=1
    print("Количество символов без пробелов и знаков препинания: ", len(StorageForTextFromReading))
    SF=str(len(StorageForTextFromReading))
    fileForWriting.write("\nNumber of sentences with no punctuation marks nor spaces:")
    fileForWriting.write(SF)

a=f_load()
f_process(a)

print("\nServus!")

    
