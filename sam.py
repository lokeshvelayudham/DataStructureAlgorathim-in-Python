def permutation(str):
    if len(str) == 0:
        return 
    
    output = []
    for i in range(len(str)):
        start = str[i]
        
                
        remaining = str[:i] + str[i+1:]        
        output.append(start + remaining )
        
        # remaining = str[i+1:] + str[:i]
        # output.append(start+remaining)
    return output

string = input()
ans = permutation(string)
# print(ans)
for s in ans:
    print(s)