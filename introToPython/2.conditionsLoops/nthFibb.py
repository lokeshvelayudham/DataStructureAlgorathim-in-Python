# Function for nth Fibonacci number
from math import sqrt
n = int(input())
#n = int(m) +1
#print(n)

# To find the n-th Fibonacci Number using formula
# import square-root method from math library


def nthFib(n):
	res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
	# compute the n-th fibonacci number
	print(int(res))
	# format and print the number


# driver code
nthFib(n)

