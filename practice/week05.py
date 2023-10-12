
name = input("이름:")
age = int(input("나이:"))

data1 = 41.56789
data2 = 50.0
print(data1, data2)
print(f"{data1:.2f}")
print(f"{data2:g}")

# 방법 3 : f-문자열(str)
data = f"{name}의 나이는 {age}살 입니다."
print(data)

# 방법 2 : format()메소드 이용

data = "{0}의 나이는 {1}살 입니다. {0}은 학생입니다.".format(name,age)
print(data)

data = "{1}의 나이는 {0}살 입니다.".format(name, age)
print(data)

data = "{}의 나이는 {}살 입니다.".format(name, age)
print(data)

# 방법 1 : 전통적인 파이썬 동적 문자열 생성
data = "%s의 나이는 %d살입니다." %(name, age) # 원하는 대로 띄어쓰기 실행 가능
print(data)

# + 연산자 이용
data = "이름:" + name + "나이:" + str(age)
print(data) # 이름:권지은나이:23 > 다 붙어서 출력됨

# print()로 나열하는 방법
print("이름:",name,"나이:",age) # 이름: 권지은 나이 : 23 > ,로 연결하면 공백(space) 발생