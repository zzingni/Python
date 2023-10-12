

number = int(input("정수:"))

if number > 0:
    print("양수")

if number < 0:
    print("음수")

if number == 0: # 검사를 3번 하는 코드
    print("0")

raw_input = input("inch 단위의 숫자를 입력해주세요: ")

inch = int(raw_input)
cm = inch * 2.54

print(inch, "inch는 cm 단위로", cm, "cm입니다.")

string ="안녕하세요"
string += "!"
string += "!"
print("string:", string)

int_a = int(52)
int_a1 = int("52")
float_a = float(27.2)
float_a1 = float("27.2")

print(type(int_a), int_a)
print(type(int_a1), int_a1)
print(type(float_a), float_a)
print(type(float_a1), float_a1)