def extract_positive(*numbers):
    return [number for number in numbers if number > 0]

print extract_positive(-1, -2, -3, 10, 20, 30)


def sum_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print sum_all(-1, -2, -3, 10, 20, 30)


def sum_all_positive(*numbers):
    positive = extract_positive(*numbers)
    return sum_all(*positive)

print sum_all_positive(-1, -2, -3, 10, 20, 30)
