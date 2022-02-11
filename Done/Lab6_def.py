n = int(input("Введите длину списка\n"))
arr = []
for i in range(n):
    print("Введите {}-й элемент".format(i + 1))
    arr.append(float(input()))
average = sum(arr) / len(arr)
elem = float(input("Введите элемент, который будет стоять в массиве после первого числа больше ср. ар.\n"))
for i in range(n):
    if arr[i] > average:
        arr.insert(i + 1, elem)
        break
print(arr)