import random


class Computer:
    hp = 6
    power = 2

    def attack(self):
        return Computer.power

    def status(self):
        message = None
        is_end = False
        Player.hp -= Computer.attack(self)
        if Player.hp >= Computer.power:
            message = "플레이어 hp [%d], 컴퓨터 hp [%d] 컴퓨터 승" % (Player.hp, Computer.hp)
        elif Player.hp == 0 or Computer.hp == 0:
            message = "플레이어 hp [%d], 컴퓨터 hp [%d] 최종 우승 : 컴퓨터\n 게임 종료" % (Player.hp, Computer.hp)
            is_end = True
        return message, is_end


class Player:
    hp = 10
    power = 3

    def attack(self):
        return Player.power

    def status(self):
        message = None
        is_end = False
        Computer.hp -= Player.attack(self)
        if Computer.hp >= Player.power:
            message = "플레이어 hp [%d], 컴퓨터 hp [%d] 플레이어 승" % (Player.hp, Computer.hp)
        elif Computer.hp == 0 or Player.hp == 0:
            message = "플레이어 hp [%d], 컴퓨터 hp [%d] 최종 우승 : 플레이어\n 게임 종료" % (Player.hp, Computer.hp)
            is_end = True
        return message, is_end


class Game:

    def match(self, player_win, computer_win):
        while True:
            player_select = input("가위, 바위, 보를 입력하세요 :")
            if player_select not in ["가위", "바위", "보"]:
                print("잘못된 입력입니다.")
                continue
            break

        computer_select = random.choice(["가위", "바위", "보"])
        result = None
        is_end_result = False
        if(player_select == '가위' and computer_select == '가위') or (player_select == '바위' and computer_select == '바위') or (player_select == "보" and computer_select == "보"):
            pass
            result = "무승부"
        elif(player_select == '가위' and computer_select == '보') or (player_select == '바위' and computer_select == '가위') or (player_select == '보' and computer_select == '바위'):
            result, is_end_result = player_win.status()
        elif(player_select == '가위' and computer_select == '바위') or (player_select == '바위' and computer_select == '보') or (player_select == '보' and computer_select =='가위'):
            result, is_end_result = computer_win.status()

        return result, is_end_result


while True:
    start = Game()
    player_win = Player()
    computer_win = Computer()
    result_message, is_game_end = start.match(player_win, computer_win)
    print(result_message)

    if is_game_end:
        break
