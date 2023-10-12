
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