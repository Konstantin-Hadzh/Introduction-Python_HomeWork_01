""" 
    4) Пользователь вводит целое положительное число. Найдите самую большую
    цифру в числе. Для решения используйте цикл while и арифметические 
    операции 
"""

user_num = int(input("Введите целое положительное число: "))
print(f"Максимальная цифра в {user_num}")
num_max = user_num % 10 # находим последнюю цифру в user_num, получаемeю путем деления на 10 с остатком
user_num = user_num // 10 # удаляем последнюю цифру user_num делением на 10
while user_num > 0: # цикл работает до тех пор, пока user_num >0
    if user_num % 10 > num_max: # на каждой итерации в user_num удаляется последняя цифра
        num_max = user_num % 10
    user_num = user_num // 10
print(f"равна {num_max}")