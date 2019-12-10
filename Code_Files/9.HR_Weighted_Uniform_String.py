
def weightedUniformStrings(s):
    from string import ascii_lowercase
    low = ascii_lowercase
    s_dc = set()
    i, j = 0, 1
    while i < len(s):
        score = (low.index(s[i]) + 1)
        if i + 1 != len(s) and s[i + 1] == s[i]:
            j += 1
        else:
            j = 1
        s_dc.add(score * j)
        i += 1

    return s_dc

if __name__ == '__main__':
    s = input().strip()
    q = int(input())
    s = weightedUniformStrings(s)
    print(s)
    for i in range(q):
        print('Yes' if int(input()) in s else 'No')