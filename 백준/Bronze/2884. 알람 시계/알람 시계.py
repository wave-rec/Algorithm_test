H ,M = map(int, input().split())

if H == 0 and M >= 45:
    print(0, M-45)

elif H == 0 and M < 45:
    print(23, 60-abs(M-45))

elif H != 0 and M >= 45:
    print(H, M-45)

elif H != 0 and M < 45:
    print(H-1, 60-abs(M-45))