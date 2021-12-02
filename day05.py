import re
import sys


def is_nice(s):
    if any(sub in s for sub in ('ab', 'cd', 'pq', 'xy')):
        return False

    if sum(s.count(vowel) for vowel in 'aeiou') < 3:
        return False

    return bool(re.search(r'(.)\1', s))


def is_actually_nice(s):
    if not re.search(r'(.)(.).*?\1\2', s):
        return False
    return bool(re.search(r'(.).\1', s))


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        print(sum(map(int, map(is_nice, f.readlines()))))
    with open(filename) as f:
        print(sum(map(int, map(is_actually_nice, f.readlines()))))
