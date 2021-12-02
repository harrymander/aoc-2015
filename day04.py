import hashlib
import sys


def find_hash_starts_with(startswith, key):
    leading_number = 1
    while True:
        full_key = key + str(leading_number)
        hashhex = hashlib.md5(full_key.encode()).hexdigest()
        if hashhex.startswith(startswith):
            break
        leading_number += 1
    return leading_number


if __name__ == '__main__':
    key = sys.argv[1]

    print(find_hash_starts_with('00000', key))
    print(find_hash_starts_with('000000', key))
