import random
from datetime import datetime
import sqlite3

conn = sqlite3.connect('vet_sys.db')
cur = conn.cursor()


def insert_visitor_to_db(animal):
    return cur.execute("insert into visitor values(?)", (animal.id,))


def select_visitor_all_from_db():
    return cur.execute("select animal_id from visitor").fetchall()


class Visitor:
    def __init__(self, animal):
        self.animal = animal  # animal obj
        self.animals = [animal]
        self.situation = "진료대기중"

    def register_another_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
        self.animal = animal
        return self.animal

    def __repr__(self):
        return self.animal


def make_animal_map(data):
    return {
        "id": data[0],
        "animal_type": data[1],
        "condition": data[2],
    }


def insert_animal_to_db(id, animal_type, condition):
    return cur.execute("insert into animal(id, type, condition) values(?,?,?)", (id, animal_type, condition))


def select_animal_from_db(animal_id):
    return cur.execute("select id, type, condition from animal where id = (?)", (animal_id, )).fetchone()


def get_animal(animal_id):
    data = select_animal_from_db(animal_id)
    return make_animal_map(data)


def create_animal(id, animal_type, condition):
    data = get_animal(insert_animal_to_db(id, animal_type, condition).lastrowid)
    return Animal(id=data["id"], animal_type=data["animal_type"], condition=data["condition"])


class Animal:
    def __init__(self, id, animal_type, condition):
        self.id = id
        self.animal_type = animal_type
        self.condition = condition
        self.symptoms = ()
        self.chart = []

    def check_symptoms(self, *symptoms):
        self.symptoms = symptoms

    def __repr__(self):
        return f'({self.id} - {self.animal_type})'


class AnimalType:
    DOG = "개"
    BIRD = "새"
    CAT = "고양이"
    FISH = "물고기"


class Condition:
    NORMAL = 0
    ABNORMAL = 1


class Symptom:
    COUGH = "기침"
    FEVER = "고열"
    DIARRHEA = "설사"
    UNCLEAR_EYES = "탁한 눈"
    HAIR_LOSS = "탈모"
    DEAD_SKIN_CELL = "피부 각질"
    DROOLING = "침흘림"


def insert_vet_to_db(staff):
    return cur.execute("insert into vet values(?)", (staff.license_number,))


def select_vet_all_from_db():
    return cur.execute("select staff_id from vet").fetchall()


class Vet:
    def __init__(self, *staff):
        self.staff = (staff,)
        self.rest_room = 5
        self.room_info = {}


def doctor_license_number():
    license_number = random.randint(10000, 99999)
    global doctor_license_number_list
    doctor_license_number_list = list(range(10000, 100000))
    while license_number in doctor_license_number_list:
        if license_number in doctor_license_number_list:
            doctor_license_number_list.remove(license_number)
            return license_number
        else:
            license_number = random.randint(10000, 99999)


def nurse_license_number():
    license_number = random.randint(100, 999)
    global nurse_license_number_list
    nurse_license_number_list = list(range(100, 1000))
    while license_number in nurse_license_number_list:
        if license_number in nurse_license_number_list:
            nurse_license_number_list.remove(license_number)
            return license_number
        else:
            license_number = random.randint(100, 999)


class Gender:
    MALE = 0
    FEMALE = 1


class Staff:
    def __init__(self, career, gender, salary):
        self.career = career
        self.gender = gender
        self.salary = salary


class DiseaseName:
    COLD = "감기"
    FLU = "독감"
    ENTERITIS = "장염"
    FOOD_POISONING = "식중독"
    CATARACT = "백내장"
    STRESS = "스트레스"
    SKIN_DISEASE = "피부병"


class Treatment:
    MEDICINE = "감기약"
    INJECTION = "독감 주사"
    HOSPITALIZATION = "입원 치료"
    SURGERY = "수술"
    OINTMENT = "피부 연고"


def write_disease(symptoms):
    if symptoms == (Symptom.COUGH,):
        return DiseaseName.COLD
    elif symptoms == (Symptom.COUGH, Symptom.FEVER):
        return DiseaseName.FLU
    elif symptoms == (Symptom.DIARRHEA,):
        return DiseaseName.ENTERITIS
    elif symptoms == (Symptom.DIARRHEA, Symptom.FEVER):
        return DiseaseName.FOOD_POISONING
    elif symptoms == (Symptom.UNCLEAR_EYES,):
        return DiseaseName.CATARACT
    elif symptoms == (Symptom.HAIR_LOSS,) or symptoms == (Symptom.DROOLING,) or symptoms == (
            Symptom.HAIR_LOSS, Symptom.DROOLING):
        return DiseaseName.STRESS
    elif symptoms == (Symptom.DEAD_SKIN_CELL,):
        return DiseaseName.SKIN_DISEASE


def write_treatment(disease):
    if disease == DiseaseName.COLD:
        return Treatment.MEDICINE
    elif disease == DiseaseName.FLU:
        return Treatment.INJECTION
    elif disease == DiseaseName.ENTERITIS or disease == DiseaseName.FOOD_POISONING or disease == DiseaseName.STRESS:
        return Treatment.HOSPITALIZATION
    elif disease == DiseaseName.CATARACT:
        return Treatment.SURGERY
    elif disease == DiseaseName.SKIN_DISEASE:
        return Treatment.OINTMENT


