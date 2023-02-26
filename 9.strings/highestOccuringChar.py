#code is contributed by Lokesh Poluru Velayudham


from sys import stdin
from collections import Counter


def highestOccuringChar(string):
	count = Counter(string)
	return(max(count, key=count.get))
	#Your code goes here


#main
string = stdin.readline().strip()
ans = highestOccuringChar(string)

print(ans)
