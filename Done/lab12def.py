number_of_strings_left = 0
last_string = True
with open("in.txt") as f_in, open("out.txt", "w") as f_out:
    for line in f_in:
        number_of_strings_left += 1
    while number_of_strings_left != 0:
        counter = 0
        f_in.seek(0)
        for line in f_in:
            counter += 1
            if counter == number_of_strings_left:
                if last_string:
                    f_out.write(line + "\n")
                    last_string = False
                elif number_of_strings_left == 1:
                    f_out.write(line[:len(line) - 1])
                else:
                    f_out.write(line)
                break
        number_of_strings_left -= 1
