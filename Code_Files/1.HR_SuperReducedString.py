def superReducedString(s):
    i = 0
    j = 1
    s = list(s)
    if len(s) == 2:
        if s[0] == s[1]:
            return 'Empty String'
        else:
            return s[0] + s[1]
    else:

        while len(s) > 0 and i < len(s) and j < len(s):
            if s[i] == s[j]:
                del s[i]
                del s[i]
                i, j = 0, 1
            else:
                i += 1
                j += 1

        if len(s) == 0:
            return ' Empty String'

    return ''.join(i for i in s)


lst = input()
print(superReducedString(lst))