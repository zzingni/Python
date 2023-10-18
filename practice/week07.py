

def test():
    print(1)
    print(2)
    return

print(test()) # None이 return 됨

def test():
    print("3")
    print("4")
    return 0

print(test()) # 0이 return 됨
# test() 함수를 덮어써버림!!!!!!!!!!!!!!!!!
# 기본적으로 파이썬은 함수 내에 return이 없어도 그냥 return 하는 것과 똑같음.

def test():
    print("5")
    return
    print("6")

# 인터럽트 : 함수 호출했을 때 메인에서 진행중이던 코드가 중지한 상태
# 파이썬은 함수가 무조건 하나의 값 이상을 반환한다고 생각해도 됨(None)

print(test())

def test(itr):
    for i in range(itr):
        print("안녕")

# print(test(2)) # None
test(2)

def test(itr, value):
    for i in range(itr):
        print(value)

test(2, "안녕")

def avg(input):
    if type(input) is list: # range에는 기본적으로 정수만 들어옴. 정수가 아닌 아이가 들어오면 함수가 뻗어버림.
        return sum(input) / len(input)

print(avg([1,2,3,4]))
result = print(avg("1234"))

if result: # None 이면 False랑 똑같음
    print(result)
else:
    print("자료에 문제가 있습니다.")

# 파이썬에서는 참 거짓이 true, false(0, None 등) 2가지밖에 없음

student_scores = {"김인하":92, "이인하":85, "박인하":78}

def calculate_average_from_dict(scores):
    if type(scores) is dict:
        values = list(scores.values())
        return sum(values) / len(values)

avg_score = calculate_average_from_dict(student_scores)
print(f"평균점수: {avg_score:.2f}")

def calculate_average(scores):
    if type(scores) is dict:
        values = list(scores.values())
        return sum(values) / len(values)
    elif type(scores) is list:
        return sum(values) / len(values)


def remove_value(_list, target):
    return [i for i in _list if target != i]
    # src_list = _list[:]
    # while target in src_list:
    #     src_list.remove(target)
    # retrun src_list


numbers = [1, 2, 3, 2, 4, 2, 5]
value_remove = 2
new_numbers = remove_value(numbers, value_remove)
print(numbers, new_numbers)

avg_score = calculate_average_from_dict(student_scores)
print(f"평균점수: {avg_score:.2f}")