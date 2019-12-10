from  string import ascii_uppercase, ascii_lowercase
def caesarCipher(s, k):
    u = list(ascii_uppercase)
    l = list(ascii_lowercase)
    if k in (26, 52, 78):
        k = 26
    elif k < 26:
        k = k
    elif k > 26 and k < 52:
        k = k - 26
    elif k > 52 and k < 78:
        k = k - 52
    elif k > 78 and k <= 100:
        k = k - 78


    tail_u = u[:k]
    head_u = [u[i] for i in range(k, len(u))]
    encr_u = head_u + tail_u
    tail_l = l[:k]
    head_l = [l[i] for i in range(k, len(l))]
    result = ''
    encr_l = head_l + tail_l
    import re
    for i in range(len(s)):
        if re.search(r'[a-zA-Z]', s[i]):
            if s[i] in encr_u:
                result += encr_u[u.index(s[i])]
            else:
                result += encr_l[l.index(s[i])]

            result += s[i]
        #print(alpha.index(s[i]), encr)
    return result
if __name__ == '__main__':
    n = int(input())
    s = input()
    r = int(input())
    print(caesarCipher(s, r))

# input
# 12
# Hello_World!
# 4

# output
# Lipps_Asvph!

