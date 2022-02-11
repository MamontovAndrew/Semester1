# Текстовый редактор
# Мамонтов Андрей ИУ7-11Б

txt = list('''аб аб аб аб аб аб аб аб аб 
419/12/0Лежанье 419/12/0у Ильи Ильича 192*48 не было ни необходимостью, как у больного или как у человека
, который хочет спать, ни случайностью, как у того, кто устал, ни наслаждением, как у лентяя: это было его нормальным состоянием. Когда
 он был дома — а он был почти всегда дома, — он все лежал, и все постоянно в одной комнате, где мы его нашли, служившей ему спальней, 
178 * 48 кабинетом и приемной. У него было еще три комнаты, но он редко туда заглядывал, утром разве, и то не всякий день,
 когда человек мёл кабинет его, чего всякий день не делалось. В тех комнатах мебель закрыта была чехлами, 234/123
 шторы спущены. Комната, где лежал Илья Ильич, с первого взгляда казалась прекрасно убранною. Там стояло бюро красного
дерева, два дивана, обитые шелковою 74*38 материею, красивые ширмы с вышитыми небывалыми в природе птицами и плодами. Были там шелковые
 занавесы, ковры, несколько картин, бронза, фарфор и множество красивых мелочей.
 когда
 
ааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа'''.split("\n"))


# Вывод текста
def print_text(txt):
    for i in txt:
        print(i)


# Вычисление выражений умножения и деления
def calculation():
    signs = ["*", "/"]
    numbers_signs_dot_and_space = ["*", ".", " ", "/"] + list(str(i) for i in range(0, 10))
    for i in range(len(txt)):
        j = 0
        while j < len(txt[i]):
            if txt[i][j] in signs:
                expression = ""
                l = 0
                r = len(txt[i])
                count = j - 1
                while (txt[i][count] in numbers_signs_dot_and_space) and (count >= l):
                    expression = txt[i][count] + expression
                    count -= 1
                if expression[0] == " ":
                    expression = expression[1:]
                count = j
                while (count < r) and (txt[i][count] in numbers_signs_dot_and_space):
                    expression += txt[i][count]
                    count += 1
                if expression[len(expression) - 1] == " ":
                    expression = expression[:len(expression) - 1]
                expression_copy = expression
                expression = expression.replace(" ", "")
                arr = []
                k = 0
                while k < len(expression):
                    if expression[k] in signs:
                        arr.append(expression[:k])
                        arr.append(expression[k])
                        expression = expression[k + 1:]
                        k = 0
                    k += 1
                arr.append(expression)
                res = 1
                mode = ""
                a = 1
                for k in range(len(arr)):
                    if arr[k] in signs:
                        mode = arr[k]
                    else:
                        if res == 1:
                            res = float(arr[k])
                        else:
                            a = float(arr[k])
                    if mode == "/" and k % 2 == 0:
                        if a != 0:
                            res /= float(a)
                        else:
                            res = "INF"
                            break
                    elif mode == "*" and k % 2 == 0:
                        res *= float(a)
                length = len(txt[i])
                txt[i] = txt[i].replace(expression_copy, str(res))
                j -= length - len(txt[i])
            j += 1
    print_text(txt)


# Удаление/замена всех вхождений
def delete_change_all_occurrences(word, new_word):
    length = len(word)
    for i in range(len(txt)):
        j = 0
        while j < len(txt[i]) - length + 1:
            if txt[i][j:j + length].lower() == word.lower():
                flag1 = False
                flag2 = False
                if j == 0:
                    flag1 = True
                    first = 0
                else:
                    first = j
                    flag1 = not txt[i][j - 1].isalpha()
                if len(txt[i]) == j + length:
                    flag2 = True
                    last = len(txt[i])
                else:
                    flag2 = not txt[i][j + length].isalpha()
                    last = j + length
                if flag1 and flag2:
                    txt[i] = txt[i][:first] + new_word + txt[i][last:]
                else:
                    j += 1
            else:
                j += 1
    print_text(txt)


