import re
import sys

import numpy as np


GRID_LEN = 1000


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        lines = list(f.readlines())

    parse_re = re.compile(r'(turn on|toggle|turn off) '
                          r'(\d+,\d+) through (\d+,\d+)')

    grid = np.zeros((GRID_LEN, GRID_LEN))
    for line in lines:
        match = parse_re.match(line.strip())
        command = match[1]
        col1, row1 = map(int, match[2].split(','))
        col2, row2 = map(int, match[3].split(','))

        row2 += 1
        col2 += 1

        if command == 'turn on':
            grid[row1:row2, col1:col2] += 1
        elif command == 'turn off':
            grid[row1:row2, col1:col2] -= 1
            grid[row1:row2, col1:col2][grid[row1:row2, col1:col2] < 0] = 0
        elif command == 'toggle':
            grid[row1:row2, col1:col2] += 2
        else:
            raise ValueError(f'invalid command: {command}')

    print(np.sum(grid))
