class Student:
    def __init__(self, name):
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


class Pro:
    def __init__(self, name):
        self.subject = []
        self.name = name

    def open_sub(self, name, desc, limit, subject_type):
        my_sub = subject_type(name, desc, self, limit)
        self.subject.append(my_sub)
        return my_sub

    def assign_essential(self, essential_subjects):
        for sub in essential_subjects:
            if sub.pro is None:
                sub.pro = self
                sub.limit = 3
                self.subject.append(sub)

    def __repr__(self):
        return self.name