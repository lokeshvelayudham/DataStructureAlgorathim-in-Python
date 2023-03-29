from stackArray import stack 

s = stack()
s.push(12)
s.push(13)
s.push(14)

s.push(22)
while s.isEmpty() is False :
    print(s.pop())

s.top() 