print("Servus!\n")


def f_load():
    #Файл для чтения внизу
    fileForReading=open('txt_r.txt','r')
    #Информацию из открытого файла перекидуем в переменную, указаную ниже
    StorageForTextFromReading=fileForReading.read()
    StorageForTextFromReading=StorageForTextFromReading.replace(". ", ".")
    fileForReading.close()
##    print(StorageForTextFromReading)
##    print("_____________________________")
    return(StorageForTextFromReading)

def f_process(StorageForTextFromReading):
    LIST_1=[]
    LIST_2=[]
    for slovo in StorageForTextFromReading.split(","):
        if slovo==".":break
        LIST_1.append(slovo)
##        print(slovo)
    print(LIST_1)
    print("_____________________________")
    for slovo in StorageForTextFromReading.split("+"):
        LIST_2.append(slovo)
##        print(slovo)
    del LIST_2[0]
    print(LIST_2)
    print("+++++++++++++++++++++++++++++")
    SLOVAR=dict(zip(LIST_1,LIST_2))
    print(SLOVAR)



a=f_load()
f_process(a)

print("\nServus!")

    
