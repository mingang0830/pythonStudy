class People:
    def __init__(self):
        self.perform_cnt = 0
        self.fanclub = None
        self.agency = None

    def perform(self):
        self.perform_cnt += 1
        if self.fanclub:
            self.fanclub.total += 50
        else:
            self.fanclub = Fanclub("test", self)

    def release_album(self, all_fanclub):
        totals = [fanclub.total for fanclub in all_fanclub]
        totals.sort(reverse=True)
        for fanclub in all_fanclub:
            try:
                if fanclub.total == totals[0]:
                    fanclub.total += 50
                elif fanclub.total == totals[1]:
                    fanclub.total += 40
                elif fanclub.total == totals[2]:
                    fanclub.total += 30
            except IndexError:
                fanclub.total += 10

    def follow_by_fanclub(self, fanclub):
        self.fanclub = fanclub


class Idol(People):
    def __init__(self, person):
        self.perform_cnt = person.perform_cnt
        self.fanclub = person.fanclub


class Group:
    def __init__(self, idol):
        self.idols = [idol]
        self.perform_cnt = 0

    def add_idol(self, idol):
        self.idols.append(idol)

    def perform(self):
        self.perform_cnt += 1


class Fanclub:
    def __init__(self, name, idol):
        self.name = name
        self.idol = idol
        self.total = 10

    def join(self, how_many):
        self.total += how_many

    def signout(self, how_many):
        tmp_total = self.total - how_many
        if tmp_total < 0:
            self.total = 0
        else:
            self.total = tmp_total


class Agency:
    def debut(self, person):
        if not person.agency and person.fanclub.total >= 50 and person.perform_cnt >= 5:
            person.agency = self
            return True
        else:
            return False

    def make_group(self, idol):
        if not idol.agency:
            return Group(idol)


if __name__ == "__main__":
    p1 = People()
    i1 = Idol(p1)
    i1.perform()
    print(i1.fanclub.name)

    p2 = People()
    i2 = Idol(p2)
    f2 = Fanclub("i2", i2)


