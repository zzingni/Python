

max_value = 0
a = 0
b = 0

for i in range(1,100):
    j = 100 - i
    if j * i > max_value:
        a = j
        b = i
        max_value = j * i
print(f"최대가 되는 경우: {a} * {b} = {max_value}")