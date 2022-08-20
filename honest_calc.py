# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
messages = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def read_calc():
    calc = input(msg_0 + "\n")
    calc = calc.strip().split(" ")
    return calc


def calc_sum(x, y):
    return x + y


def calc_sub(x, y):
    return x - y


def calc_mult(x, y):
    return x * y


def calc_div(x, y):
    if y == 0:
        print(msg_3)
    else:
        return x / y


def is_one_digit(digit):
    if digit.is_integer() and -10 < digit < 10:
        return True
    else:
        return False


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if x == 1 or y == 1:
        msg += msg_7
    if x == 0 or y == 0 and oper in ['*', '+', '-']:
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def confirm_save(result):
    if is_one_digit(result):
        msg_index = 10
        while msg_index <= 12:
            answer = input(messages[msg_index] + '\n')
            if answer == 'y':
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    return True
            elif answer == 'n':
                return False
            else:
                continue
    else:
        return True


def parse_num(str_, memory):
    try:
        if str_ == 'M':
            num = memory
        else:
            num = float(str_)
        return num
    except ValueError:
        print(msg_1)
        return None


def parse_numbers(x, y, memory):
    return parse_num(x, memory), parse_num(y, memory)


def save_result():
    save = input(msg_4 + "\n").lower()
    if save == 'y':
        return True
    elif save == 'n':
        return False
    else:
        return save_result()


def do_proceed():
    proceed = input(msg_5 + "\n").lower()
    if proceed == 'y':
        return True
    elif proceed == 'n':
        return False
    else:
        return do_proceed()


def calculate():
    memory = 0.0
    while True:
        x, oper, y = read_calc()
        x, y = parse_numbers(x, y, memory)
        if x is None or y is None:
            continue

        if oper in ['+', '-', '*', '/']:
            check(x, y, oper)
            if oper == "+":
                result = calc_sum(x, y)
            elif oper == "-":
                result = calc_sub(x, y)
            elif oper == "*":
                result = calc_mult(x, y)
            elif oper == "/":
                result = calc_div(x, y)
            else:
                print(msg_2)
                continue

        if result is not None:
            print(result)

            if save_result():
                if confirm_save(result):
                    memory = result
            if do_proceed():
                continue
            else:
                break


calculate()
