import utils
from day_03_inputs import wires, traverse_tests, traverse_tests_2


@utils.timer
def traverse_wires(wire_a, wire_b, return_manhattan=True):
    # extract path (in x, y coordinates) from wires
    path_a = extract_path_from_wire(wire_a)
    path_b = extract_path_from_wire(wire_b)

    intersections = []  # for manhattan distance
    detailed_intersections = []  # for steps total

    for line_a, line_b, path_steps in segment_generator(path_a, path_b):
        exists, coords = check_for_intersection(line_a, line_b)
        if exists:
            if return_manhattan:
                # use tuple() for extraction in min(sum()...list-comp) below
                intersections.append(tuple(coords))
            else:
                idx_a, idx_b = path_steps
                pre_intersection_coords = path_a[idx_a], path_b[idx_b]
                detailed_intersections.append(
                    (path_steps, pre_intersection_coords, coords))

    if return_manhattan:
        return min([sum([abs(x), abs(y)]) for x, y in intersections])
    else:
        return find_least_steps(detailed_intersections, wire_a, wire_b)


def extract_path_from_wire(wire, origin=[0, 0]):
    path = [origin]

    # append coordinates for each direction in inputs
    for direction in wire:
        next_coords = get_next_coords(path[-1], direction)
        path.append(next_coords)

    return path


def get_next_coords(coords, direction):
    next_coords = coords.copy()
    direction, distance = direction[0], int(direction[1:])

    # x-axis [0] / y-axis [1]
    change_pos = 0 if direction in {"R", "L"} else 1
    # positive / negative axis movement
    multiplier = 1 if direction in {"U", "R"} else -1

    next_coords[change_pos] = next_coords[change_pos] + (distance * multiplier)
    return next_coords


def segment_generator(path_a, path_b):
    for idx_a in range(0, len(path_a) - 1):
        line_a = [path_a[idx_a], path_a[idx_a + 1]]

        for idx_b in range(0, len(path_b) - 1):
            line_b = [path_b[idx_b], path_b[idx_b + 1]]

            path_steps = idx_a, idx_b  # used for step counting / non-manhattan
            yield line_a, line_b, path_steps


def check_for_intersection(line_a, line_b):
    exists = False
    coords = [None, None]

    # sp = static position, r = range
    sp_a, ra_start, ra_end = static_pos_and_range(*line_a)
    sp_b, rb_start, rb_end = static_pos_and_range(*line_b)

    # if both static positions are equal, they are parallel / no intersection
    if sp_a == sp_b:
        return exists, coords

    static_val_a = line_a[0][sp_a]
    static_val_b = line_b[0][sp_b]

    # check if static value of line is within the other line's range
    a_in_b_range = rb_start <= static_val_a <= rb_end
    b_in_a_range = ra_start <= static_val_b <= ra_end

    # if both are true, the line intersects at the two static values
    exists = a_in_b_range and b_in_a_range
    # place the values with the relative static position
    coords[sp_a] = static_val_a
    coords[sp_b] = static_val_b

    # the origin does not count as an intersection
    if coords == [0, 0]:
        exists = False

    return exists, coords


def static_pos_and_range(coord_a, coord_b):
    # set static and range list positions
    if coord_a[0] == coord_b[0]:
        static_pos, r_pos = 0, 1
    elif coord_a[1] == coord_b[1]:  # this could probably be 'else'
        static_pos, r_pos = 1, 0

    # set range start and end values
    r = [coord_a[r_pos], coord_b[r_pos]]
    r_start = min(r)
    r_end = max(r)

    return static_pos, r_start, r_end


def find_least_steps(detailed_intersections, wire_a, wire_b):
    least_steps = None

    # int_coords, int as in abbr for intersection
    for steps, pres, int_coords in detailed_intersections:
        step_a, step_b = steps  # direction-steps up to intersection
        pre_a, pre_b = pres  # coordinates before intersection

        wire_a_steps = count_steps(wire_a, step_a, pre_a, int_coords)
        wire_b_steps = count_steps(wire_b, step_b, pre_b, int_coords)

        total_steps = wire_a_steps + wire_b_steps

        if least_steps is None:
            least_steps = total_steps
        else:
            least_steps = min(least_steps, total_steps)

    return least_steps


def count_steps(wire, steps, pre_coords, int_coords):
    total = 0

    # add the integer values from the wire-directions
    for idx in range(0, steps):
        direction = wire[idx]
        total += int(direction[1:])

    x1 = pre_coords[0]
    y1 = pre_coords[1]
    x2 = int_coords[0]
    y2 = int_coords[1]

    # add the difference between the pre-intersection coords and
    #   intersection coords
    total += (max(x1, x2) - min(x1, x2)) + (max(y1, y2) - min(y1, y2))
    return total


def test_traverse_wires():
    print("---Testing manhattan distance...---")
    for test, answer in traverse_tests:
        wire_a, wire_b = test
        assert traverse_wires(wire_a, wire_b) == answer
    print("---Test over---\n")


def test_traverse_wires_2():
    print("---Testing steps distance...---")
    for test, answer in traverse_tests_2:
        wire_a, wire_b = test
        assert traverse_wires(wire_a, wire_b, return_manhattan=False) == answer
    print("---Test over---\n")


test_traverse_wires()
test_traverse_wires_2()

wire_a, wire_b = wires
# Part 1 Time: ~0.17 seconds
print(traverse_wires(wire_a, wire_b))  # 2180
# Part 2 Time: ~0.14 seconds
print(traverse_wires(wire_a, wire_b, return_manhattan=False))  # 112316
