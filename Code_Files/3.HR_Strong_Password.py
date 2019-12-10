def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    counter = 0
    if n < 6:
        if any(i in numbers for i in password):
            counter += 1
        if any(i in lower_case for i in password):
            counter += 1
        if any(i in upper_case for i in password):
            counter += 1
        if any(i in special_characters for i in password):
            counter += 1

        if n + (4 - counter) >= 6:
            if counter == 1:
                counter = 3
            elif counter == 2:
                counter = 2
            elif counter == 3:
                counter = 1
        else:
            counter = 6 - ((4-counter) + (n - (4 - counter)))


    elif n >= 6:
        if any(i in numbers for i in password):
            counter += 1
        if any(i in lower_case for i in password):
            counter += 1
        if any(i in upper_case for i in password):
            counter += 1
        if any(i in special_characters for i in password):
            counter += 1
        counter = 4 - counter

    return counter

if __name__ == '__main__':
    n = int(input())
    pas = input()
    print(minimumNumber(n,pas))
