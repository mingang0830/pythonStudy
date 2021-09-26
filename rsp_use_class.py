from random import choice


class Character:
    def __init__(self, hp, ap):
        self.hp = hp
        self.ap = ap

    def draw(self):
        raise NotImplemented


class Player(Character):
    def draw(self):
        return input("뭐 낼꺼임")


class Computer(Character):
    def draw(self):
        return choice(["가위", "바위", "보"])


class Duck:  # 덕 타이핑
    def draw(self):
        return "가위"


class Match:
    def __init__(self, player, computer): #  의존성 up!
        self.player = player
        self.computer = computer

    def is_draw(self, player_draw, computer_draw):
        return player_draw == computer_draw

    def is_player_won(self, player_draw, computer_draw):
        if (player_draw == "보" and computer_draw == "가위"
            or player_draw == "가위" and computer_draw == "바위"
            or player_draw == "바위" and computer_draw == "보"):
            return False
        elif (player_draw == "가위" and computer_draw == "보"
              or player_draw == "바위" and computer_draw == "가위"
              or player_draw == "보" and computer_draw == "바위"):
            return True

    def match(self):
        player_draw = self.player.draw()
        computer_draw = self.computer.draw()

        print("플레이어가 낸거 :", player_draw)
        print("컴퓨터가 낸거 :", computer_draw)

        is_player_won = self.is_player_won(player_draw, computer_draw)
        if (self.is_draw(player_draw, computer_draw)):
            return
        elif is_player_won:
            self.computer.hp = self.computer.hp - self.player.ap
        elif is_player_won is False:
            self.player.hp = self.player.hp - self.computer.ap


if __name__ == "__main__":
    player = Player(hp=10, ap=3)
    computer = Computer(hp=8, ap=2)

    '''
    duck = Duck()
    duck.hp = 30
    duck.ap = 10
    '''

    Match(player, computer).match()

    print(player.hp)
    print(computer.hp)
