a = int(input('Введите число столбцов: '))
b = int(input('Введите число строк: '))
print('матрица {}x{}'.format(a, b))

if a != b:
    number_of_rows = max(a,b)
    number_of_cols = min(a,b)
else:
    number_of_rows = a
    number_of_cols = b

i=0
sum=0
while i<=(number_of_cols-1) :
    sum = sum + (number_of_cols-i)*(number_of_rows-i)
    i+=1

print('всего {} квадратов'.format(sum))

