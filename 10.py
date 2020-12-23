def part_1(adapters):
    adapters.append(0)
    adapters.sort()
    differences = [adapters[i + 1] - x for i, x in enumerate(adapters[:-1])]
    # +1 for the difference to the device
    return differences.count(1) * (differences.count(3) + 1)


def part_2(adapters):
    # Requires that part_1() ran before because the adapters must be sorted
    # and they must include 0.
    possibilities = {adapters[-1]: 1}
    for a in reversed(adapters[:-1]):
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a+1, a+2, a+3))
    return possibilities[0]

with open("C:/Users/Andu/Desktop/aoc/10.txt") as file:
    challenge_input = [int(x) for x in file.read().splitlines()]
print(part_1(challenge_input))  # 2760
print(part_2(challenge_input))  # 13816758796288