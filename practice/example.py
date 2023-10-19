

alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'red', 'points':15}
alien_2 = {'color': 'blue', 'points':20}

aliens = [alien_0, alien_1, alien_2]

for idx in range(len(aliens)):
    print(f"{idx+1}번 외계인 색상: {aliens[idx]['color']}")

for idx, alien in enumerate(aliens):
    print(f"{idx+1}번 외계인 점수: {alien['points']}")


students = {
    '12210001': {'name': '김인하', 'major':'컴퓨터'},
    '12210011': {'name': '김슈슉', 'major':'전자'},
    '12210111': {'name': '김슈욱', 'major':'물류'}
            }

for number, student in students.items():
    print(f"학번:{number}")
    print(f"이름:{student['name']}")
    print(f"전공:{student['major']}")
    print()
