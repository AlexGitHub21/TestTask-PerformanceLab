import sys

numbers_file = sys.argv[1]
with open(numbers_file, 'r') as f2:
    numbers = []
    for line in f2:
        num = int(line.strip())
        numbers.append(num)

sums = []
for num in numbers:
    summa = 0
    for i in range(len(numbers)):
        if numbers[i] != num:
            summa += abs(num - numbers[i])
            if summa > 20:
                break
    else:
        sums.append(summa)

if sums:
    print(min(sums))
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")


