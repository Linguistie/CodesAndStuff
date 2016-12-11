m=[1,2,3,'kek',0.23]
print (m)
m1="lel lol"
m2=list(m1)
print(m2)
m3=[1,2,"heh",[2,"s"]]
print(m3)
# c 0 до 9
m4=[2*i for i in range(10)]
print(m4)
print(m4[0])
print(m4[-1])
print(len(m4))
#
#
#
#
#Считает сколько елементов и отнимает -1
print(m4[len(m4)-1])
a="kek lel hah"
m4[0]=a
print(m4)
m5=m4[2:5]
print(m5)
m5=m4[7:10]
print(m5)
m5=m4[7:11]
print(m5)
m5=m4[-3:]
print(m5)
m6=[228,"k"]
m4.extend(m6)
print(m4)
m4.insert(1, -5)
print(m4)
m4[2:2]=['KEKNUTSA', "HEHEHEHE"]
print(m4)
m7=[1,2,3,4,5,6,7,8]
m8=['kek','mek','zek']
m9=m7+m8
print(m9)
#
#
#
# Удаление елемента .pop()
#
m9.pop(0)
print(m9)
m9.remove("mek")
print(m9)
m9[0:2]=[]
print(m9)
del m9[3]
print(m9)
m9[1:3]=[-1,-1,-2,-3,-4,-2,-1,-5]
print(m9)
#
#True если присутствует в списке (in)
#
b3=-5 in m9
b4=-6 in m9
print(b3)
print(b4)
#
#
# Возвращает индекс значения
b5=m4.index(8)
print(b5)
#считает количество значений в каком-то списке
b6=m9.count(-1)
print(b6)
#obratnaja storona
m9.reverse()
print(m9)
#функция разворота (создаем лист вывернув готовый список)
m10=list(reversed(m9))
print(m10)
n1=[1,3,2,3,2,4,5,4,3,2,1]
n1.sort()
print(n1)
n1.sort(reverse=True)
print(n1)


