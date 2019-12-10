
def separateNumbers(s):
    if len(s) == 1 or s[0] == '0':
        print('NO')
    elif len(s) == 2:
        if int(s[1]) - int(s[0]) == 1:
            print('YES', s[0])
        else:
            print('NO')
    else:
        flag = False
        i = 1
        while not flag:
            # keeps the the initial position of the number
            l = []
            # take start of string element as i value increase by 1......n
            k = int(s[:i])
            s2 = ''
            # here increase the k value by 1 each time in the loop below so that that we get a valid beautiful number
            while len(s2) < len(s):
                s2 += str(k)
                k += 1

            l.append(s[:i])

            if s2 == s:
                print('YES', l[len(l)-1])  # here get last element from the list l as an initial element.
                flag = True
            else:
                # loop until half of the string
                # if you go beyond the above the half of the string then they are not beautiful numbers
                if i > len(s)//2:
                    print('NO')
                    flag = True
                else:
                    # increment the element the length to pick from the string
                    i += 1


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)



# input
# 101103

# output
# NO

# input
# 4
# 99910001001
# 7891011
# 9899100
# 999100010001

# output
# YES 999
# YES 7
# YES 98
# NO