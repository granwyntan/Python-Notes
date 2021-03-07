def HCF(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            return i
print(HCF(6, 27))
print(HCF(24, 36))
print(HCF(6969, 11))
