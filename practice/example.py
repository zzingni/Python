

str_input = input("태어난 해를 입력해 주세요> ")
birth_year = int(str_input)
birth = birth_year % 12

ddi = {0:"원숭이", 1:"닭", 2:"개", 3:"돼지", 4:"쥐", 5:"소", 6:"범", 7:"토끼", 8:"용", 9:"뱀", 10:"말", 11:"양"}


for i in ddi:
    if birth == i:
        print(f"{ddi[i]}띠 입니다.")
        break
    else:
        continue