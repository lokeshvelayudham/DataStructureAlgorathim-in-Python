def subs(s):
    if len(s) == 0:
        output = []
        output.append("")
        return output
    smallerString = s[1:]
    smallOutput = subs(smallerString)

    output = []
    for sub in smallOutput:
        output.append(sub)
    for sub in smallOutput:
        output.append(s[0]+ sub)
    return output

s = input()
ans = subs(s)
for ele in ans:
    print(ele)