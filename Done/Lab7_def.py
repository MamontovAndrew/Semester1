n = int(input("Введите число элементов списка\n"))
arr = []
sums_of_elements = []
for i in range(n):
    arr.append(input("Введите {}-й элемент\n".format(i + 1)))
    sum_of_element = 0
    for j in arr[i]:
        if j.isdecimal():
            sum_of_element += int(j)
    sums_of_elements.append(sum_of_element)
print("Элемент с наибольшей суммой цифр: ", arr[sums_of_elements.index(max(sums_of_elements))])