

scores = [100, 45, 80, 0, 23]
# scores_new = reversed(scores) >>>> 에러!!!!
scores_new = list(reversed(scores))
print(scores_new)
print()
print(reversed(scores))
print(list(reversed(scores)))
print(scores)

# reversed랑 soted는 원본 리스트를 변경하지 않음
# reversed는 이터레이터 객체가 !!!반환!!! 되기 때문에 새로운 list 생성필요
# 따라서, 리스트로 변환해줘야함!!!!!!!!!!!

print(sorted(scores))
print(list(sorted(scores)))
print(scores)

# sorted는 revered와 달리 순회 가능한 객체를 정렬한 새로운 리스트 반환!
# 따라서 에러를 발생시키진 않음!!!!!!!

a = reversed(scores)
for r in a:
    print("1st ", r) # reversed()는 한 번만 실행되며 없어짐. 1회용으로 쓸 수 있음.
for r in a: # 2nd 출력 안 됨
    print("2nd ",r)

for r in reversed(scores):
    print(r)

a = list(reversed(scores))
for r in a:
    print("1st ", r)
for r in a:
    print("2nd ", r)