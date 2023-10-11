

if True:
    pass
print("해야지")

if True:
    print("참")
    print("true")
    if 10 < 100:
        print("맞네!")

if False:
    print("거짓")

print(not True)
print(not False)

print(5 < 10 and 5 < 3) # False
print(5 < 10 or 5 < 3)  # True

print("#" * 30)

a = 2
b = 10

print(a < 5 < 10)   # True
print(a < b < 5)    # False

print(True)
print(False)
print(type(True))

age = int(input("올해 나이: "))
print("내년 나이:", age+1)

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