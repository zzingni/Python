
a = 1   # 리터럴로 표시, 약식 표현
a1 = int(1)  # 생성자로 값을 표현(정식)

b = 1.1
b1 = float(1.1)

c = "1"
c1 = str("1")

print(type(a), type(a1), a==a1)  # <class 'int'> <class 'int'> True
print(type(b), type(b1), a==a1)  # <class 'float'> <class 'float'> True
print(type(c), type(c1), a==a1)  # <class 'str'> <class 'str'> True

print(1+1)

# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요","저의","이름은","윤인성입니다!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다. ")
print("===확인 전용선---")
print()
print()
print("---확인전용선---")