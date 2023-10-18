

character = {
    "name": "기사",
    "level" : 12,
    "items" : {
        "sword": "불꽃의 검",
        "armor" : "풀플레이트",
    },
    "skill":["베기", "세게 베기", "아주 세게 베기"] 
}

for key in character:
    if type(character[key]) is dict:
        for v in character[key].values():
            print(f"{key} : {v}")
    elif type(character[key]) is list:
        for v in range(len(character[key])):
            print(f"{key} : {character[key][v]}")
    else:
        print(f"{key} : {character[key]}")


