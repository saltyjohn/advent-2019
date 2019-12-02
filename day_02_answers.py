from day_02_inputs import intcode as ic
import utils


def read_intcode(ic, add_fix=False, fix_vals=(12, 2)):
    new_ic = ic.copy()
    if add_fix:
        a, b = fix_vals
        new_ic[1] = a
        new_ic[2] = b

    for i in range(0, len(new_ic), 4):
        if new_ic[i] == 99:
            break

        pos_a = new_ic[i + 1]
        pos_b = new_ic[i + 2]
        update_pos = new_ic[i + 3]

        if new_ic[i] == 1:
            new_ic[update_pos] = new_ic[pos_a] + new_ic[pos_b]
        elif new_ic[i] == 2:
            new_ic[update_pos] = new_ic[pos_a] * new_ic[pos_b]

    return new_ic


@utils.timing
def find_ic_target(target=19690720):
    for j in range(100):
        for k in range(100):
            fixed_opline = read_intcode(ic=ic, add_fix=True, fix_vals=(j, k))
            if fixed_opline[0] == target:
                return 100 * j + k


def test_read_intcode():
    tests = [([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40,
               50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
             ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
             ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
             ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
             ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])]

    for test_ic, answer in tests:
        print(read_intcode(test_ic) == answer)


test_read_intcode()

fixed_opline = read_intcode(ic=ic, add_fix=True)
print(fixed_opline[0])
print(find_ic_target())
"""
--- Part 1 Original ---
def read_intcode(inp, pointer=0, add_fix=False):
    if add_fix:
        inp[1] = 12
        inp[2] = 2

    # for i in range(len(inp), step=4):
    if inp[pointer] == 99:
        return inp

    pos_a = inp[pointer + 1]
    pos_b = inp[pointer + 2]
    update_pos = inp[pointer + 3]

    if inp[pointer] == 1:
        inp[update_pos] = inp[pos_a] + inp[pos_b]
    elif inp[pointer] == 2:
        inp[update_pos] = inp[pos_a] * inp[pos_b]
    pointer += 4

    return read_intcode(inp, pointer=pointer)


def test_read_intcode():
    tests = [([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40,
               50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
             ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
             ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
             ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
             ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])]

    for i, answer in tests:
        print(read_intcode(i) == answer)



def find_ic_target(target=19690720):
    for j in range(100):
        for k in range(100):
            fixed_opline = read_intcode(ic=ic, add_fix=True, fix_vals=(j, k))
            if fixed_opline[0] == target:
                return 100 * j + k


fixed_opline = read_intcode(inp=inp, add_fix=True)
print(fixed_opline[0])
print(find_ic_target())
"""
