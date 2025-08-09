divide_number = []

for _ in range(10):
    numbers = int(input())
    divide_number.append(numbers%42)

print(len(set(divide_number)))