##Write your code here, return the answer don't print
def quadruplets(arr, x):
    pass








n= int(input())
arr= list(map(int, input().split()))
x =int(input())
final_ans= quadruplets(arr, x)
for i in range(len(final_ans)):
    for j in range(4):
        print(final_ans[i][j],end=" ")
    print(" ")
