arr = list(map(int, input().split()))

normal_lst = [1, 2, 3, 4, 5, 6, 7, 8]

if arr == normal_lst:
    print('ascending')
elif arr == sorted(normal_lst, reverse=True):
    print('descending')
else:
    print('mixed')
