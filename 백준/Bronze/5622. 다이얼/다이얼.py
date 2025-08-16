dial = [' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabets = input()
result = 0

for i in range (len(alphabets)):
    for j in range (len(dial)):
        if alphabets[i] in dial[j]:
            result = result + dial.index(dial[j])+2

print(result)