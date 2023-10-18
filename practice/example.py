

numbers = [1,2,6,8,4,3,2,1,1,3,7,8,9,5,3,3,2,2,2,3,5,6]
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1 # key값 생성 후 그 값도 +1 해줘야함. else 말고 if 밖에서 +=1 필요!
print(counter)