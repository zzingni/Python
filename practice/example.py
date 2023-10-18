

# 간단한 대화 프로그램

import datetime

now = datetime.datetime.now()
hour = now.hour

while True:
    user = input("입력: ")
    if "안녕" in user:
        print("안녕하세요.")
        answer = input("계속 하시겠습니까?(y,n) ")
        if answer.upper() == "Y":
            continue
        else:
            break
    elif "몇 시" in user:
        print(f"지금은 {hour}시입니다.") # print(f{user}) > 오류. f-string은 문자열과 함께 사용해야 쓸 수 없음. 변수명만 쓸 때는 오류.
        answer = input("계속 하시겠습니까?(y,n) ")
        if answer.upper() == "Y":
            continue
        else:
            break
    else:
        print(user)
        answer = input("계속 하시겠습니까?(y,n) ")
        if answer.upper() == "Y":
            continue
        else:
            break


        
