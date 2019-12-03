from day_03_inputs import wires

wire_a, wire_b = wires


def next_coords(coords: list, path):
    direction, distance = path[0], int(path[1:])

    # x-axis / y-axis
    change_pos = 0 if direction in {'R', 'L'} else 1
    # positive / negative axis movement
    multiplier = 1 if direction in {'U', 'R'} else -1

    coords[change_pos] = distance * multiplier
    return coords


def traverse_wires(wire_a, wire_b):
    a_long = len(wire_a) >= len(wire_b)
    longest_wire = wire_a if a_long else wire_b
    shortest_wire = wire_b if a_long else wire_a

    for l_path in longest_wire:
        pass


def test_next_coords():
    tests = [
        [([0, 0], 'R100'), [100, 0]],
        [([0, 0], 'D5'), [0, -5]],
        [([0, 0], 'L5'), [-5, 0]],
        [([0, 0], 'U31'), [0, 31]],
    ]
    for test, answer in tests:
        origin, path = test
        assert next_coords(origin, path) == answer
    # print('next_coords tests passed')


def test_find_intersection():
    tests = [
        [(['R2', 'U2'], ['U2', 'R2']), (2, 2)],
        [(['R2', 'U3'], ['U2', 'R3']), (2, 2)],
    ]
    for test, answer in tests:
        assert find_intersections(*test) == answer


test_next_coords()
