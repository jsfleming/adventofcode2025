#!/usr/bin/env python3

def solve(data: list[str]) -> list[int]:
    solution = []
    # part 1
    sum = 0
    for id in data:
        first, last = map(int, id.split('-'))
        for i in range(first, last+1):
            candidate = str(i)
            if len(candidate) % 2 == 0:
                mid = len(candidate) // 2
                if candidate[:mid] == candidate[mid:]:
                    sum += i
    solution.append(sum)

    # part 2
    sum = 0
    for id in data:
        first, last = map(int, id.split('-'))
        for i in range(first, last+1):
            candidate = str(i)
            for n in range(1, len(candidate)):
                if len(candidate) % n != 0:
                    continue
                substrings = [candidate[j:j+n] for j in range(0, len(candidate), n)]
                if len(set(substrings)) == 1:
                    sum += i
                    break

    solution.append(sum)

    return solution

if __name__ == '__main__':
    with open('input') as f:
        data = f.read().split(',')
    print(solve(data))
