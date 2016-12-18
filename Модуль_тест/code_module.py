import re
a=open('initial.txt','r',encoding="utf8")
storage=a.read()
print("Содержимое initial.txt:",storage)
b=open('result.txt','w')

# # Задание 1
print('Пятый символ строки:',storage[4:5])
b.write(storage[4:5])
b.write("\n")
print('Предпоследний и последний символ строки:',storage[-2:-1], storage[-1])
b.write("\n")
b.write(storage[-2:-1])
b.write(storage[-1])
print('Первые 3 символа строки:',storage[0:3])
b.write("\n")
b.write(storage[0:3])
print('Все, без последних трех символов:',storage[:-3])
b.write("\n")
b.write(storage[:-3])
print('Все с четными идндексами:',storage[1::2])
b.write("\n")
b.write(storage[1::2])
print('Все с нечетными идндексами:',storage[::2])
b.write("\n")
b.write(storage[::2])
print('Все в обратном порядке:',storage[::-1])
b.write("\n")
b.write(storage[::-1])
print('Все в обратном порядке через 1 с предпоследнего:',storage[-2:0:-2])
b.write("\n")
b.write(storage[-2:0:-2])
print('Длина строки исходного файла:',len(storage))
o=str(len(storage))
b.write("\n")
b.write(o)
storagev2=storage.replace(",","")
storagev3=storagev2.replace(".","")
storagev4=storagev3.replace("!","")
storagev5=storagev4.replace(" ","")
storagev6=storagev5.replace(":","")
storagev7=storagev6.replace(";","")
storagev8=storagev7.replace("?","")
storagev9=storagev8.replace("'","")
storagev10=storagev9.replace('"',"")
print('Кол-во символов в исходном файле без знаков препинания:',len(storagev10))
O=str(len(storagev10))
b.write(O)
#
# # Задание 2
def func1():
    Input=input("Введите предложение:")
    a=0
    for i in Input.split(' '):
        print(i[0].upper(),end="")
        print(i[1:-1],end="")
        print(i[-1].upper(),end=" ")
        b.write("\n")
        b.write(i)
    return()
a=func1()

# Задание 3
n=0
LIST=[]
N=int(input("Введите количество слов, которое вы хотите ввести (без контрольного слова):"))
while n!=N:
    a=""
    a=str(input("Введите слово:"))
    if len(a)>0:
        LIST.append(len(a))
    n+=1
B=input("Введите контрольное слово:")
Blen=len(B)
c=0
for i in LIST:
    if Blen == i:
        c+=1
if c>0:print("Количество слов имеющих длину идентичную длине ключевого слова:", c)
if c>0:b.write("\n")
J=str(c)
if c>0:b.write(J)
else:
    print("Слов, имеющих длину соответствующую длине ключевого слова не найдено!")
    b.write("\n")
    b.write("No words of matching length found")
b.write("\n")
c=str(c)
b.write(c)

# Задание 4
a=input("Введите строку:")
LEST=[]
for i in a.split(" "):
    LEST.append(i)
print("Исходная строка:",a)
LEST[0], LEST[-1] = LEST[-1], LEST[0]
c=" ".join(LEST)
print("Преобразованная строка:",c)
b.write("\n")
b.write(c)

#Задание 5
a=input("Введите строку:")
A=0
for i in a:
    if A==0:
        if i=="f":
            print("Индекс первого вхождения f:",a.index(i))
            P=str(a.index(i))
            b.write("\n")
            b.write(P)
            A+=1
    if i=='f':
        A+=1
if A>=3:print("Результат: 'f' встречается более 1го раза!")
if A==2:print("Результат: -1")
if A==0:print("Результат: -2")
if A>=3:b.write("\nResult: 'f' appears more than a time!\n")
if A==2:b.write("\nResult: -1\n")
if A==0:b.write("\nResult: -2\n")

#Задание 6
a=input("Введите строку:")
A=0
B=0
for i in a:
    if i=="h":A+=1
for i in a:
    if i=="h":B+=1
    if B==0:
        continue
    else:
        a=list(a)
        a.pop(a.index(i))
        if B==A:
            break
a="".join(a)
print(a)
b.write(a)

#Задание 7
a=input("Введите строку:")
a=re.sub("2","два",a)
print(a)
b.write(a)

#Задание 8
a=input("Введите строку:")
LIST=[]
for i in a:
    LIST.append(i)
c=int(input("Введите индекс между какими двумя символами втсавить '!'"))
LIST.insert(c,"!")
print("Полученая строка:",LIST)
print(a)
b.write(a)

#Задание 9
a=input("Введите строку:")
LIST=[]
for i in a:
    if a.index(i)%2==0:
        LIST.append(i)
a="".join(LIST)
print("Полученая строка:",a)
b.write(a)