def make_staff_map(data):
    return {
        "id": data[0],
        "career": data[1],
        "gender": data[2],
        "salary": data[3],
    }


def insert_doctor_to_db(career, gender, salary):
    return cur.execute("insert into doctor(id, career, gender, salary) values(?,?,?,?)"
                       , (doctor_license_number(), career, gender, salary))


def select_doctor_from_db(doctor_id):
    return cur.execute("select id, career, gender, salary from doctor where id = (?)", (doctor_id,)).fetchone()


def get_doctor(doctor_id):
    data = select_doctor_from_db(doctor_id)
    return make_staff_map(data)


def create_doctor(career, gender, salary):
    data = get_doctor(insert_doctor_to_db(career, gender, salary).lastrowid)
    return Doctor(career=data["career"], gender=data["gender"], salary=data["salary"], license_number=data["id"])


class Doctor(Staff):
    def __init__(self, career, gender, salary, license_number=doctor_license_number()):
        super().__init__(career, gender, salary)
        self.license_number = license_number

    def treat(self, visitor):
        visitors_animal = visitor.animal
        symptoms = visitor.animal.symptoms
        disease_name = write_disease(symptoms)
        visitors_animal.chart.append({disease_name: write_treatment(disease_name)})
        visitor.situation = "진료완료"


def get_doctor_obj(doctor_id):
    data = get_doctor(doctor_id)
    return Doctor(career=data["career"], gender=data["gender"], salary=data["salary"], license_number=data["id"])


def insert_nurse_to_db(career, gender, salary):
    return cur.execute("insert into nurse (id, career, gender, salary) values(?,?,?,?)"
                       , (nurse_license_number(), career, gender, salary))


def select_nurse_from_db(nurse_id):
    return cur.execute("select id, career, gender, salary from nurse where id = (?)", (nurse_id,)).fetchone()


def get_nurse(nurse_id):
    data = select_nurse_from_db(nurse_id)
    return make_staff_map(data)


def create_nurse(career, gender, salary):
    data = get_nurse(insert_nurse_to_db(career, gender, salary).lastrowid)
    return Nurse(career=data["career"], gender=data["gender"], salary=data["salary"], license_number=data["id"])


def recovery(animal_id): # 왜 적용이 안되지
    return cur.execute("update animal set condition = (?) where id = (?)", (Condition.NORMAL, animal_id))


class Nurse(Staff):
    def __init__(self, career, gender, salary, license_number=nurse_license_number()):
        super().__init__(career, gender, salary)
        self.license_number = license_number

    def accept_payment(self, visitor):
        pay = input("수납하실 돈을 넣어주세요 : ")
        if pay != "":
            visitor.situation = "수납완료"

    def after_doctor_treat(self, visitor, vet):
        today_chart = visitor.animal.chart[-1]
        for disease, treatment in today_chart.items():
            if treatment == Treatment.HOSPITALIZATION:
                self.hospitalize(visitor, vet)
            else:
                visitor.situation = "수납대기중"
                print(visitor.situation)
                self.accept_payment(visitor)

    def hospitalize(self, visitor, vet):
        if vet.rest_room > 0:
            vet.rest_room -= 1
            visitor.situation = "입원완료"
            vet.room_info[visitor.animal.id] = "입원날짜 - {}, 입원 예정 기간 - {}일" \
                .format(datetime.today().strftime("%Y/%m/%d"), random.randint(1, 3))
        else:
            visitor.situation = "입원대기중"

    def discharge(self, visitor, vet):
        visitor.situation = "수납대기중"
        print(visitor.situation)
        vet.rest_room += 1
        recovery(visitor.animal.id)  # 안되는 중..
        self.accept_payment(visitor)


def get_nurse_obj(nurse_id):
    data = get_nurse(nurse_id)
    return Nurse(career=data["career"], gender=data["gender"], salary=data["salary"], license_number=data["id"])


if __name__ == "__main__":
    cat1 = create_animal(2, AnimalType.CAT, Condition.ABNORMAL)
    cat1.check_symptoms(Symptom.COUGH, Symptom.FEVER)
    v1 = Visitor(cat1)
    insert_visitor_to_db(cat1)
    print(cat1.id)
    print(cat1.condition)
    recovery(cat1.id)
    print(cat1.condition)

    d1 = create_doctor(1, Gender.FEMALE, 3000)
    n1 = create_nurse(2, Gender.FEMALE, 3000)

    vet1 = Vet(d1, n1)
    insert_vet_to_db(d1)
    insert_vet_to_db(n1)

    d1.treat(v1)
    print(v1.situation)
    print(v1.animal.chart)

    n1.after_doctor_treat(v1, vet1)
    print(v1.situation)

    bird1 = create_animal(3, AnimalType.BIRD, Condition.ABNORMAL)
    bird1.check_symptoms(Symptom.DIARRHEA)
    print(bird1.condition)

    v1.register_another_animal(bird1)
    insert_visitor_to_db(bird1)

    d1.treat(v1)
    print(v1.animal.chart)
    print(v1.situation)

    n1.after_doctor_treat(v1, vet1)
    print(v1.situation)
    print(vet1.rest_room)
    print(vet1.room_info)

    n1.discharge(v1, vet1)
    print(v1.situation)

    recovery(bird1.id)
    print(bird1.condition)





