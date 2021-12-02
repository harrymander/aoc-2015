import sys


def look_and_say(number):
    new_number = ''
    current = number[0]
    count = 1
    for d in number[1:]:
        if d == current:
            count += 1
        else:
            new_number += str(count) + current
            current = d
            count = 1
    return new_number + str(count) + current


if __name__ == '__main__':
    number = sys.argv[1]
    for i in range(1, 51):
        number = look_and_say(number)
        if i in (40, 50):
            print(len(number))
