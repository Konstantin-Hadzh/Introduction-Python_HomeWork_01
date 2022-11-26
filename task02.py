"""
   2) Пользователь вводит время в секундах. Переведите время в часы, 
   минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование 
   строк
"""

user_interval_sec = int(input("Введите значение интервала в секундах: "))
clock = user_interval_sec // 3600
min = (user_interval_sec % 3600) // 60
sec = user_interval_sec % 3600 % 60
print(f"{clock}:{min}:{sec}")