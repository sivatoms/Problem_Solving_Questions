def pangrams(s):

    from string import ascii_lowercase,ascii_uppercase, ascii_letters
    l = list(ascii_lowercase)
    u = list(ascii_uppercase)
    l1 = ''
    u1 = ''
    i, j = 0, 0
    n = len(s)
    while n >= 0 and i < len(s):
        if s[i] in l:
            l1 += s[i]

        if s[i] in u:
            u1 += s[i]
        i += 1

        n -= 1

    r1 = u1 + l1
    #print(len(u1), len(l1),)
    if len(set(r1.lower())) == 26:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    s = input()
    print(pangrams(s))

# input
# We promptly judged antique ivory buckles for the next prize

# output
# pangram

# input
# We promptly judged antique ivory buckles for the prize

# output
# not pangram