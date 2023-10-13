

infos = {
    "202300001":{"name":"kim inha", "age":21},
    "202300002":{"name":"choi comjung", "age":22, "major":"컴퓨터정보"}
}

number = input("학번:")
# print(infos[number])

info = infos.get(number, "학번이 없어요")
print(info)
print()

if number in infos: # keys() 메소드 쓰지 않아도 기본적으로 키 값에서 찾아줌
    print(infos[number])
else:
    print("학번이 없습니다.")