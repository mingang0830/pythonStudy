import sqlite3
conn = sqlite3.connect("student_system.db")
c = conn.cursor()

c.execute("create table IF NOT EXISTS professor(id text primary key, name text)")
c.execute("create table IF NOT EXISTS student(id text primary key, name text)")
c.execute("create table IF NOT EXISTS register_class(student_id text, subject_id int, grade text)")
c.execute("create table IF NOT EXISTS subject(id int primary key, name text, professor_id text)")


class Student:
    def __init__(self, id , name):
        c.execute("insert into student values(?,?)", (id, name))
        self.name = name
        self.id = id
        self.subject_lst = []

    def my_score(self):
        my_score = {}
        for sub in self.subject_lst:
            try:
                my_score[sub] = sub.score[self]
            except KeyError:
                my_score[sub] = None
        return my_score

    def __repr__(self):
        return self.name


class Pro:
    def __init__(self, id, name):
        c.execute("insert into professor values(?,?)", (id, name))
        self.subject = []
        self.name = name
        self.id = id

    def open_sub(self, id, name, limit):
        my_sub = Subject(id, name, self, limit)
        self.subject.append(my_sub)
        return my_sub

    def __repr__(self):
        return self.name


class Subject:
    def __init__(self, id, name, pro, limit):
        c.execute("insert into subject values(?,?,?)", (id, name, pro.id))
        self.id = id
        self.name = name
        self.pro = pro
        self.limit = limit
        self.sub_stu = []
        self.is_deleted = False
        self.score = {}

    def join(self, student):
        num = len(self.sub_stu)
        if self.is_deleted is False and num < self.limit:
            c.execute("insert into register_class (student_id, subject_id) values (?,?)", (student.id, self.id))
            self.sub_stu.append(student)
            student.subject_lst.append(self)
        else:
            return False

    def close(self):
        if len(self.sub_stu) == 0:
            self.is_deleted = True
            self.sub_stu = []
            c.execute("delete from subject where id = '{}'".format(self.id))
            c.execute("delete from register_class where subject_id = '{}'".format(self.id))

    def check(self, student, score):
        if score in [Score.A, Score.B, Score.C]:
            if student in self.sub_stu:
                c.execute("update register_class set grade = '{}' where student_id = '{}' and subject_id = '{}'".format(score, student.id, self.id))
                self.score[student] = score
        else:
            raise Exception('잘못된 점수입니다.')

    def __repr__(self):
        return f'({self.id} - {self.name} - {self.pro} - {self.limit})'
        # == '{} - {}'.format(self.name, self.desc)


class Score:
    A = 'A'
    B = 'B'
    C = 'C'


def program():
    p1 = Pro('kkii', '김교수')
    p2 = Pro('eeee', '이교수')
    stu1 = Student("kim1234", "김동욱")
    stu2 = Student("uu11uu", "유재석")
    stu3 = Student("kang", '강호동')

    sub_list = []  # 개설된 강의 리스트
    for pro, id, name, limit, in [(p1, 1, "자료구조", 2),
                                   (p1, 2, "컴퓨터의 기본", 4),
                                   (p2, 3, "수학개론", 1),
                                   (p2, 4, "물리개론", 3),
                                   (p2, 5, "생물개론", 5)]:
        sub_list.append(pro.open_sub(id, name, limit))

    sub_list[0].join(stu1)  # 수강신청
    sub_list[2].join(stu1)
    sub_list[4].join(stu1)
    sub_list[0].join(stu2)
    sub_list[4].join(stu2)
    sub_list[4].join(stu3)

    for sub in sub_list:  # 정원 안 찬 강의 폐강시키기
        sub.close()

    sub_list[0].check(stu1, Score.A)
    sub_list[4].check(stu1, Score.C)
    sub_list[0].check(stu2, Score.C)
    sub_list[4].check(stu2, Score.C)
    sub_list[4].check(stu3, Score.A)


