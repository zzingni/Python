

test_list = [1,2,3]
test_list.append(5)
test_list.append(8)
print(test_list) # 1,2,3,5,8

test_list.insert(3, 7)
print(test_list) # 1,2,3,7,5,8

test_list.insert(-19, 0)
print(test_list) # 0,1,2,3,7,5,8
# 음수 인덱스는 리스트의 끝에서부터 역으로 셈. 인덱스 범위 벗어나면 맨 앞에 0이 추가됨.

test_list.insert(100,200)
print(test_list, len(test_list)) # 0,1,2,3,7,5,8,100
# 100이면 맨 뒤에 있을 거라 생각하고 맨 뒤에 추가해줌.

test_list1 = [1,2,3]
test_list2 = [3,4]

print(1+1) # 2
print("1" + "1") # 11
print(test_list1 + test_list2) # 1,2,3,3,4
print(test_list2 * 3) # 3,4,3,4,3,4
print(test_list1) # 1,2,3 > 리스트 원본 변경 안 됨
print(len(test_list1)) # 3

test_list1 = [1,2,3]
test_list2 = ["3","4"]
print(test_list1 + test_list2) # 1, 2, 3, '3', '4' > 배열 내 요소의 타입이 동일하진 않지만 리스트 + 리스트 는 리스트의 합을 보여줌.