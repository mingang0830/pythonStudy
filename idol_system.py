from random import choice


class Fanclub:
    def __init__(self, fanclub):
        self.total = 10  # 팬클럽 회원 수(팬클럽이 있다면 10명부터 시작)
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

    def release_album(self, f_lst):  # 라스트 받기

        # 리스트 정렬
        sort_f = sorted(f_lst)

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

    def performance(self):
        self.perform += 1
        # 만약 팬클럽이 있다면
        if self.is_fanclub():
            # 공연할때마다 팬클럽에 속한 사람들의 30%만큼 팬이 증가합니다.
            self.total += int(self.total * 0.3)
        else:
            self.fanclub = input('팬클럽 생성 : ')  # 팬클럽 이름 지정
            self.total = 10  # 팬클럽 회원수 추가

    def audition(self): # 소속사에 지원하면 데뷰할 수 없습니다.
        print('이미 데뷔해서 오디션에 지원할 수 없습니다.')


class Group(Idol):  # idol에서 데려오기
    def __init__(self, g_name, name, fanclub):
        super().__init__(name, fanclub)
        self.g_name = g_name  # 그룹 이름

    def performance(self):
        self.perform += 1


class Agency(Group):

    def solo_debut(self):
        #if self.total >= 50 and self.perform >= 5:
        #   print('{0} 데뷔!!'.format(self.name))
        #print('데뷔 못함')
        pass

    def group_debut(self):
        pass


if __name__ == "__main__":

    jay = People('제이', '재프')
    jay.performance()
    print(jay.fanclub)
    jay.performance()

    min = People('민', None)
    min.performance()
    print(min.fanclub)
    min.join(50)

    qq = People('큐', '큐프')
    qq.performance()
    qq.join(2)

    f_lst = [min.total, jay.total, qq.total]

    print(f_lst)

    min.release_album(f_lst)
    print(min.total)

    iu = Idol('아이유', '유애나')
    iu.performance()
    print(iu.total)
    print(iu.fanclub)

    f_lst = [min.total, jay.total, qq.total, iu.total]
    iu.release_album(f_lst)

    iu.audition()



