text = '''
аб аб аб аб аб аб аб аб аб 
419/12/0Лежанье 419/12/0у Ильи Ильича 192*48 не было ни необходимостью, как у больного или как у человека

, который хочет спать, ни случайностью, как у того, кто устал, ни наслаждением, как у лентяя: это было его нормальным состоянием. Когда
 он был дома — а он был почти всегда дома, — он все лежал, и все постоянно в одной комнате, где мы его нашли, служившей ему спальней, 
178 * 48 кабинетом и приемной. У него было еще три комнаты, но он редко туда заглядывал, утром разве, и то не всякий день,

 когда человек мёл кабинет его, чего всякий день не делалось. В тех комнатах мебель закрыта была чехлами, 234/123
 шторы спущены. Комната, где лежал Илья Ильич, с первого взгляда казалась прекрасно убранною. Там стояло бюро красного
дерева, два дивана, обитые шелковою 74*38 материею, красивые ширмы с вышитыми небывалыми в природе птицами и плодами. Были там шелковые
 занавесы, ковры, несколько картин, бронза, фарфор и множество красивых мелочей.'''.split("\n")
max_len_word = ""
sentence_with_max_len_word = ""
sentence = ""
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] != ".":
            sentence += text[i][j]
        else:
            sentence += "."
            word = ""
            for k in sentence:
                if k.isalpha():
                    word += k
                else:
                    if len(word) > len(max_len_word):
                        max_len_word = word
                        sentence_with_max_len_word = sentence
                    word = ""
            sentence = ""
print("Предложение с самым длинным словом:", sentence_with_max_len_word)
print("Слово: {}    Его длина: {}".format(max_len_word, len(max_len_word)))