if __name__ == "__main__":

    program()

    # print(c.execute("select * from register_class").fetchall())
    # print(c.execute("select * from student").fetchall())
    # print(c.execute("select * from professor").fetchall())
    # print(c.execute("select * from subject").fetchall())

    print("====================================")
    print("1. 학생 관리")
    print("2. 교수 관리")
    print("3. 학점 주기")
    print("4. 검색")
    menu = input("선택할 메뉴 : ")

    if menu == "1":
        print(c.execute("select id, name from student").fetchall())
        student_id = input("아이디 입력 : ")
        try:
            c.execute("select id from student where id = '{}'".format(student_id))
            student_info = {}
            student_name = c.execute("select name from student where id = '{}'".format(student_id)).fetchone()[0]
            student_registered_class = c.execute("select  b.id, b.name, c.name, a.grade from register_class a join subject b on a.subject_id = b.id join professor c on b.professor_id = c.id where a.student_id = '{}'".format(student_id)).fetchall()
            student_info[student_name] = student_registered_class
            # { 이름 : 과목 id, 과목 이름, 성적, 담당교수}
            print(student_info)
        except TypeError:
            print("없는 아이디 입니다.")

    elif menu == "2":
        print(c.execute("select id, name from professor").fetchall())
        professor_id = input("아이디 입력 : ")
        try:
            c.execute("select id from professor where id = '{}'".format(professor_id))
            # 오픈한 과목 하나밖에 안나와 왜
            professor_info = c.execute("select a.name, b.id, b.name, count(c.student_id) from professor a join subject b on a.id = b.professor_id join register_class c on b.id = c.subject_id where b.professor_id = '{}' ".format(professor_id)).fetchall()
            print(professor_info)
        except TypeError:
            print("없는 아이디 입니다.")

    elif menu == "3":
        # print(c.execute("select * from register_class").fetchall())
        professor_id = input("교수 아이디 입력 : ")
        subject_id = input("과목 아이디 입력 : ")
        student_id = input("학생 아이디 입력 : ")
        grade = c.execute("select a.grade from register_class a join subject b on a.subject_id = b.id join student c on a.student_id = c.id where b.id = '{}'and c.id = '{}'".format(subject_id, student_id)).fetchall()
        if grade == [(None,)]:
            input_grade = input("성적 입력 : ")
            c.execute("update register_class set grade = '{}' where student_id = '{}' and subject_id = '{}'".format(input_grade, student_id, subject_id))
            # print(c.execute("select * from register_class where student_id = '{}' and subject_id = '{}'".format(student_id, subject_id)).fetchone())
        else:
            raise Exception("성적입력 불가능")

    elif menu == "4":
        print("1. 학생 검색")
        print("2  과목 검색")
        sub_menu = input("선택할 메뉴 : ")

        if sub_menu == "1":
            print("1. 성적으로 학생 검색")
            print("2. 과목으로 학생 검색")
            side_menu = input("선택할 메뉴 : ")

            if side_menu == "1":
                grade = input("검색할 성적을 입력해주세요 : ")
                students = c.execute("select a.id, a.name from student a join register_class b on a.id = b.student_id where b.grade = '{}'".format(grade)).fetchall()
                print(set(students))
            elif side_menu == "2":
                subject_id = input("검색할 과목 아이디를 입력해주세요 : ")
                # 여러개 입력받아 select문에 넣기 어떻게 하는 건가요....
                # 1,2,3,4
                # split(,)
                # -> [1,2,3,4]
                # select ... from student where id in [1,2,3,4]
                # [(1, ...), (2, ...), (3, ...), (4, ...)]
                # for - loop
                students = c.execute("select a.id, a.name from student a join register_class b on a.id = b.student_id where b.subject_id = '{}'".format(subject_id)).fetchall()
                if not students:
                    print("수강신청한 학생이 없습니다.")
                else:
                    print(students)
            else:
                raise Exception("없는 메뉴 입니다.")

        elif sub_menu == "2":
            print("1. 제일 많이 수강 신청한 과목")
            print("2. 제일 많이 낙제한 과목")
            print("3. 제일 많이 A 받은 과목")

            side_menu = input("선택할 메뉴 : ")

            if side_menu == "1":
                subject = c.execute("select a.id, a.name from subject a join register_class b on a.id = b.subject_id group by b.subject_id order by b.subject_id desc").fetchone()
                print(subject)
            elif side_menu == "2":
                subject = c.execute("select a.id, a.name from subject a join register_class b on a.id = b.subject_id where b.grade = 'C' group by b.grade order by b.grade desc").fetchone()
                print(subject)
            elif side_menu == "3":
                subject = c.execute("select a.id, a.name from subject a join register_class b on a.id = b.subject_id where b.grade = 'A' group by b.grade order by b.grade desc").fetchone()
                print(subject)
            else:
                raise Exception("없는 메뉴 입니다.")

        else:
            raise Exception("없는 메뉴 입니다.")

    else:
        raise Exception("없는 메뉴 입니다.")


