from day_02_inputs import intcode as ic
from day_02_inputs import tests


def update_intcode(ic, add_fix=False, fix_a=12, fix_b=2):
    lic = ic.copy()  # local intcode

    # Restore values in position 1 and 2
    if add_fix:
        lic[1] = fix_a
        lic[2] = fix_b

    # Loop through intcode by opcode positions
    for i in range(0, len(lic), 4):
        if lic[i] == 99:
            break

        idx_a = lic[i + 1]
        idx_b = lic[i + 2]
        update_idx = lic[i + 3]

        if lic[i] == 1:
            lic[update_idx] = lic[idx_a] + lic[idx_b]
        elif lic[i] == 2:
            lic[update_idx] = lic[idx_a] * lic[idx_b]

    return lic


def find_ic_target(target=19690720):
    for a in range(100):
        for b in range(100):
            fixed_opline = update_intcode(ic=ic,
                                          add_fix=True,
                                          fix_a=a,
                                          fix_b=b)

            if fixed_opline[0] == target:
                return 100 * a + b

    return "Target not found."


def test_update_intcode():
    for test_ic, answer in tests:
        assert update_intcode(test_ic) == answer


test_update_intcode()
fixed_intcode = update_intcode(ic=ic, add_fix=True)
print(fixed_intcode[0])  # 310187
print(find_ic_target())  # 8444
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
"""
# --- Part 1, Attempt 1 ---
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
