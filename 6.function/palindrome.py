
def checkPalindrome(num):
    temp = num
    rev = 0
    while(num > 0):
        dig = num % 10
        rev = rev*10+dig
        num = num//10
    return(temp == rev)
#Implement Your Code Here
pass
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
