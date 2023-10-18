

user = int(input("도형 선택(1:사각, 2:삼각, 3:원) : "))

if user == 1:
    x = int(input("가로 입력 :"))
    y = int(input("세로 입력 :"))
    print("도형의 넓이 =", x * y)
elif user == 2:
    x = float(input("밑변 입력 :"))
    y = float(input("높이 입력 :"))
    print(f"도형의 넓이 = {0.5*x*y:.2f}")
elif user == 3:
    x = float(input("반지름 입력 :"))
    print(f"도형의 넓이 = {3.14*(x ** 2):.2f}")
else:
    print("잘못된 입력입니다.")

