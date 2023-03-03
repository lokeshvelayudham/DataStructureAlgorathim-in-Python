#code is contributed by Lokesh Poluru Velayudham

#approach 1

# n = input()
# print(n[::-1])

# approach 2

n =int(input())
rev = 0
while n != 0:
    x = n%10
    rev = rev * 10 + x
    n//=10
print(str(rev))