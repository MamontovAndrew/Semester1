def checking_for_integer(s, mode="integer"):
    if mode == "natural":
        if s.isdecimal():
            if int(s) > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        if len(s) >= 2:
            if s[0] == "-":
                s = s[1:]
        if s.isdecimal():
            return True
        else:
            return False

def checking_for_float(s):
    if len(s) == 0:
        return False
    if s[0] == "-":
        s = s[1:]
    if s[len(s) - 1] == "e":
        s += "0"
    if s.count("e") == 1:
        mantissa = s[:s.index("e")]
        exponent = s[s.index("e"):]
        flagmantissa = False
        flagexponent = False
        if exponent[1].isdigit():
            exponent = exponent[1:]
            if exponent.isdecimal():
                flagexponent = True
        else:
            if (exponent.count("+") == 1 or exponent.count("-") == 1) and (exponent[1] == "+" or exponent[1] == "-"):
                exponent = exponent[2:]
                if exponent.isdecimal():
                    flagexponent = True
        if mantissa.count(".") == 1:
            mantissa = mantissa.replace(".", "")
            if mantissa.isdecimal():
                flagmantissa = True
        else:
            if mantissa.isdecimal():
                flagmantissa = True
        if flagmantissa and flagexponent:
            return True
        else:
            return False
    elif s.count("e") == 0:
        if s.count(".") == 1:
            s = s.replace(".", "")
            if s.isdecimal():
                return True
        else:
            if s.isdecimal():
                return True
            else:
                return False
    else:
        return False