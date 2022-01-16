from module2 import user_input, subtract_numbers, sum_numbers


def sum_and_subtract(a: int, b: int) -> int:
    print(user_input)
    return sum_numbers(a, b) - subtract_numbers(a, b)


print(sum_and_subtract(1, 2))
