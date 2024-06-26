def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    result = 0

    while number != 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        result += 1

    return result
