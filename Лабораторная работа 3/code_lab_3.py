print("Servus!\n")


def f_load():
    #Файл для чтения внизу
    fileForReading=open('txt_r.txt','r',encoding="utf8")
    #Информацию из открытого файла перекидуем в переменную, указаную ниже
    StorageForTextFromReading=fileForReading.read()
    StorageForTextFromReading=StorageForTextFromReading.replace(". ", ".")
    fileForReading.close()
##    print(StorageForTextFromReading)
##    print("_____________________________")
    return(StorageForTextFromReading)

def f_load_t():
    #Файл для чтения внизу
    fileForReading=open('txt_r_t.txt','r',encoding="utf8")
    #Информацию из открытого файла перекидуем в переменную, указаную ниже
    StorageForTextFromReading_t=fileForReading.read()
    StorageForTextFromReading_t=StorageForTextFromReading_t.replace(". ", ".")
    fileForReading.close()
##    print(StorageForTextFromReading_t)
##    print("_____________________________")
    return(StorageForTextFromReading_t)

def f_process(StorageForTextFromReading,StorageForTextFromReading_t):
    fileForWriting=open('txt_w.txt',"w",encoding="utf8")
    fileForWriting.write("Слова, использованые в переводе: \n\n")
    LIST_1=[]
    LIST_2=[]
    for slovo in StorageForTextFromReading.split(","):
        if slovo==".":break
        LIST_1.append(slovo)
##        print(slovo)
##    print(LIST_1)
##    print("_____________________________")
    for slovo in StorageForTextFromReading.split("+"):
        LIST_2.append(slovo)
##        print(slovo)
    del LIST_2[0]
##    print(LIST_2)
##    print("+++++++++++++++++++++++++++++")
    SLOVAR=dict(zip(LIST_1,LIST_2))
##    print(SLOVAR)
    StorageForTextFromReading_t=StorageForTextFromReading_t.replace(",", " ")
    StorageForTextFromReading_t=StorageForTextFromReading_t.replace(".", " ")
    NEW_SLOVAR=[]
    for slovo in StorageForTextFromReading_t.split(" "):
        NEW_SLOVAR.append(slovo)
    i=0
##    print(NEW_SLOVAR)
    ko=0
    for i in NEW_SLOVAR: 
        if i in SLOVAR:
            ko+=1
            i=i.rstrip('.') 
            print(i, '-', SLOVAR[i])
            a1=str(i)
            a2=str(SLOVAR[i])
            fileForWriting.write(a1)
            fileForWriting.write(":")
            fileForWriting.write(a2)
            fileForWriting.write("\n")
    a10=" ".join(NEW_SLOVAR)
    print("\nОбрабатываемый текст:")
    print(a10)
    fileForWriting.write("\nОбрабатываемый текст:")
    fileForWriting.write(a10)
    me=0
    him=0
    her=0
    it=0
    print()
    for i in NEW_SLOVAR:
        if i == "me":
            me+=1
    print("\n\nКоличество местоимений me: ",me)
    fileForWriting.write("\nКоличество местоимений me: ")
    a3=str(me)
    fileForWriting.write(a3)
    for i in NEW_SLOVAR:
        if i == "him":
            him+=1
    print("Количество местоимений him: ",him)
    a4=str(him)
    fileForWriting.write("\nКоличество местоимений him: ")
    fileForWriting.write(a4)
    for i in NEW_SLOVAR:
        if i == "her":
            her+=1
    print("Количество местоимений her: ",her)
    a5=str(her)
    fileForWriting.write("\nКоличество местоимений her: ")
    fileForWriting.write(a5)
    for i in NEW_SLOVAR:
        if i == "it":
            it+=1
    print("Количество местоимений it: ",it)
    a6=str(it)
    fileForWriting.write("\nКоличество местоимений it: ")
    fileForWriting.write(a6)
    print("\nКоличество переведенных слов: ",ko)
    a7=str(ko)
    fileForWriting.write("\n\nКоличество переведенных слов: ")
    fileForWriting.write(a7)
    NEW_SLOVAR.sort()
    print(NEW_SLOVAR)
    fileForWriting.write("\n\nСлова текста в алфавитном порядке:\n\n")
    a8=" ,".join(NEW_SLOVAR)
    fileForWriting.write(a8)
    kek=str(input("Введите слово для удаления (Оставить пустым при нежелании): "))
    print(kek)
    for i in list(SLOVAR):
        if kek==i:
            SLOVAR.pop(kek)
    print("_______",SLOVAR)
    VALUE=str(input("Введите слово для добавления (англ): "))
    KEY=str(input("Введите перевод введенного слова (рус): "))
##  ПОЧЕМУ-ТО ВЫДАЕТ ИМЕННО ИМЯ ПЕРЕМЕННОЙ В ПЕРЕВОД, А НЕ ЕЁ СОДЕРЖАНИЕ    
    SLOVAR[KEY] = VALUE
    print("\n",SLOVAR)
       
a=f_load()
b=f_load_t()
f_process(a,b)


print("\nServus!")
