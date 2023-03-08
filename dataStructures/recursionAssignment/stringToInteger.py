#code is contributed by Lokesh Poluru Velayudham


def sttoin(s):
    if (len(s) == 1):
        return ord(s[0]) - ord('0')
    y = sttoin(s[1:])
    x = ord(s[0]) - ord('0')

    x = x * (10**(len(s) - 1)) + y
    return x

s = input()
print(sttoin(s))
