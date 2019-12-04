def check_has_equal(num):
    string = str(num)
    has_equal = False
    for i in range(0, len(string) - 1):
        val_1, val_2 = int(string[i]), int(string[i + 1])
        if val_1 == val_2:
            has_equal = True
            break
    return has_equal


def check_always_incs_or_equals(num):
    string = str(num)
    always_inc = True
    for i in range(0, len(string) - 1):
        val_1, val_2 = int(string[i]), int(string[i + 1])
        if val_1 > val_2:
            always_inc = False
            break
    return always_inc


def part_1():
    answers = []
    for i in range(264360, 746325 + 1):
        len_is_good = len(str(i)) == 6
        equal = check_has_equal(i)
        inc = check_always_incs_or_equals(i)
        if len_is_good and inc and equal:
            answers.append(i)
    return len(answers)


def test_1():
    tests = [(111111, True), (223450, False), (123789, False)]
    for test_num, answer in tests:
        inc = check_always_incs_or_equals(test_num)
        equal = check_has_equal(test_num)
        assert (inc and equal) == answer


def test_2():
    tests = [(112233, True), (123444, False), (111122, True)]


test_1()
print(part_1())  # 945
