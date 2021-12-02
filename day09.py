import itertools
import re
import sys


def parse_locations_distances(lines):
    locations = set()
    distances = {}
    for line in lines:
        matched = re.match(r'(\w+) to (\w+) = (\d+)', line.strip())

        first = matched[1]
        second = matched[2]
        distance = int(matched[3])

        locations.add(first)
        locations.add(second)
        distances[(first, second)] = distance
        distances[(second, first)] = distance

    return tuple(locations), distances


def calc_distance(route, distances):
    return sum(map(distances.get, zip(route[:-1], route[1:])))


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        locations, distances = parse_locations_distances(f.readlines())

    routes = itertools.permutations(locations)
    distances = tuple(calc_distance(r, distances) for r in routes)

    print(min(distances))
    print(max(distances))
