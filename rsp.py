import random
win_count = 0


def player_scissors():
    if str(computer) == "1":
        massage = "플레이어 : 가위 - 컴퓨터: 가위 = 무승부"
        win = 0
    elif str(computer) == "2":
        massage = "플레이어: 가위 - 컴퓨터: 보 = 플레이어 승리"
        win = 1
    else:
        massage = "플레이어: 가위 - 컴퓨터: 바위 = 플레이어 패배"
        win = 0
    return massage, win


def player_rock():
    if str(computer) == "1":
        massage = "플레이어 : 바위 - 컴퓨터: 바위 = 무승부"
        win = 0
    elif str(computer) == "2":
        massage = "플레이어: 바위 - 컴퓨터: 가위 = 플레이어 승리"
        win = 1
    else:
        massage = "플레이어: 바위 - 컴퓨터: 보 = 플레이어 패배"
        win = 0
    return massage, win


def player_paper():
    if str(computer) == "1":
        massage = "플레이어 : 보 - 컴퓨처: 보 = 무승부"
        win = 0
    elif str(computer) == "2":
        massage = "플레이어: 보 - 컴퓨터: 바위 = 플레이어 승리"
        win = 1
    else:
        massage = "플레이어: 보 - 컴퓨터: 가위 = 플레이어 패배"
        win = 0
    return massage, win


while True:
    print("======가위바위보======")
    print("1.가위\n2.바위\n3.보\n4.종료")
    player = input("입력 : ")
    computer = random.randrange(1, 4)
    if player not in ["1", "2", "3", "4"]:
        print("잘못된 입력입니다.")
        continue
    elif player == "1":
        result_massage, win_result = player_scissors()
    elif player == "2":
        result_massage, win_result = player_rock()
    elif player == "3":
        result_massage, win_result = player_paper()
    elif player == "4":
        print("프로그램 종료")
        break

    if win_result == 1:
        win_count += 1

    print(result_massage)
    print("이긴 라운드 수 : %d" % win_count)


