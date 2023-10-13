

infos = {
    "202300001":{"name":"kim inha", "age":21},
    "202300002":{"name":"choi comjung", "age":22, "major":"컴퓨터정보"}
}

infos["202300003"] = {} # 빈 딕셔너리 생성

infos["202300003"]["name"] = "yi comsi"
infos["202300003"]["major"] = "컴퓨터 시스템"

infos["202300004"] = {
    "name":"wang jeonja",
    "major": "전자"
}

print(infos)


test_dict = {1: "uno", 2:"two", 3:"three"}

test_dict[5] = "five"
print(test_dict)    # {1: "uno", 2:"two", 3:"three", 5:"five"}

test_dict[1] = "one"
print(test_dict)    # {1: "one", 2:"two", 3:"three", 5:"five"}

del test_dict[2]
print(test_dict)    # {1: "one", 3:"three", 5:"five"}