import math

def count_power_pokemon_couples(power):
    count = 0
    power_counts = {}

    for p in power:
        if p in power_counts:
            power_counts[p] += 1
        else:
            power_counts[p] = 1

    for p in power:
        for i in range(1, 23):
            q = int(math.pow(2, i) - p)
            if q in power_counts and power_counts[q] > 0:
                power_counts[q] -= 1
                count += 1
                break

    return count % (10**9 + 7)


N = int(input())
power = list(map(int, input().split()))


result = count_power_pokemon_couples(power)
print(result)
