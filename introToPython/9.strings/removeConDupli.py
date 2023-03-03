

#code is contributed by Lokesh Poluru Velayudham
from sys import stdin

def removeConsecutiveDuplicates(string) :
    i = 0
    j = 0

    newSt = ""
    while(j<len(string)):
        if(string[i] == string[j]):
            j+=1
        elif((string[j] != string[i]) or (j==len(string)-1)):
            newSt += string[i]
            i = j
            j+=1
    newSt += string[j-1]
    return newSt
    # if len(string) < 2:
    #     return string
    # if string[0] != string[1]:
    #     return string[0]+removeConsecutiveDuplicates(string[1::])
    # return removeConsecutiveDuplicates(string[1::])
	# # Your code goes here






#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)


