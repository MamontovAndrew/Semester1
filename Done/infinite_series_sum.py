#Программа для вычисления суммы бесконечного ряда 1 + 1 / 2 ** 4 + ... + 1 / n ** 4 с заданной точностью
#с выводом промежуточных значений с заданным шагом и ограничением в заданное кол-во итераций в виде таблицы
#Мамонтов Андрей ИУ7-11Б

#Ввод данных
accuracy = float(input("Введите точность, с которой нужно вычислить сумму ряда\n"))
print_step = int(input("Введите шаг печати\n"))
max_iterations = int(input("Введите максимальное количество итераций\n"))

#Обработка случая, когда шаг меньше 1
if print_step < 1:
    print("Шаг задан неверно")
    exit()

#Обработка случая, когда точность меньше или равна 0
if accuracy <= 0.0:
    print("Точность задана неверно")
    exit()

#Вывод "шапки" таблицы
header = "|" + "{:^32}".format("№ итерации") + "|" + "{:^32}".format("t") + "|" + "{:^32}".format("s") + "|"
print("—" * 100)
print(header)
print("—" * 100)
output = "|" + "{:^32g}".format(1) + "|" + "{:^32g}".format(1) + "|" \
         + "{:^32g}".format(1) + "|"
print(output)

#Обработка случая, когда максимальное число итераций - 1
if max_iterations == 1:
    print("—" * 100)
    print("Сумма бесконечного ряда - 1, вычислена за 1 итерацию.")
    exit()

#Вычисление остальных случаев и вывод таблицы
iteration = 2
current_state = 1.0
while 1 / iteration ** 4 > accuracy and iteration <= max_iterations:
    current_state += 1 / iteration ** 4
    if (iteration - 1) % print_step == 0:
        output = "|" + "{:^32g}".format(iteration) + "|" + "{:^32g}".format(1 / (iteration ** 4)) + "|" \
            + "{:^32.27g}".format(current_state) + "|"
        print(output)
    iteration += 1

if iteration == max_iterations + 1:
    print("—" * 100)
    print("Сумма бесконечного ряда с точностью {} не найдена за {} итерации(-й)".format(accuracy, max_iterations))
else:
    print("—" * 100)
    print("Сумма бесконечного ряда - {}, вычислена за {} итерации(-й).".format(current_state, iteration - 1))