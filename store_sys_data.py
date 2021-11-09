import sqlite3
conn = sqlite3.connect("student_system.db")
c = conn.cursor()


def make_subject_map(data):
    return {
        "id": data[0],
        "name": data[1],
        "professor.id": data[2],
    }


def select_subject_by_id_from_db(id):
    return c.execute("select id, name, professor_id where id = (?)", (id, )).fetchone()


def insert_subject_to_db(id, name, professor):
    return c.execute("insert into subject values(?,?,?)", (id, name, professor.id))


def create_subject(id, name, professor):
    return make_subject_map(insert_subject_to_db(id, name, professor))


def get_subject_by_id(id):
    data = select_subject_by_id_from_db(id)
    return make_subject_map(data)


def insert_register_class_to_db(student_id, subject_id):
    return c.execute("insert into register_class (student_id, subject_id) values (?,?)", (student_id, subject_id))


def delete_from_subject_by_id(id):
    return c.execute("delete from subject where id = (?)", (id,))


def delete_from_register_class_by_subject_id(subject_id):
    return c.execute("delete from register_class where subject_id = (?)", (subject_id,))


def update_register_class_set_grade_by_student_id_and_subject_id(score, student_id, subject_id):
    return c.execute("update register_class set grade = (?) where student_id = (?) and subject_id = (?)", (score, student_id, subject_id))


def get_grade_by_subject_id_and_student_id(subject_id, student_id):
    return c.execute("select register_class.grade from register_class "
                     "join subject on register_class.subject_id = subject.id "
                     "join student on register_class.student_id = student.id "
                     "where subject.id = (?) and student.id = (?)", (subject_id, student_id)).fetchall()


def check_grade(subject_id, student_id):
    if get_grade_by_subject_id_and_student_id(subject_id, student_id) == [(None,)]:
        return True
    return False


def select_student_by_grade(grade):
    return c.execute("select student.id, student.name "
                     "from student join register_class on student.id = register_class.student_id "
                     "where register_class.grade = (?)", (grade,)).fetchall()


def get_students_by_set_type(grade):
    return set(select_student_by_grade(grade))


def if_subjects(id):
    return c.execute(
        "select student.id, student.name from student "
        "join register_class on student.id = register_class.student_id "
        "where register_class.subject_id in (?)", (id,)).fetchall()


def if_a_subject(id):
    return c.execute("select student.id, student.name from student "
                     "join register_class on student.id = register_class.student_id "
                     "where register_class.subject_id = (?)", (id, )).fetchall()


def make_students_with_subject_id(subject_id):
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
            delete_from_subject_by_id(self.id)
            delete_from_register_class_by_subject_id(self.id)

    def check(self, student, score):
        if score in [Score.A, Score.B, Score.C]:
            if student in self.sub_stu:
                self.score[student] = score
                update_register_class_set_grade_by_student_id_and_subject_id(score, student.id, self.id)
        else:
            raise Exception('잘못된 점수입니다.')

    def __repr__(self):
        return f'({self.id} - {self.name} - {self.professor} - {self.limit})'


def get_professor_obj_by_id(id):
    professor_name = c.execute("select name from professor").fetchone()[0]
    return Pro(id=id, name=professor_name)


def get_subject_obj_by_id(id):
    data = get_subject_by_id(id)
    return Subject(id=data["id"], name=data["name"], professor=get_professor_obj_by_id(data["professor.id"]))


class Score:
    A = 'A'
    B = 'B'
    C = 'C'
