N = int(input())
power = list(map(int, input().split()))

MOD = int(1e9) + 7
count = 0
frequency = {}

for p in power:
    complement = (1 << (p.bit_length())) - p
    if complement in frequency:
        count += frequency[complement]
    frequency[p] = frequency.get(p, 0) + 1

print(count % MOD)
