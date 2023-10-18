


fruits = ["딸기", "귤", "키위", "복숭아"]

scores = [10,20,30,20]

print(max(scores))
print(min(scores))

max_score = scores[0]
for i in range(1, len(scores)):
    if max_score < scores[i]:
        max_score = scores[i]
print(max_score)

min_score = scores[0]
for i in range(1, len(scores)):
    if min_score > scores[i]:
        min_score = scores[i]
print(min_score)



for i in reversed(range(len(fruits))):
    print(f"{i+1} 순위 {fruits[i]}")
print() # 순위 내림차순

for i in range(len(fruits)):
    print(f"{i+1} 순위 {fruits[i]}")
print()

# for i in range(5):
#    print(f"{i+1} 순위 {fruits[i]}")
# print()  # list 요소 개수와 i 개수 일치하지 않아 에러 생김


for fruit in fruits:
    print(fruit)
print()

for i in range(5,10,3):
    print(i)

for i in range(1,10):
    print(i)

for i in range(10):
    print(i)

for i in [0,1,2,3,4]:
    print(i)

range_test4 = range(10)
range_test5 = range(2,10)
range_test6 = range(2, 10, 3)
print(range_test4)
print(range_test5)
print(range_test6)



range_test1 = list(range(10))
range_test2 = list(range(2,10))
range_test3 = list(range(2,10,3))

print(range_test1)
print(range_test2)
print(range_test3)

# list = [1,2,3]
# a = list(["Aaaa"])    # 리스트 생성자 사용
# print(a)

# range = range(10)
# print(range. type(range))
