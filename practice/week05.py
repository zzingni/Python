


a = "string"
a[0] # s

b = [1,2,3]
b[0] # 1

infos = {
    "202300001":{"name" : "kim inha", "age" : 21},
    "202300002":{"name" : "choi comjung", "age" : 22, "major":"컴퓨터정보"}
}

print(infos["202300002"]["major"])

infos = {1:["kim iniha", 21], 2:["choi comjung", 22]}
infos[2] # ['choi comjung', 22]
print(infos[2][1])


info_a = {"name" : "kim inha", "age" : 21}
info_b = {"name" : "choi comjung", "age" : 22}

# print(info_a[0]) # 키 에러 / 인덱스로 접근 불가 / 딕셔너리는 순번 없음
# print(info_a[name]) # 네임 에러 / name 이라는 변수 없음
# print(info_a["이름"]) # 키 에러

print(info_a['name'])
print(info_a['age'])



test_dict = {
    "one" : 1,
    "one" : 5, # key 값이 동일하면 덮어씌어짐.
    "two" : 2,
    "three" : 3
}

print(test_dict)

test_dict = dict()
print(test_dict, type(test_dict))

test_dict = {}
print(test_dict, type(test_dict))