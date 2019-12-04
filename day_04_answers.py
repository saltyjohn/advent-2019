def is_inc_with_exception_of_adj_euqal_or_equilvalence(num):
    string = str(num)
    is_inc = True
    for i in range(0, len(string) - 1):
        a = string[i]
        b = string[i + 1]
        if a < b and check_has_only_one_equal_adj(string):
            is_inc = False

    return is_inc


def check_has_only_one_equal_adj(num):
    string = str(num)
    found = False
    for i in range(0, len(string) - 1):
        s_val_1 = string[i]
        s_val_2 = string[i + 1]
        vals_is_equal = s_val_1 == s_val_2
        if not found and vals_is_equal:
            found = True
        elif found and vals_is_equal:
            return False
    return found


def test():
    tests = [(111111, True), (223450, False), (123789, False)]
    for test, answer in tests:
        is_inc = is_inc_with_exception_of_adj_euqal_or_equilvalence(test)
        one_equal = check_has_only_one_equal_adj(test)
        assert (is_inc and one_equal) == answer


def main():
    for i in range(264360, 746325 + 1):
        a = check_has_only_one_equal_adj(i)
        b = is_inc_with_exception_of_adj_euqal_or_equilvalence(i)
        if a and b:
            return i


main()
