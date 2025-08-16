text = input()
croatia_arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_arr:
    text = text.replace(i, '*') 

print(len(text))