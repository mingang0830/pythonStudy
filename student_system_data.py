class Subject:
    def __init__(self, name, desc, pro, limit):
        self.name = name
        self.desc = desc
        self.pro = pro
        self.limit = limit
        self.sub_stu = []
        self.is_deleted = False
        self.score = {}

    def join(self, student):
        num = len(self.sub_stu)
        if self.is_deleted is False and num < self.limit:
            self.sub_stu.append(student)
            student.subject_lst.append(self)

        else:
            return False

    def close(self):
        if len(self.sub_stu) == 0:
            self.is_deleted = True
            self.sub_stu = []

    @staticmethod
    def make_essential(pro=None):
        essential_list = []
        for name, desc, type_ in ESSENTIAL_SUBJECTS:
            essential_list.append(type_(name, desc, pro, None))
        return essential_list

    def __repr__(self):
        return f'({self.__class__} {self.name} - {self.desc} - {self.pro} - {self.limit})'
        # == '{} - {}'.format(self.name, self.desc)


class SubjectScore(Subject):
    def check(self, student, score):
        if score in [Score.A, Score.B, Score.C]:
            if student in self.sub_stu:
                self.score[student] = score
        else:
            raise Exception('잘못된 점수입니다.')

    @staticmethod
    def make_essential(pro=None):
        raise Exception('잘못된 접근입니다.')


class SubjectPass(SubjectScore):
    def check(self, student, score):
        if score in [Score.PASS, Score.NONPASS]:
            if student in self.sub_stu:
                self.score[student] = score
        else:
            raise Exception('잘못된 점수입니다.')

    @staticmethod
    def make_essential(pro=None):
        raise Exception('잘못된 접근입니다.')


ESSENTIAL_SUBJECTS = [('영문학', '영문학개론', SubjectPass),
                      ('통번역', '통번역개론', SubjectScore)]

class Score:
    A = 100
    B = 80
    C = 70
    PASS = True
    NONPASS = False
