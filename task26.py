#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def GetValueByUser(Num):
    while True:
        getnum = input(Num)
        if getnum.isdigit():
            return getnum

def NumberDegree (FirstNumber, SecondNumber):
    if SecondNumber == 1:
        return FirstNumber
    else:
        return (FirstNumber * NumberDegree(FirstNumber, SecondNumber - 1))

A = int(GetValueByUser('Введите число A (положительное): '))
B = int(GetValueByUser('Введите число B (положительное): '))
print(NumberDegree(A,B))
