import sqlite3

from store_sys_data import check_grade, update_register_class_set_grade_by_student_id_and_subject_id, \
    get_students_by_set_type, make_students_with_subject_id, the_most_registered_subject, the_most_get_c_grade, \
    the_most_get_a_grade
from store_sys_user import select_student_all, select_student_by_id_from_db, make_student_info, \
    select_professor_all, select_professor_by_id_from_db, professor_info_by_id
conn = sqlite3.connect("student_system.db")
c = conn.cursor()


print("====================================")
print("1. 학생 관리")
print("2. 교수 관리")
print("3. 학점 주기")
print("4. 검색")
menu = input("선택할 메뉴 : ")

if menu == "1":
    select_student_all()
    student_id = input("아이디 입력 : ")
    try:
        select_student_by_id_from_db(student_id)
        student_info = make_student_info(student_id)
        print(student_info)
    except TypeError:
        print("없는 아이디 입니다.")

elif menu == "2":
    select_professor_all()
    professor_id = input("아이디 입력 : ")
    try:
        select_professor_by_id_from_db(professor_id)
        professor_info = professor_info_by_id(professor_id)
        print(professor_info)
    except TypeError:
        print("없는 아이디 입니다.")

elif menu == "3":
    professor_id = input("교수 아이디 입력 : ")
    subject_id = input("과목 아이디 입력 : ")
    student_id = input("학생 아이디 입력 : ")
    if check_grade(subject_id, student_id) is True:
        input_grade = input("성적 입력 : ")
        update_register_class_set_grade_by_student_id_and_subject_id(input_grade, student_id, subject_id)
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
            students = get_students_by_set_type(grade)
            print(students)
        elif side_menu == "2":
            subject_id = input("검색할 과목 아이디를 입력해주세요 : ")
            students = make_students_with_subject_id(subject_id)
            print(students)
        else:
            raise Exception("없는 메뉴 입니다.")

    elif sub_menu == "2":
        print("1. 제일 많이 수강 신청한 과목")
        print("2. 제일 많이 낙제한 과목")
        print("3. 제일 많이 A 받은 과목")

        side_menu = input("선택할 메뉴 : ")

        if side_menu == "1":
            print(the_most_registered_subject())
        elif side_menu == "2":
            print(the_most_get_c_grade())
        elif side_menu == "3":
            print(the_most_get_a_grade())
        else:
            raise Exception("없는 메뉴 입니다.")

    else:
        raise Exception("없는 메뉴 입니다.")

else:
    raise Exception("없는 메뉴 입니다.")


