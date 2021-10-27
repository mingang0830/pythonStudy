from student_system_data import Subject, SubjectScore, SubjectPass, Score
from student_system_user import Pro, Student


def program():

    essential_subjects = Subject.make_essential()

    p1 = Pro('김교수')
    p2 = Pro('이교수')
    stu1 = Student("김동욱")

    sub_list = []  # 개설된 강의 리스트

    for pro, name, desc, limit, type_ in [(p1, "자료구조", "자료의 구조", 1, SubjectScore),
                                   (p1, "컴퓨터의 기본", "기본", 2, SubjectPass),
                                   (p2, "수학개론", "수학", 3, SubjectScore),
                                   (p2, "물리개론", '물리', 3, SubjectScore),
                                   (p2, "생물개론", '생물', 5, SubjectScore)]:
        sub_list.append(pro.open_sub(name, desc, limit, type_))

    return sub_list, stu1, p1, essential_subjects


if __name__ == "__main__":

    sub_list, stu1, p1, essential_subjects = program()

    p1.assign_essential(essential_subjects)  # side effect

    sub_list[0].join(stu1)  # 수강신청
    sub_list[2].join(stu1)
    sub_list[4].join(stu1)

    for sub in sub_list:  # 정원 안 찬 강의 폐강시키기
        sub.close()

    #sub_list[0].check(stu1, Score.A)
    sub_list[1].check(stu1, Score.PASS)
    #sub_list[4].check(stu1, Score.A)
    for i in p1.subject:
        print(i)
        print(i.name)







