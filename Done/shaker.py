def bubble_sort_one_iteration(l, r, step, arr):
    for i in range(l, r, step):
        if step == 1:
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
        else:
            if arr[i] < arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
    return arr


arr = list(map(int, input("Введите элементы массива, который нужно отсортировать, через пробел: ").split()))
l = 0
r = len(arr) - 1
while l <= r:
    prev_arr = arr.copy()
    arr = bubble_sort_one_iteration(l, r, 1, arr)
    if prev_arr == arr:
        break
    r -= 1
    prev_arr = arr.copy()
    arr = bubble_sort_one_iteration(r, l, -1, arr)
    if prev_arr == arr:
        break
    l += 1
    print(arr)
print("Отсортированный массив: ", *arr)
