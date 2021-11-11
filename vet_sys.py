import random
from datetime import datetime


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


class Animal:
    def __init__(self, id, name, animal_type, condition):
        self.id = id
        self.name = name
        self.animal_type = animal_type
        self.condition = condition
        self.symptoms = ()
        self.chart = []

    def check_symptoms(self, *symptoms):
        self.symptoms = symptoms

    def __repr__(self):
        return f'({self.name} - {self.animal_type})'


class AnimalType:
    DOG = "개"
    BIRD = "새"
    CAT = "고양이"
    FISH = "물고기"


class Condition:
    NORMAL = True
    ABNORMAL = False


class Symptom:
    COUGH = "기침"
    FEVER = "고열"
    DIARRHEA = "설사"
    UNCLEAR_EYES = "탁한 눈"
    HAIR_LOSS = "탈모"
    DEAD_SKIN_CELL = "피부 각질"
    DROOLING = "침흘림"


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
    MALE = "남성"
    FEMALE = "여성"


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


class Doctor(Staff):
    def __init__(self, career, gender, salary):
        super().__init__(career, gender, salary)
        self.license_number = "doc-{}".format(doctor_license_number())

    def treat(self, visitor):
        visitors_animal = visitor.animal
        symptoms = visitor.animal.symptoms
        disease_name = write_disease(symptoms)
        visitors_animal.chart.append({disease_name: write_treatment(disease_name)})
        visitor.situation = "진료완료"


class Nurse(Staff):
    def __init__(self, career, gender, salary):
        super().__init__(career, gender, salary)
        self.license_number = "nur-{}".format(nurse_license_number())

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
        visitor.animal.condition = Condition.NORMAL
        self.accept_payment(visitor)


if __name__ == "__main__":
    cat1 = Animal(1, "키티", AnimalType.CAT, Condition.ABNORMAL)
    cat1.check_symptoms(Symptom.COUGH, Symptom.FEVER)

    v1 = Visitor(cat1)

    d1 = Doctor(6, Gender.MALE, 3000)

    n1 = Nurse(2, Gender.FEMALE, 3000)

    vet1 = Vet(d1, n1)
    print(vet1.staff)

    d1.treat(v1)
    print(v1.situation)
    print(v1.animal.chart)

    n1.after_doctor_treat(v1, vet1)
    print(v1.situation)

    bird1 = Animal(2, "짹짹이", AnimalType.BIRD, Condition.ABNORMAL)
    bird1.check_symptoms(Symptom.DIARRHEA)

    v1.register_another_animal(bird1)

    d1.treat(v1)
    print(v1.animal.chart)
    print(v1.situation)

    n1.after_doctor_treat(v1, vet1)
    print(v1.situation)
    print(vet1.rest_room)
    print(vet1.room_info)

    n1.discharge(v1, vet1)
    print(v1.situation)

    print(vet1.rest_room)












