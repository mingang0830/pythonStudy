import random

win_count = 0


def game(player, computer):
    result = None
    is_win = False

    if (player == '가위' and computer == '가위') or (player == '바위' and computer == '바위') or (player == '보' and computer == '보'):
        result = "무승부"
    elif (player == '가위' and computer == '보') or (player == '바위' and computer == '가위') or (player == '보' and computer == '바위'):
        result = "승리"
        is_win = True
    elif (player == '가위' and computer == '바위') or (player == '바위' and computer == '보') or (player == '보' and computer =='가위'):
        result = "패배"

    message = f"플레이어: {player} - 컴퓨터: {computer} = {result}"
    return is_win, message


while True:
    print("======가위바위보======")
    print("1.가위\n2.바위\n3.보\n4.종료")
    rock_scissors_paper = {'1': '가위', '2': '바위', '3': '보', '4': '종료'}

    player = rock_scissors_paper.get(input("입력 : "))
    computer = rock_scissors_paper[str(random.randrange(1, 4))]

    if player is None:
        print("잘못된 입력입니다.")
        continue

    if player == '종료':
        print("프로그램 종료")
        break

    is_win_result, result_message = game(player, computer)

    if is_win_result:
        win_count += 1

    print(result_message)
    print("이긴 라운드 수 : %d" % win_count)
