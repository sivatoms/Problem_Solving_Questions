
def hackerrankInString(s):
    t = list('hackerrank')
    flag = False
    if all(i for i in s if i in t):
        s = ''.join(r for r in s if r in t)
        flag = True
    result = ''
    if not flag:
        return 'NO'
    else:
        i = 0
        j = 0
        while j < len(s) and i < len(t):
            if t[i] == s[j]:
                result += s[j]
                i += 1
            j += 1

        if result == 'hackerrank':
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        print(hackerrankInString(input()))



# input
# 2
# hereiamstackerrank
# hackerworld

# output
# YES
# NO