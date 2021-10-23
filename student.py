class Student:
    def __init__(self, name):
        self.name = name
        self.subject_lst = []


class Subject:
    def __init__(self, name, desc, pro, limit):
        self.name = name
        self.desc = desc
        self.pro = pro
        self.limit = limit
        self.sub_stu = []
        self.is_deleted = False

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


class Pro:
    def __init__(self):
        self.subject = []

    def open_sub(self, name, desc, limit):
        my_sub = Subject(name, desc, self, limit)
        self.subject.append(my_sub)
        return my_sub


if __name__ == "__main__":
    p1 = Pro()
    p2 = Pro()
    stu1 = Student("김동욱")

    sub_list = []
    for pro, name, desc, limit in [(p1, "자료구조", "자료의 구조", 1),
                                   (p1, "컴퓨터의 기본", "기본", 2),
                                   (p2, "수학개론", "수학", 3),
                                   (p2, "물리개론", '물리', 3),
                                   (p2, "생물개론", '생물', 5)]:
        sub_list.append(pro.open_sub(name, desc, limit))

    sub_list[0].join(stu1)
    sub_list[2].join(stu1)
    sub_list[4].join(stu1)

    for sub in sub_list:
        sub.close()
        print(sub.is_deleted)
