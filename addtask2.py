#Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел, сумма цифр которых равна s. 
#Запись натурального числа не может начинаться с цифры 0.
#В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.

def GetValueByUser(Num):
    while True:
        getnum = input(Num)
        if getnum.isdigit():
            return getnum

def SumOfElements(Number):
    Sum = 0
    while Number!=0: 
        Sum = Sum + Number % 10
        Number = Number // 10
    return Sum
    
def GetNewNumber(Number):
    Value = 1
    while Number!=0:
        Value = Value*10
        Number = Number - 1
    return Value - 1

def CountSame (FirstNumber, SecondNumer):
    if FirstNumber == SecondNumer: return 1
    else: return 0
    
NewCount = 0
K = int(GetValueByUser('Введите число К: '))
S = int(GetValueByUser('Введите число S: '))

Number = GetNewNumber (K)
Stop = Number // 10

while Number != Stop:
    NewCount = NewCount + CountSame(SumOfElements(Number), S) 
    Number = Number - 1

print('Существует',NewCount, K,'-значных чисел, cумма которых равна',S)