#!/usr/bin/env python3

def solve(data: list[str]) -> int:
    solution = []

    # part one
    number_of_zeros = 0
    starting_value = 50

    for rotation in data:
        direction, value = rotation[0], int(rotation[1:])
        if direction == 'L':
            starting_value = (starting_value - value) % 100
        else:
            starting_value = (starting_value + value) % 100
        if starting_value == 0:
            number_of_zeros += 1

    solution.append(number_of_zeros)

    # part two
    number_of_zeros = 0
    starting_value = 50

    for rotation in data:
        direction, value = rotation[0], int(rotation[1:])
        number_of_zeros += (value // 100)
        value %= 100
        if direction == 'L':
            if starting_value - value <= 0 and starting_value != 0:
                number_of_zeros += 1
            starting_value = (starting_value - value) % 100
        else:
            if starting_value + value >= 100:
                number_of_zeros += 1
            starting_value = (starting_value + value) % 100

    solution.append(number_of_zeros)

    return solution

if __name__ == '__main__':
    with open('input') as f:
        data = f.readlines()
    print(solve(data))
