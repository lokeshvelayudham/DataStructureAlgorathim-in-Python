#code is contributed by Lokesh Poluru Velayudham

# string = input()
# rev = string[::-1]

# if (rev == string):
#     print(True)
# else:
#     print(False)




# Read input as sepcified in the question
# Print output as specified in the question
def checkPalindrome(st):
    temp = st
    rev = st[-1::-1]
    return(temp == rev)


#Implement Your Code Here
pass

st = input()
isPalindrome = checkPalindrome(st)
if(isPalindrome):
	print('true')
else:
	print('false')
