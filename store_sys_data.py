import sqlite3

from store_sys_user import get_professor_obj

conn = sqlite3.connect("student_system.db")
c = conn.cursor()


def make_subject_map(data):
    return {
        "id": data[0],
        "name": data[1],
        "professor.id": data[2],
    }


def select_subject_from_db(subject_id):
    return c.execute("select id, name, professor_id from subject where id = (?)", (subject_id,)).fetchone()


def insert_subject_to_db(subject_id, name, professor):
    return c.execute("insert into subject values(?,?,?)", (subject_id, name, professor.id))


def create_subject(subject_id, name, professor):
    return make_subject_map(insert_subject_to_db(subject_id, name, professor))


def get_subject(subject_id):
    data = select_subject_from_db(subject_id)
    return make_subject_map(data)


def insert_register_class_to_db(student_id, subject_id):
    return c.execute("insert into register_class (student_id, subject_id) values (?,?)", (student_id, subject_id))


def delete_from_subject_to_db(subject_id):
    return c.execute("delete from subject where id = (?)", (subject_id,))


def delete_from_register_class_to_db(subject_id):
    return c.execute("delete from register_class where subject_id = (?)", (subject_id,))


def grade_to_db(score, student_id, subject_id):
    return c.execute("update register_class set grade = (?) where student_id = (?) and subject_id = (?)",
                     (score, student_id, subject_id))


def get_score_from_db(subject_id, student_id):
    return c.execute("select register_class.grade from register_class "
                     "join subject on register_class.subject_id = subject.id "
                     "join student on register_class.student_id = student.id "
                     "where subject.id = (?) and student.id = (?)", (subject_id, student_id)).fetchall()


def check_score(subject_id, student_id):
    if get_score_from_db(subject_id, student_id) == [(None,)]:
        return True
    return False


def select_student_from_db(score):
    return c.execute("select student.id, student.name "
                     "from student join register_class on student.id = register_class.student_id "
                     "where register_class.grade = (?)", (score,)).fetchall()


def get_students_by_set_type(score):
    return set(select_student_from_db(score))


def if_subjects(subject_id):
    return c.execute(
        "select student.id, student.name from student "
        "join register_class on student.id = register_class.student_id "
        "where register_class.subject_id in (?)", (subject_id,)).fetchall()


def if_a_subject(subject_id):
    return c.execute("select student.id, student.name from student "
                     "join register_class on student.id = register_class.student_id "
                     "where register_class.subject_id = (?)", (subject_id,)).fetchall()


def make_students(subject_id):
    if "," in subject_id:
        return if_subjects(tuple(subject_id.split(",")))
    else:
        return if_a_subject(subject_id)


def the_most_registered_subject():
    return c.execute("select subject.id, subject.name from subject "
                     "join register_class on subject.id = register_class.subject_id "
                     "group by register_class.subject_id order by register_class.subject_id desc").fetchone()


def the_most_get_c_grade():
    return c.execute("select subject.id, subject.name from subject "
                     "join register_class on subject.id = register_class.subject_id where register_class.grade = 'C' "
                     "group by register_class.grade order by register_class.grade desc").fetchone()


def the_most_get_a_grade():
    return c.execute("select subject.id, subject.name from subject "
                     "join register_class on subject.id = register_class.subject_id where register_class.grade = 'A' "
                     "group by register_class.grade order by register_class.grade desc").fetchone()


class Subject:
    def __init__(self, id, name, professor, limit=5):
        self.id = id
        self.name = name
        self.professor = professor
        self.limit = limit
        self.sub_stu = []
        self.is_deleted = False
        self.score = {}

    def join(self, student):
        num = len(self.sub_stu)
        if self.is_deleted is False and num < self.limit:
            self.sub_stu.append(student)
            student.subject_lst.append(self)
            insert_register_class_to_db(student.id, self.id)
        else:
            return False

    def close(self):
        if len(self.sub_stu) == 0:
            self.is_deleted = True
            self.sub_stu = []
            delete_from_subject_to_db(self.id)
            delete_from_register_class_to_db(self.id)

    def check(self, student, score):
        if score in Score.ALL and student in self.sub_stu:
            self.score[student] = score
            grade_to_db(score, student.id, self.id)
        else:
            raise Exception('잘못된 점수입니다.')

    def __repr__(self):
        return f'({self.id} - {self.name} - {self.professor} - {self.limit})'


def get_subject_obj(subject_id):
    data = get_subject(subject_id)
    return Subject(id=data["id"], name=data["name"], professor=get_professor_obj(data["professor.id"]))


class Score:
    A = 'A'
    B = 'B'
    C = 'C'
    ALL = [A, B, C]
