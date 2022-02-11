import time, random


# Преобразование в двоичную кучу
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Основная функция для сортировки
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = list(map(int, input("Введите массив целых чисел через пробел: ").split()))
heapSort(arr)
print("Отсортированный список: ", *arr)
size1 = int(input("Введите первую размерность: "))
size2 = int(input("Введите вторую размерность: "))
size3 = int(input("Введите третью размерность: "))
ordered_arrays = [list(range(0, size1)), list(range(0, size2)), list(range(0, size3))]
random_arrays = [list(random.randint(-100000, 100000) for i in range(size1)), list(random.randint(-100000, 100000) \
                                                                                   for i in range(size2)),
                 list(random.randint(-100000, 100000) for i in range(size3))]
reversed_ordered_arrays = [ordered_arrays[i][::-1] for i in range(3)]
timing = [[], [], []]
print("-" * 118)
print("|{:^116s}|".format("Пирамидальная сортировка"))
print("-" * 118)
print("|" + "Размерность / Вид списка для исследования" + "|" + "{:^24d}".format(size1) + "|" + "{:^24d}".format(
    size2) + "|" + "{:^24d}".format(size3) + "|")
print("-" * 118)
for i in range(3):
    beginning = time.time()
    heapSort(ordered_arrays[i])
    finish = time.time()
    timing[0].append(finish - beginning)
for i in range(3):
    beginning = time.time()
    heapSort(random_arrays[i])
    finish = time.time()
    timing[1].append(finish - beginning)
for i in range(3):
    beginning = time.time()
    heapSort(reversed_ordered_arrays[i])
    finish = time.time()
    timing[2].append(finish - beginning)
for i in range(3):
    match i:
        case 0:
            print("|" + "{:^41s}".format("Упорядоченный список") + "|", end="")
        case 1:
            print("|" + "{:^41s}".format("Случайный список") + "|", end="")
        case 2:
            print("|" + "{:^41s}".format("Упорядоченный в обратном порядке список") + "|", end="")
    for j in range(3):
        print("{:^24f}".format(timing[i][j]) + "|", end="")
    print("\n" + "-" * 118)
