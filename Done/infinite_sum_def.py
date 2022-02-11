#1 + x / 1! + 2x / 2! + 3x / 3!.... + nx/n!
x = float(input("Введите X\n"))
accuracy = float(input("Введите точность, с которой нужно вычислить сумму ряда\n"))
if accuracy <= 0.0:
    print("Точность задана неверно")
    exit()
factorial = 1
iteration = 1
current_state = 1
while abs(iteration * x / factorial) > accuracy:
    factorial *= iteration
    current_state += iteration * x / factorial
    iteration += 1
print("Сумма бесконечного ряда: {:.25g}".format(current_state))