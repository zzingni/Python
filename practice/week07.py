

ip_addr = [127, 0, 0, 1]
ip_addr_new = [str(ip) for ip in ip_addr]
ip_addr_new = ".".join(ip_addr_new) 
print(ip_addr_new, type(ip_addr_new))
# join()으로 합치면 타입이 string이 됨!!


array = []
for i in range(0,20,2):
    if i % 4:
        array.append(i * i) 
print(array)
print()

array = [i * i for i in range(0,20,2) if i % 4]
print(array)



array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)
print()

array = [ i * i for i in range(0, 20, 2)]
print(array)


fruits = ["딸기", "사과", "배"]

print(", ".join(fruits))
# join 메서드로 연결

my_fev = ""
for f in fruits:
    if len(my_fev) > 0:
        my_fev += ","
    my_fev += f

print(my_fev)
print()
# 함수로 연결

example = {1:"one", 2:"two", 5:"five"}


for k in example:
    print(k)

for k in example.keys():
    print(k)

for v in example.values():
    print(v)

for k, v in example.items():
    print(k,v)


scores = [100, 45, 80, 0, 23]

for i, score in enumerate("권지은"):
    print(f"{i+1}번 과목 : {score}")

for i, score in enumerate(scores):
    print(f"{i+1}번 과목 : {score}")

# enumerate : 반복 가능한 객체를 받아서 해당 객체의 각 요소와 해당 요소의 인덱스를 반환