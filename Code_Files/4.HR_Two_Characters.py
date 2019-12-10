def alternate(n, s):

    if n == 2:
        if s[0] != s[1]:
            return 2
        else:
            return 0
    else:
        flag, k = repeat(s)
        from itertools import combinations
        pairs = list(combinations(k, 2))
        i = 0
        max_len = 0
        ln = len(pairs)
        # check all two characters combinations length in a string
        while i < ln:
            if pairs[i][0] != pairs[i][1]:
                temp = ''.join(l2 for l2 in k if l2 in (pairs[i]))
                flag, temp = repeat(temp)
                if not flag:
                    max_len = max(len(temp), max_len)

            i += 1
        return max_len


# check for any consecutive characters
def repeat(k2):
    k = list(k2)
    i, j = 0, 1
    n = len(k2)
    flag = False
    while n > 0 and len(k) > 1 and j < len(k):

        if k[i] == k[j]:
            flag = True
            k = delete(k, k[i])
        i += 1
        j += 1
        n -= 1
    return flag, k


# delete if any consecutive characters are same
def delete(k3, d):
    k4 = list(i for i in k3 if i != d)
    return k4


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(alternate(n, s))


# input
# 28
# asdcbsdcagfsdbgdfanfghbsfdab

# output
# 8


# input
# 106
# muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz

# output
# 6