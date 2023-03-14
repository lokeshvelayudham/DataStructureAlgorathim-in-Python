#code is contributed by Lokesh Poluru Velayudham

def maximumProfit(arr):
	arr.sort()
	# print(arr)
	arr1 = []
	for i in range(len(arr)):
		arr2 = arr[i]*(len(arr)-i)
		arr1.append(arr2)
		# arrN = [int(ele) for ele in arr1]
	# print(arr1)
	return max(arr1)
	#Implement Your Function here
	pass

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)