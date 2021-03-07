def LCM(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            return greater
            break
        greater += 1
print(LCM(6, 10))
print(LCM(2, 3))
