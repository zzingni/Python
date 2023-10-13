


list_of_list = [
    [1,2,3],
    [3,4,5,7],
    [10,11]
]

for items in list_of_list:
    for item in items:
        print(item, end=" ")
    print()

for items in list_of_list:
    print(items) # [1,2,3] [3,4,5,7] [10,11]

name = "권지은"
scores = [22, 100, 30, 40]

for ele in name:
    print(ele, end="/") # 권/지/은

for score in scores:
    print(score)    # 22 100 30 40(줄바꿈)
