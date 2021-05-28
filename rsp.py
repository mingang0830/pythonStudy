import random
win_count = 0
player_result = None
computer_result = None
game_result = None


def game(player, computer):
    player_select = None
    computer_select = None
    result = None
    if player == "1":
        player_select = "가위"
        if computer == "1":
            result = "무승부"
        elif computer == "2":
            result = "패배"
        elif computer == "3":
            result = "승리"
    elif player == "2":
        player_select = "바위"
        if computer == "1":
            result = "승리"
        elif computer == "2":
            result = "무승부"
        elif computer == "3":
            result = "패배"
    elif player == "3":
        player_select = "보"
        if computer == "1":
            result = "패배"
        elif computer == "2":
            result = "승리"
        elif computer == "3":
            result = "무승부"

    if computer == "1":
        computer_select = "가위"
    elif computer == "2":
        computer_select = "바위"
    elif computer == "3":
        computer_select = "보"

    return player_select, computer_select, result


while True:
    print("======가위바위보======")
    print("1.가위\n2.바위\n3.보\n4.종료")
    player = input("입력 : ")
    computer = str(random.randrange(1, 4))
    if player not in ["1", "2", "3", "4"]:
        print("잘못된 입력입니다.")
        continue

    if player in ["1", "2", "3"]:
        player_result, computer_result, game_result = game(player, computer)
    elif player == "4":
        print("프로그램 종료")
        break

    if game_result == "승리":
        win_count += 1

    result_message = f"플레이어: {player_result} - 컴퓨터: {computer_result} = {game_result}"
    print(result_message)
    print("이긴 라운드 수 : %d" % win_count)
