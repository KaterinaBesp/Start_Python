""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
Вывод: 0 """



 
N = int(input("Введите размер списка: "))
spam = list(range(-N, N+1))
print(spam)

def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer
 
print(multiply(spam))

