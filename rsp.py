import random
win_count = 0
player_result = None
computer_result = None
game_result = None
result_message = None


def game(player, computer):
    result = None
    win = False
    rsp1 = {'가위': '1', '바위': '2', '보': '3'}
    rsp2 = {'1': '가위', '2': '바위', '3': '보'}
    player_select = rsp2[player]
    computer_select = rsp2[computer]

    if (player == rsp1['가위'] and computer == rsp1['가위']) or (player == rsp1['바위'] and computer == rsp1['바위']) or (player == rsp1['보'] and computer == rsp1['보']):
        result = "무승부"
    elif (player == rsp1['가위'] and computer == rsp1['보']) or (player == rsp1['바위'] and computer == rsp1['가위']) or (player == rsp1['보'] and computer == rsp1['바위']):
        result = "승리"
        win = True
    elif (player == rsp1['가위'] and computer == rsp1['바위']) or (player == rsp1['바위'] and computer == rsp1['보']) or (player == rsp1['보'] and computer == rsp1['가위']):
        result = "패배"

    message = f"플레이어: {player_select} - 컴퓨터: {computer_select} = {result}"
    return win, message


while True:
    print("======가위바위보======")
    print("1.가위\n2.바위\n3.보\n4.종료")
    player = input("입력 : ")
    computer = str(random.randrange(1, 4))

    if player not in ["1", "2", "3", "4"]:
        print("잘못된 입력입니다.")
        continue

    if player == "4":
        print("프로그램 종료")
        break

    win_result, result_message = game(player, computer)

    if win_result:
        win_count += 1

    print(result_message)
    print("이긴 라운드 수 : %d" % win_count)
