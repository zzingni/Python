
infos = {
    "202344069":{"name":"kim inha","age":21},
    "202344444":{"name":"choi comjung", "age":22, "major":"컴퓨터정보"}
}

for key, value in infos.items():
    print(key, value)
print()

for key in infos.keys():
    print(infos[key])   # 값들이 출력됨!!!!! 헷갈리지 말기 ㅠㅠㅠㅠㅠ 
print()

for key in infos.keys():
    print(key)
print()

for value in infos.values():
    print(value)
print()