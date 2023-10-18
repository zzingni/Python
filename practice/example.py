
# 나누어 떨어지는 숫자
# 숫자를 입력하면 그 숫자가 2,3,4,5로 나누어 떨어지는지 확인하고 출력하는 프로그램


while True:
    number = int(input("정수를 입력해주세요: "))
    if type(number) != int:
        print("정수를 입력해주세요!")
    else:
        for i in range(2,6):
            result = number % i
            if result == 0:
                print(f"{number}은 {i}로 나누어 떨어지는 숫자입니다.")
            else:
                print(f"{number}은 {i}로 나누어 떨어지는 숫자가 아닙니다.")
    q = input("계속하시겠습니까?(y,n) ")
    if q.upper() == "Y":
        continue
    else:
        break