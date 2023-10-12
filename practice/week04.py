
test = ["수박", "귤", "메론", "배", "딸기"]

del test[4]
print(test) # "수박", "귤", "메론", "배"

del test[0:2]
print(test) # "메론", "배"

test.append("망고")
test.append("귤")
test.append("블루베리")
print(test) # "메론", "배", "망고", "귤", "블루베리"

test.remove("귤") 
print(test) # "메론", "배", "망고", "블루베리"

p = test.pop() # "메론", "배", "망고"
print(p, type(p)) # 출력 : 블루베리, str
# 원본 리스트 : "메론" "배", "망고" / 원본 리스트에서는 빠지지만 p라는 변수에 값은 저장됨
# 즉, pop()메소드는 값을 삭제하지 않고 어딘가에 보관하고 있는 것.

test.pop() # "배"
test.pop(0) # ""
# 원래 스택 구조상 제일 뒤에 있는 걸 빼주는게 pop()인데 파이썬에서는 지정해서 빼줄
print(test) # 출력x