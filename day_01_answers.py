from day_01_inputs import vals
import utils


def basic_fuel_estimator(mass):
    return (mass // 3) - 2


def adv_fuel_estimator(mass, total=0):
    added_fuel = basic_fuel_estimator(mass)
    total += added_fuel

    # only a fuel-mass of 9 or greater will contribute to more fuel:
    #   --> (9 // 3) - 2 = 1
    #   --> (8 // 3) - 2 = 0
    if added_fuel > 8:
        return adv_fuel_estimator(mass=added_fuel, total=total)

    return total


@utils.timing
def total_fuel(vals, func):
    return sum([func(i) for i in vals])


# time=0.0
part_1_answer = total_fuel(vals, func=basic_fuel_estimator)
print(f'Part 1: {part_1_answer}')  # 3394032

# time=0.0009982585906982422
part_2_answer = total_fuel(vals, func=adv_fuel_estimator)
print(f'Part 2: {part_2_answer}')  # 5088176
