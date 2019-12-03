from day_03_inputs import wires, traverse_tests, coords_tests


def next_coords(coords: list, path):
    direction, distance = path[0], int(path[1:])

    # x-axis / y-axis
    change_pos = 0 if direction in {"R", "L"} else 1
    # positive / negative axis movement
    multiplier = 1 if direction in {"U", "R"} else -1

    coords[change_pos] = distance * multiplier
    return coords


def check_for_intersection(l_coord_pair, s_coord_pair):
    pass


def traverse_wires(wire_a, wire_b):
    # longest wire, shortest wire
    a_long = len(wire_a) >= len(wire_b)
    l_wire, s_wire = wire_a, wire_b if a_long else wire_b, wire_a

    # long wire coords 0 & 1, short wire coords 0 & 1
    lc0 = [0, 0]
    lc1 = [0, 0]
    sc0 = [0, 0]
    sc1 = [0, 0]

    for l_path in l_wire:
        lc0 = lc1
        lc1 = next_coords(lc0, l_path)

        for s_path in s_wire:
            sc0 = sc1
            sc1 = next_coords(sc0, s_path)


def test_next_coords():
    for test, answer in coords_tests:
        origin, path = test
        assert next_coords(origin, path) == answer


def test_traverse_wires():
    for test, answer in traverse_tests:
        wire_a, wire_b = test
        assert traverse_wires(*test) == answer


test_next_coords()
wire_a, wire_b = wires
