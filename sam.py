def generatePermutationsHelper(str, l, r, ans):

    # base case
    if (l == r):
        ans.append(str)
        return

    for i in range(l, r + 1):
        # Swapping the characters at position i and l
        str = list(str)
        str[l], str[i] = str[i], str[l]
        str = "".join(str)

        generatePermutationsHelper(str, l + 1, r, ans)

        # backtrack
        str = list(str)
        str[l], str[i] = str[i], str[l]
        str = "".join(str)


def generatePermutations(str):

    # stores the permutations of the string
    ans = []

    l = 0
    r = len(str) - 1

    # call the recursive function
    generatePermutationsHelper(str, l, r, ans)

    # lexicographically increasing order
    ans.sort()

    return ans