# Привязка текста к левой / правой стороне / по ширине
def text_alignment(mode):
    match mode:
        case "left":
            ind = "zero_string"
            for i in range(len(txt)):
                line_copy = txt[i].replace("  ", " ")
                while line_copy != txt[i]:
                    txt[i] = line_copy
                    line_copy = txt[i].replace("  ", " ")
                for j in range(len(txt[i])):
                    if txt[i][j] != " ":
                        ind = j
                        break
                if ind != "zero_string":
                    txt[i] = txt[i][ind:]
            print_text(txt)
        case "right":
            ind = "zero_string"
            for i in range(len(txt)):
                line_copy = txt[i].replace("  ", " ")
                while line_copy != txt[i]:
                    txt[i] = line_copy
                    line_copy = txt[i].replace("  ", " ")
                for j in range(len(txt[i]) - 1, 0, -1):
                    if txt[i][j] != " ":
                        ind = j
                        break
                if ind != "zero_string":
                    txt[i] = txt[i][:ind + 1]
            longest = len(max(txt, key=len))
            for i in range(len(txt)):
                txt[i] = " " * (longest - len(txt[i])) + txt[i]
            print_text(txt)
        case "width":
            for i in range(len(txt)):
                ind1 = 0
                ind2 = len(txt[i])
                for j in range(len(txt[i])):
                    if txt[i][j] != " ":
                        ind1 = j
                        break
                for j in range(len(txt[i]) - 1, 0, -1):
                    if txt[i][j] != " ":
                        ind2 = j
                        break
                txt[i] = txt[i][ind1:ind2 + 1]
            longest = len(max(txt, key=len))
            for i in range(len(txt)):
                t = longest - len(txt[i])
                spaces = txt[i].count(" ")
                if spaces == 0:
                    format_string = "{:^" + str(longest) + "s}"
                    txt[i] = format_string.format(txt[i])
                    continue
                if t // spaces > 0:
                    txt[i] = txt[i].replace(" ", " " * (t // spaces + 1))
                t = t - t // spaces * spaces
                txt[i] = txt[i].replace(" ", "  ", t)
            print_text(txt)
        case _:
            pass


# Поиск предложения с максимальным количеством слов с чередующимися гласными/согласными
def sentence_with_max_words():
    vowels = "АОУИЭЫЕЁЮЯаоуиэыеёюя"
    letters = [chr(i) for i in range(192, 256)]
    sentences = []
    sentence = ""
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j] != ".":
                sentence += txt[i][j]
            else:
                sentence += txt[i][j]
                if j == 0:
                    if not txt[i][1].isdigit():
                        sentences.append(sentence)
                        sentence = ""
                else:
                    if not txt[i][j - 1].isdigit():
                        sentences.append(sentence)
                        sentence = ""
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
    number_of_words = [0 for i in range(len(sentences))]
    for i in range(len(sentences)):
        words = []
        flag = False
        index = 0
        j = 0
        while j < len(sentences[i]):
            if sentences[i][j].isalpha() and not flag:
                flag = True
                index = j
            elif not sentences[i][j].isalpha() and flag:
                flag = False
                words.append(sentences[i][index:j])
                index = j
            elif j == len(sentences[i]) - 1 and flag:
                j += 1
                words.append(sentences[i][index:j])
            j += 1
        for j in words:
            flag = True
            for k in range(1, len(j)):
                if not ((j[k] in vowels and (not j[k - 1] in vowels and j[k - 1] in letters)) or ((j[k] in letters and not j[k] in vowels) and j[k - 1] in vowels)):
                    flag = False
                    break
            if flag and len(j) > 1:
                number_of_words[i] += 1
    maximum_ind = number_of_words.index(max(number_of_words))
    print("Количество слов с чередующимися гласными/согласными: ", max(number_of_words))
    print("Предложение с максимальным количеством слов с чередующимися гласными/согласными: ", sentences[maximum_ind])


# Меню и основная программа
while True:
    print("""    Меню:
    1. Выровнять текст по левому краю
    2. Выровнять текст по правому краю
    3. Выровнять текст по ширине
    4. Удаление всех вхождений заданного слова
    5. Замена одного слова другим во всём тексте
    6. Вычисление арифметических выражений c операциями умножения/деления внутри текста
    7. Найти предложение с максимальным количеством слов, в которых гласные чередуются с согласными.
    8. Выйти из программы
    Введите номер команды: """, end="")
    option = input()
    match option:
        case "1":
            text_alignment("left")
        case "2":
            text_alignment("right")
        case "3":
            text_alignment("width")
        case "4":
            word = input("Введите слово, которое необходимо удалить: ")
            delete_change_all_occurrences(word, "")
        case "5":
            word = input("Введите слово, которое необходимо заменить: ")
            new_word = input("Введите слово, которое необходимо подставить вместо старого: ")
            delete_change_all_occurrences(word, new_word)
        case "6":
            calculation()
        case "7":
            sentence_with_max_words()
        case "8":
            exit()
        case _:
            print("Вы ввели неправильный номер команды, попробуйте еще раз")
