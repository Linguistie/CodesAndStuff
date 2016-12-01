#Создание словаря
print("# Создание словаря: Пустой словарь с помощью {}")
d={}
print(d)
##
print("# Создание словаря: Пустой словарь с помощью dict()")
d1=dict()
print(d1)
##
print("# Создание словаря: Заполненый словарь по ключам и значениям")
d2={'one':1,'two':2,'three':3}
print(d2)
##
print("# Создание словаря: Заполненый словарь с функцией dict()")
d3=dict(one=1,two=2,three=3)
print(d3)
##
print("# Создание словаря: Заполненый словарь копированием функцией dict(*словарь*)")
d4=dict(d3)
print(d4)
##
print("# Список кортежей с двумя елементами:")
d5=dict([("one",1),("two",2),("three",3)])
print(d5)
##
print("# Список списоков с двумя елементами:")
d6=dict([["one",1],["two",2],["three",3]])
print(d6)
##
print("# Список кортежей из списков:")
t1=['one','two','three']
t2=[1,2,3]
sp=list(zip(t1,t2))
print(sp)
##
print("# Словарь из списков:")
d7=dict(zip(t1,t2))
print(d7)
##
print("# Последовательный словарь:")
d8={}
d8['one']=1
d8['two']=2
d8['three']=3
print(d8)
##
print("# Словарь с помощью .fromkeys:")
d9=dict.fromkeys(['one','two','three'])
print(d9)
d10=dict.fromkeys(['one','two','three'],1)
print(d10)
print("# Словарь из кортежа ключей:")
d11=dict.fromkeys(('one','two','three'),2)
print(d11)
print("# Групповое присваивание - ссылка на 1 объект:")
d12=d13={'one':1,'two':2,'three':3}
print("d12",d12)
print("d13",d13)
print("Присваивание одного елемента другому словарю")
d13['two']='два'
print(d12,d12)
print(d13,d13)

print("Сылка на разные обьекты")
print("d12 и d13 один и тот же обьект",d12 is d13)

d14,d15={'one':1,'two':2,'three':3},{'one':1,'two':2,'three':3}
print(d14 is d15)
print(d15)
d15['two']='два'
print(d15)
###
print("создание словаря с помощью dict()")
d16={'one':1,'two':2,'three':3}
d17=dict(d16)
print(d16,d17)
print(d16 is d17)
##
print("создание  поверзностного словаря с помощью .copy")
d18={'one':1,'two':2,'three':3}
d19=d18.copy()
print(d19)
print(d19 is d18)
##
d19['two']='два'
print (d19)
print("создание  полной копии словаря с помощью .copy")
d20={'a':1, 'b':[20,30,40]}
d21=dict(d20)
print(d20, d21)
d21['b'][0]='test'
print(d20,d21)
print("создание  полной копии словаря с помощью .deepcopy, module copy")
import copy
d23=copy.deepcopy(d20)
print(d20,d23,d20 is d23)
d23['b'][0]='test'
print(d20,d23,d20 is d23)
##############
print("Операции над словарями")
d24={1:'int','a':"str",(1,2):'tuple'}
print (d24)
print(d24[1])
print(d24['a'])
print(d24[(1,2)])
print("Проверка существования ключа (оператор in)")
d25={'one':1,'two':2,'three':3}
print(d25)
print('ключ''one')
print('ключ существует', 'one' in d25)
##print('ключ zero существует', 'one' in d25)
print('метод .get проверка сущ. ключа')
d26={'a':1,'b':2}
print(d26)
print("ключ 'а'",d26.get("a"))
print("ключ 'c',800",d26.get("c",800))









