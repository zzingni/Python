
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[],[],[]]
print(len(output))
for number in numbers:
    output[(number-1) % len(output)].append(number)

print(output)