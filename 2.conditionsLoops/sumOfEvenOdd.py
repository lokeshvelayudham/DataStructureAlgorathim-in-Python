n = int(input())
li = list(map(int, str(n)))
# print(li)
even = 0
odd = 0
for i in li:
    for j in str(i):
        if int(j) % 2 == 0:
            even += i
        else:
            odd += i
print(even,"",odd)