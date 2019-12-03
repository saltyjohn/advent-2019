from day_03_inputs import wires, traverse_tests
from pprint import pprint


def traverse_wires(wire_a, wire_b, return_manhattan=True):
    # extract paths from wire
    wire_a_path = extract_path_from_wire(wire_a)
    wire_b_path = extract_path_from_wire(wire_b)

    intersections = []
    detailed_intersections = []

    # check each line segment from wire_a with all segments from wire_b
    for idx_a in range(0, len(wire_a_path) - 1):
        wire_a_line = [wire_a_path[idx_a], wire_a_path[idx_a + 1]]
        for idx_b in range(0, len(wire_b_path) - 1):
            wire_b_line = [wire_b_path[idx_b], wire_b_path[idx_b + 1]]

            exists, coords = check_for_intersection(wire_a_line, wire_b_line)
            if exists:
                intersections.append(tuple(coords))
                detailed_intersections.append([(idx_a + 1, idx_b + 1), coords])

    if return_manhattan:
        return min([sum([abs(x), abs(y)]) for x, y in intersections])
    else:
        print(detailed_intersections)


def extract_path_from_wire(wire, origin=[0, 0]):
    path = [origin]
    for direction in wire:
        new_coords = get_next_coords(path[-1], direction)
        path.append(new_coords)

    return path


def get_next_coords(coords: list, direction):
    coords = coords.copy()
    direction, distance = direction[0], int(direction[1:])

    # x-axis / y-axis
    change_pos = 0 if direction in {"R", "L"} else 1
    # positive / negative axis movement
    multiplier = 1 if direction in {"U", "R"} else -1

    coords[change_pos] = coords[change_pos] + (distance * multiplier)
    return coords


def check_for_intersection(line_a, line_b):
    exists = False
    coords = [None, None]

    sp_a, ra_start, ra_end = static_pos_and_range(*line_a)
    sp_b, rb_start, rb_end = static_pos_and_range(*line_b)

    # if both static positions are equal, they are parallel / no intersection
    if sp_a == sp_b:
        return exists, coords

    static_val_a = line_a[0][sp_a]
    static_val_b = line_b[0][sp_b]

    # check if static values are within of other's range
    a_in_b_range = rb_start <= static_val_a <= rb_end
    b_in_a_range = ra_start <= static_val_b <= ra_end

    # if both are true, the line intersects at the two static values
    exists = a_in_b_range and b_in_a_range
    coords[sp_a] = static_val_a
    coords[sp_b] = static_val_b

    # the origin does not count as and intersection
    if coords == [0, 0]:
        exists = False

    return exists, coords


def static_pos_and_range(coord_a, coord_b):
    if coord_a[0] == coord_b[0]:
        static_pos, r_pos = 0, 1
    elif coord_a[1] == coord_b[1]:
        static_pos, r_pos = 1, 0

    r = [coord_a[r_pos], coord_b[r_pos]]
    r_start = min(r)
    r_end = max(r)
    return static_pos, r_start, r_end


def test_traverse_wires():
    for test, answer in traverse_tests:
        wire_a, wire_b = test
        assert traverse_wires(wire_a, wire_b) == answer


test_traverse_wires()
wire_a, wire_b = wires
print(traverse_wires(wire_a, wire_b))  # 2180
# pprint(traverse_wires(wire_a, wire_b, return_manhattan=False))
