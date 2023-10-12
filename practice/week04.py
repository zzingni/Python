

stu_1 = [202344069, "김인하", "컴정", 20]
stu_2 = [202344000, "이인하", "컴정", 20]

print(stu_2[1][0]) # "이"
print(str(stu_2[0])[:4])    # 2023

a = ["hiimjiuen"]
ac = a[:4]
print(type(ac)) # 리스트의 슬라이싱 값은 리스트!!!!

print("학번", type(stu_1[0]), stu_2[0]) # 인덱싱 값은 인덱싱 한 자료형에 따라 다름.
print("이름", type(stu_1[1]), stu_2[1])

test_list = list()
print(test_list, type(test_list))

test_list = []
print(test_list, type(test_list))


test_list = ["권지은", 25, 166.6]
print(test_list)

for data in test_list:
    print(test_list) # test_list안의 개수만큼 for문 반복됨, 4번 출력.