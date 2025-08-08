numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)

    for max_num in numbers:
        if max_num == max(numbers):
            final_index = numbers.index(max_num) + 1

print(max(numbers))
print(final_index)