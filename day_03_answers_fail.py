"""
Tests passed, but lots of looping lead to crazy amounts of processing time...
"""

from day_03_inputs import wires, traverse_tests, coords_tests


def get_next_coords(coords: list, direction):
    coords = coords.copy()
    direction, distance = direction[0], int(direction[1:])

    # x-axis / y-axis
    change_pos = 0 if direction in {"R", "L"} else 1
    # positive / negative axis movement
    multiplier = 1 if direction in {"U", "R"} else -1

    coords[change_pos] = coords[change_pos] + (distance * multiplier)
    return coords


def extract_coords_from_path(x1, y1, x2, y2):
    if x1 == x2:
        r_start = min(y1, y2)
        r_stop = max(y1, y2) + 1
        update_pos = 1
        static_pos = 0
        static_val = x1
    else:
        r_start = min(x1, x2)
        r_stop = max(x1, x2) + 1
        update_pos = 0
        static_pos = 1
        static_val = y1

    path_coords = []
    for c in range(r_start, r_stop):
        new_path = [None, None]
        new_path[update_pos] = c
        new_path[static_pos] = static_val
        path_coords.append(new_path)

    return path_coords


def check_for_intersection(coords_a, coords_b):
    coords = [None, None]
    exists = False

    for coord_pair in coords_a:
        if coord_pair in coords_b and coord_pair != [0, 0]:
            exists = True
            coords = coord_pair
            break

    return exists, coords


def traverse_wires(wire_a, wire_b):
    # longest wire, shortest wire
    a_long = len(wire_a) >= len(wire_b)
    l_wire, s_wire = (wire_a, wire_b) if a_long else (wire_b, wire_a)

    # long wire coords 0 & 1
    lc0 = [0, 0]
    lc1 = [0, 0]
    intersections = []

    for l_path in l_wire:
        lc0 = lc1
        lc1 = get_next_coords(lc0, l_path)
        lc_coords = extract_coords_from_path(*lc0, *lc1)

        # had to move these here because they never reset...
        sc0 = [0, 0]
        sc1 = [0, 0]

        for s_path in s_wire:
            sc0 = sc1
            sc1 = get_next_coords(sc0, s_path)
            sc_coords = extract_coords_from_path(*sc0, *sc1)

            exists, coords = check_for_intersection(lc_coords, sc_coords)
            if exists:
                intersections.append(tuple(coords))
                break

    reduced_intersections = [
        sum([abs(c1), abs(c2)]) for c1, c2 in intersections
    ]
    return min(reduced_intersections)


def test_get_next_coords():
    for test, answer in coords_tests:
        origin, path = test
        assert get_next_coords(origin, path) == answer


def test_extract_coords_from_path():
    tests = [
        ([0, 0, 0, 2], [[0, 0], [0, 1], [0, 2]]),
        ([0, 0, 0, 3], [[0, 0], [0, 1], [0, 2], [0, 3]]),
        ([1, 0, 1, 3], [[1, 0], [1, 1], [1, 2], [1, 3]]),
    ]
    for test, answer in tests:
        assert extract_coords_from_path(*test) == answer


def test_traverse_wires():
    for test, answer in traverse_tests:
        wire_a, wire_b = test
        # print(traverse_wires(wire_a, wire_b), answer)
        assert traverse_wires(wire_a, wire_b) == answer


test_get_next_coords()
test_extract_coords_from_path()
test_traverse_wires()
wire_a, wire_b = wires
print(traverse_wires(wire_a, wire_b))
