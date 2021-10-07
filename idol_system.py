from random import choice


class Fanclub:
    def __init__(self, fanclub):
        self.total = 0  # 팬클럽 회원 수
        self.fanclub = fanclub  # 팬클럽 이름

    def join(self, number):
        self.total = self.total + number

    def withdraw(self, number):
        self.total = self.total - number


class People(Fanclub):
    def __init__(self, name, fanclub):
        super().__init__(fanclub)
        self.name = name
        self.perform = 0  # 공연 횟수

    def is_fanclub(self):
        # 팬클럽이 있으면 True 없으면 False 리턴
        if self.fanclub is not None:
            return True
        else:
            return False

    def performance(self):
        self.perform += 1
        # 만약 팬클럽이 있다면
        if self.is_fanclub():
            # 공연할때마다 팬클럽에 속한 사람들의 10%(반올림)만큼 팬이 증가합니다.
            self.total += int(self.total * 0.1)
        else:
            # 30% 확률로 팬클럽 생성
            if choice([1,1,1,2,2,2,2,2,2]) == 1:
                self.fanclub = input('팬클럽 생성 : ')  # 팬클럽 이름 지정
                self.total = 10  # 팬클럽 회원수 추가

    def audition(self):
        pass

    def release_album(self):
        pass


class Idol(People):  # 솔로
    def __init__(self, i_name, g_name, fanclub, name):
        super().__init__(name)
        self.i_name = i_name  # 아이돌 이름
        self.g_name = g_name  # 그룹 이름
        self.fanclub = fanclub  # 팬클럽 이름


class Group(Idol):  # idol에서 데려오기
    def g_performance(self):
        pass


class Agency(Group):

    def solo_debut(self):
        pass

    def group_debut(self):
        pass

if __name__ == "__main__":

    jay = People('제이', '재프')
    jay.join(10)
    jay.performance()
    print(jay.fanclub)
    print(jay.total)
    jay.performance()
    print(jay.total)
    print(jay.perform)
