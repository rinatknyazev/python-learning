# Листинг 4.3. Операции с множествами cтр 180
# Создание множества
A = {2 * k + 1 for k in range(5)}
B = {2 * k for k in range(5)}
C = {2 * k + 1 for k in range(3, 8)}
# Содержимое множеств:
print("Созданы множества: ")
print("A: ", A)
print("B: ", B)
print("C: ", C)
# Объединение множеств:
print("Объединение множеств: ")
print(f'A|B = {A.union(B)}')
print(f'B|A = {B.union(A)}')
print(f'C|A = {A|C}')
# Пересечние множеств:
print(f'Пересечение множеств:')
print(f'A&B = {A.intersection(B)}')
print(f'A&C = {A&C}')
# Разность множеств
print(f'Разность множеств:')
print(f'A-C= {A-C}')
print(f'C-A = {C.difference(A)}')
# Симметрическая разность множеств
print (f'Симметрическая разность множеств:')
print(f'A ^ C = {A^C}')
print(f'C^A = {C.symmetric_difference(A)}')
# Исходные множества:
print(f'Исходные мноежества:')
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')
