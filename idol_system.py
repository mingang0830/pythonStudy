class People:
    def __init__(self, name):
        self.name = name
        self.perform = 0  # 공연 횟수

    def performance(self):
        self.perform += 1
        pass

    def is_fanclub(self):

        pass

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


class Fanclub(Group):
    def __init__(self, i_name, g_name, fanclub, name):
        super().__init__(i_name, g_name, fanclub, name)
        self.total = None  # 팬클럽 회원 수

    def join(self, number):
        pass

    def withdraw(self, number):
        pass


class Agency(Group):

    def solo_debut(self):
        pass

    def group_debut(self):
        pass
