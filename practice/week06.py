

infos = {
    "123" : ["김인하", 22],
    "124" : ["김인하", 21]
}

print("학생 검색 시스템")

while True:
    number = input("학번: ")
    if number in infos:
        print(f"이름:{infos[number][0]}")
    else:
        print("그런 애 없다.")

    yesorno = input("계속할래?(y,n) ")
    if yesorno.upper() != "Y":
        break
# 학번 일치 불일치 상관없이 한 차례 검사 후 계속할지 물어보기

while True:
    number = input("학번: ")
    if number in infos:
        print(f"이름:{infos[number][0]}")
        break
    else:
        yesorno = input("계속할래>(y,n) ")
        if yesorno.upper() == "Y":
            continue
        else:
            break
# 학번이 일치하지 않을 때 계속할지 물어보기

while True:
    number = input("학번: ")
    if not number in infos:
        continue
    print(f"이름:{infos[number][0]}")
    break
# 학번이 일치하지 않으면 continue로 계속 조건검사
# 일치하면 출력하고 break


while True:
    number = input("학번: ")
    if number in infos.keys():
        print(f"이름:{infos[number][0]}")
        break
    else:
        pass
    print("학번 다시 입력해야해")
# 학번이 일치하면 이름 출력하고 종료
# 불일치시 계속 학번 입력받기

fruits = ["딸기", "굴", "키위", "키위", "키위", "복숭아"]

target = "키위"
while target in fruits: # in 연산자
    fruits.remove(target)
print(fruits)

i = 0
while i < len(fruits):
    print(f"{i+1} 순위 {fruits[i]}")
    i += 1 # python에서는 i++ 안됨.
print()