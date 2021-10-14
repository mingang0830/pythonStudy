from random import choice


class Fanclub:
    def __init__(self, fanclub):
        self.total = 10  # 팬클럽 회원 수
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
            if choice([1, 1, 1, 2, 2, 2, 2, 2, 2]) == 1:
                self.fanclub = input('팬클럽 생성 : ')  # 팬클럽 이름 지정
                self.total = 10  # 팬클럽 회원수 추가

    def audition(self):
        pass

    def release_album(self, f_lst):  # 딕셔너리 받기

        #딕셔너리 값을 기준으로 내림차준 정렬
        sort_f = sorted(f_lst.values())

        # 1,2,3위 변수 지정
        first = sort_f[0]
        second = sort_f[1]
        third = sort_f[2]

        if self.total == first:
            if choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == 1:  # 1위가 성공하면
                self.total += int(self.total * 0.3)
                print('성공')
            else:  # 1위가 실패하면
                self.total -= int(self.total * 0.1)
                print('실페')

        elif self.total == second:
            if choice([1, 1, 1, 2, 2]) == 1:  # 2위가 성공하면
                self.total += int(self.total * 0.3)
                print('성공')
            else:  # 2위가 실패하면
                self.total -= int(self.total * 0.1)
                print('실페')

        elif self.total == third:
            if choice([1, 2]) == 1:  # 3위가 성공하면
                self.total += int(self.total * 0.3)
                print('성공')
            else:  # 3위가 실패하면
                self.total -= int(self.total * 0.1)
                print('실페')

        else:  # 나머지 등수
            if choice([1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 1:
                self.total += int(self.total * 0.3)
                return '성공'
            else:
                self.total -= int(self.total * 0.1)
                return '실패'


class Idol(People):  # 솔로
    def __init__(self, i_name, g_name, fanclub, name):
        super().__init__(name, fanclub)
        self.i_name = i_name  # 아이돌 이름
        self.g_name = g_name  # 그룹 이름


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
    jay.performance()
    print(jay.fanclub)

    jay.performance()
    jaf = jay.total

    min = People('민','민트')
    min.performance()
    print(min.fanclub)
    min.join(50)
    mint = min.total

    qq = People('큐', '큐프')
    qq.performance()
    qq.join(2)
    qf = qq.total

    f_lst = {'mint': mint, 'jaf': jaf, 'qf': qf}

    print(f_lst)

    min.release_album(f_lst)
    print(min.total)
