

a = ["a", "1", 1.1]
print(1 in a)   # False
print("1" in a) # True
print("A" not in a) # True
print("a" not in a) # False


a = [3, 5, 7, 4, 1]
b = a[:]    # 리스트 복사 / 슬라이싱

c = sorted(a) 
d = sorted(a, reverse=True) 

print(c)    # [1, 3, 4, 5, 7]
print(d)    # [7, 5, 4, 3, 1]
print(a)    # [3, 5, 7, 4, 1]

a.sort()    
print(a)    # [1, 3, 4, 5, 7]
a.sort(reverse=True)    # [5, 5, 4, 3, 1]
print(a)    # [1, 3, 4, 5, 7]
print(b)    # [3, 5, 7, 4, 1]
print()


a = [1,2,3,4,5]
print(a)

# del a[:]
a.clear()
print(a)


test_list = [1,2,3]
add_list = ["a", "b"]

test_list.extend(test_list)
# add_list.extend()
print(test_list)
print(add_list)

result_list = test_list + add_list
print(test_list + add_list)
print(result_list)
print(test_list)
print(add_list) 
