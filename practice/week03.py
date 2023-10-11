

# id() 변수가 알고 있는 값의 위치 찾기

a = 1
print(a, id(a))

b = 1
print(b, id(b))

a = 1.1
print(a, id(a))

a = "인하"
print(a, id(a))


print(3 + 2) # 5
print(3 * 2) # 6
print(3 / 2) # 1.5 
print(3 // 2) # 1
print(3 % 2) # 1
print(3 ** 2) # 9


reg_number = "030101-3123123"

print(reg_number[0:2]) # 연도출력
print(reg_number[2:4]) # 월 출력
print(reg_number[4:6]) # 일 출력
print(reg_number[8]) # 성별 출력(인덱스)

my_school = "inha"

length = len(my_school)
print(length)

print(my_school[0])
print(my_school[1:len(my_school)])