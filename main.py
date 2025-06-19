
def longestCommonPrefix(strs):
        if not strs:
            return ""

        # Take the first string as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                # If i exceeds current string length or characters don't match
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        return strs[0]

n=int(input('enter how many strings you want to enter '))
l=[]
for i in range(n):
    s=input('enter string ')
    l.append(s)

print(f'longest common prefix of {l} is {longestCommonPrefix(l)}')  # Output: "fl"
