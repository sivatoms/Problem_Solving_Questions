def camelcase(s):
    from string import ascii_uppercase
    k = list(ascii_uppercase)
    counter = 1
    for i in list(s):
        if i in k:
            counter += 1
    return counter

if __name__ == '__main__':
    s = input()
    print(camelcase(s))