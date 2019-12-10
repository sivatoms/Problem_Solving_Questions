
def marsExploration(s):
    n = len(s)//3
    s1 = list(('SOS') * n)
    counter = 0
    for i in range(len(s)):
        if s[i] != s1[i]:
            counter += 1

    return counter


if __name__ == '__main__':
    s = input()
    print(marsExploration(s))


# input
# SOSSPSSQSSOR

# output
# 3