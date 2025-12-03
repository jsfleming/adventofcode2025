#!/usr/bin/env python3

def solve(data: list[str]) -> list[int]:
    solution = []

    # part 1
    sum = 0
    for bank in data:
        batteries = list(map(int, list(bank)))
        local_max, next_max, pos, next_pos = 0, 0, 0, 0
        for i in range(len(batteries)):
            if batteries[i] > local_max:
                next_max = local_max
                local_max = batteries[i]
                next_pos = pos
                pos = i

        if pos == len(batteries)-1:
            local_max = next_max
            pos = next_pos

        next_max = 0
        for i in batteries[pos+1:]:
            next_max = max(next_max, i)

        sum += int(str(local_max) + str(next_max))

    solution.append(sum)

    # part 2
    sum = 0
    for t in data:
        batteries = list(map(int, t))
        joltage = ''

        for i in range(12)[::-1]:
            local_max = 0
            pos = 0

            for p, b in enumerate(batteries[:-(i)] if i > 0 else batteries):
                if b > local_max:
                    local_max = b
                    pos = p

            joltage += str(local_max)
            batteries = batteries[pos+1:]

        sum += int(joltage)

    solution.append(sum)

    return solution

if __name__ == '__main__':
    with open('input') as f:
        data = f.read().split('\n')
    print(solve(data))
