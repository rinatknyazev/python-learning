# Листинг 4.2. Генерирование разных случайных чисел
# Количество разных случайных чисел:
from random import *
seed = 33323
count = 10
# Создание пустого множества:
nums = set()
# Генерирование случайных чисел:
while len(nums) < count:
    nums.add(randint(1, count + 15))
print(nums)
