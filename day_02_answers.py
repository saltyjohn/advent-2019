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
