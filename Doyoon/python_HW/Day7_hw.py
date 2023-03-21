def Find_the_common_factor_of_two_numbers(x, y):
    common_factor = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            common_factor.append(i)
    return sorted(common_factor)


print(Find_the_common_factor_of_two_numbers(12, 18))
