
#code is contributed by Lokesh Poluru Velayudham


def reverseword(string):
   string1 = string.split(" ")
   string2 = [i[::-1] for i in string1]
   string3 = " ".join(string2)
   return string3


# Driver's Code
string = input()
print(reverseword(string))
