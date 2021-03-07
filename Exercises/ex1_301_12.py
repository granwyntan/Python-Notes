N = int(input("Enter value for N: "))
agb = bga = 0
for i in range(N):
    A, B = input("Enter value for A and B separated by a space: ").split()
    A, B = int(A), int(B)
    if A > B: agb += 1
    elif B > A: bga += 1
print("a > b =", agb)
print("b > a =", bga)
