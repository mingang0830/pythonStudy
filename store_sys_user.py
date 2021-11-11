import sqlite3
conn = sqlite3.connect("student_system.db")
c = conn.cursor()


def make_user_map(data):
    return {
        "id": data[0],
        "name": data[1],
    }


def get_student_name(student_id):
    return c.execute("select name from student where id = (?)", (student_id,)).fetchone()[0]


def get_register_class_of_student_from_db(student_id):
    return c.execute(
        "select subject.id, subject.name, professor.name, register_class.grade "
        "from register_class join subject on register_class.subject_id = subject.id "
        "join professor on subject.professor_id = professor.id "
        "where register_class.student_id = (?)", (student_id,)).fetchall()


def make_student_info(student_id):
    return {get_student_name(student_id): get_register_class_of_student_from_db(student_id)}


def select_student_all_from_db():
    return c.execute("select id, name from student").fetchall()


def select_student_from_db(student_id):
    return c.execute("select id, name from student where id = (?)", (student_id,)).fetchone()


def insert_student_to_db(student_id, name):
    return c.execute("insert into student values(?,?)", (student_id, name))


def get_student(student_id):
    data = select_student_from_db(student_id)
    return make_user_map(data)


def create_student(student_id, name):
    return make_user_map(insert_student_to_db(student_id, name))


class Student:
    def __init__(self, id , name):
        self.id = id
        self.name = name
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


def get_student_obj(student_id):
    data = get_student(student_id)
    return Student(id=data["id"], name=data["name"])


def professor_info_from_db(id):
    return c.execute(
        "select professor.name, subject.id, subject.name, count(register_class.student_id) "
        "from professor join subject on professor.id = subject.professor_id "
        "join register_class on subject.id = register_class.subject_id where subject.professor_id = (?)", (id,)).fetchall()


def select_professor_all_from_db():
    return c.execute("select id, name from professor").fetchall()


def select_professor_from_db(professor_id):
    return c.execute("select id, name from professor where id = (?)", (professor_id,)).fetchone()


def insert_professor_to_db(professor_id, name):
    c.execute("insert into professor values(?,?)", (professor_id, name))


def get_professor(professor_id):
    data = select_professor_from_db(professor_id)
    return make_user_map(data)


def create_professor(professor_id, name):
    return make_user_map(insert_professor_to_db(professor_id, name))


class Pro:
    def __init__(self, id, name):
        self.subject = []
        self.name = name
        self.id = id

    def open_sub(self, id, name, limit):
        my_sub = Subject(id, name, self, limit)
        self.subject.append(my_sub)
        return my_sub

    def __repr__(self):
        return self.name


def get_professor_obj(professor_id):
    data = get_professor(professor_id)
    return Pro(id=data["id"], name=data["name"])

