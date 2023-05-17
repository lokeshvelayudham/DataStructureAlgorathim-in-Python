def check_substrings(s):
    # Check if "AB" appears before "BA"
    if 'AB' in s:
        idx = s.index('AB')
        if 'BA' in s[idx+2:]:
            return "YES"

    # Check if "BA" appears before "AB"
    if 'BA' in s:
        idx = s.index('BA')
        if 'AB' in s[idx+2:]:
            return "YES"

    return "NO"

# Input string
s = input()

# Check if substrings "AB" and "BA" exist
result = check_substrings(s)
print(result)
