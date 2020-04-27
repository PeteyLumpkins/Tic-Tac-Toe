numbers = '0123456789'
cmds = {'/exit':(False, 'Bye!'), '/help':(True, f'This program prints the sum or difference of a set of numbers')}


def check_input(value):  # checks user input, returns string
    value_split = value.split(" ")
    if value == "":
        return 'empty'
    elif value[0] == '/':
        return 'cmd'
    elif value_split[0] in numbers and len(value_split) == 1:
        return 'num'
    else:
        return 'continue'


def format_input(input_string): # takes user input, formats it
    new_str = input_string.split(" ")
    str_list = [char for char in new_str if char != '']
    return " ".join(str_list)


def sum_nums(number_list):  # can handle addition and subtraction of list of nums
    total = int(number_list[0])
    i = 1
    while i < len(number_list):
        if '-' in number_list[i] and len(number_list[i]) % 2 != 0:
            total -= int(number_list[i + 1])
        else:
            total += int(number_list[i + 1])
        i += 2
    return total


def __main__():  # main method
    run = True
    while run:
        value = format_input(input())
        check = check_input(value)
        if check == 'cmd':
            if cmds.get(value):
                print(cmds[value][1])
                run = cmds[value][0]
            else:
                print('Unknown command')
            continue
        elif check == 'empty':
            continue
        elif check == 'num':
            print(value)
        elif check == 'continue':
            try:
                print(sum_nums(value.split(" ")))
            except ValueError:
                print(f'Invalid expression')
            except IndexError:
                print(f'Invalid expression')



__main__()