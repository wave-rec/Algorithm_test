A, B = map(int, input().split())

rock = 2
scissor = 1
paper = 3

if A == rock and B == scissor:
    print('A')
elif A == paper and B == rock:
    print('A')
elif A == scissor and B == paper:
    print('A')
else:
    print('B')