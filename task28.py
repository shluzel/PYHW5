#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def GetValueByUser(Num):
    while True:
        getnum = input(Num)
        if getnum.isdigit():
            return getnum
        
def SumOfNumbers(FirstNumber, SecondNumber):
    if FirstNumber == 0: 
        return SecondNumber
    else:
        return SumOfNumbers(FirstNumber - 1, SecondNumber +1)
    
A = int(GetValueByUser('Введите первое слагаемое (неотрицательное): '))
B = int(GetValueByUser('Введите второе слагаемое (неотрицательное): '))
print(SumOfNumbers(A,B))