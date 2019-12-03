from day_03_inputs import wires, traverse_tests, traverse_tests_2


def traverse_wires(wire_a, wire_b, return_manhattan=True):
    # extract path (in x, y coordinates) from wires
    path_a = extract_path_from_wire(wire_a)
    path_b = extract_path_from_wire(wire_b)

    intersections = []  # for manhattan distance
    detailed_intersections = []  # for steps total

    # check each line segment from wire_a with all segments from wire_b
    for idx_a in range(0, len(path_a) - 1):
        line_a = [path_a[idx_a], path_a[idx_a + 1]]

        for idx_b in range(0, len(path_b) - 1):
            line_b = [path_b[idx_b], path_b[idx_b + 1]]

            exists, coords = check_for_intersection(line_a, line_b)
            if exists:
                # for manhattan distance
                intersections.append(tuple(coords))

                # for step calculation distance
                pre_intersections = path_a[idx_a], path_b[idx_b]
                path_steps = (idx_a, idx_b)
                detailed_intersections.append(
                    (path_steps, (pre_intersections), coords))

    if return_manhattan:
        return min([sum([abs(x), abs(y)]) for x, y in intersections])

    # calculate total steps
    else:
        least_steps = None

        for steps, pres, coords in detailed_intersections:
            step_a, step_b = steps
            pre_a, pre_b = pres

            wire_a_steps = calculate_steps(wire_a, step_a, pre_a, coords)
            wire_b_steps = calculate_steps(wire_b, step_b, pre_b, coords)

            total_steps = wire_a_steps + wire_b_steps

            if least_steps is None:
                least_steps = total_steps
            else:
                least_steps = min(least_steps, total_steps)

        return least_steps


def calculate_steps(wire, steps, pre_coords, coords_intersection):
    total = 0
    for idx in range(0, steps):
        direction = wire[idx]
        total += int(direction[1:])

    x1 = pre_coords[0]
    y1 = pre_coords[1]
    x2 = coords_intersection[0]
    y2 = coords_intersection[1]

    # add the difference between the pre-intersection coords and
    #   intersection coords
    total += (max(x1, x2) - min(x1, x2)) + (max(y1, y2) - min(y1, y2))
    return total


def extract_path_from_wire(wire, origin=[0, 0]):
    path = [origin]
    for direction in wire:
        new_coords = get_next_coords(path[-1], direction)
        path.append(new_coords)

    return path


def get_next_coords(coords, direction):
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


def test_traverse_wires_2():
    for test, answer in traverse_tests_2:
        wire_a, wire_b = test
        print('Non manhattan:',
              traverse_wires(wire_a, wire_b, return_manhattan=False), answer)
        # assert traverse_wires(wire_a, wire_b, return_manhattan=False) == answer


wire_a, wire_b = wires
# test_traverse_wires()
test_traverse_wires_2()
# print(traverse_wires(wire_a, wire_b))  # 2180
pprint(traverse_wires(wire_a, wire_b, return_manhattan=False))
