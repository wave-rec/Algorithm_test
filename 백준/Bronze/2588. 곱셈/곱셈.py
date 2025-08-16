N = int(input())
M = input()
M_list = []
for i in M:
    M_list.append(i)


first = N*int(M_list[2])
second = N*int(M_list[1])
third = N*int(M_list[0])


print(first)
print(second)
print(third)
print(first + second*10 + third*100)