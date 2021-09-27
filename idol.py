class Idol:
    def __init__(self, group_name):
        self.group_name = group_name
        self.member = []
        self.new_album = None
        self.released_album = []

    def debut_idol(self, name):
        self.member.append(name)

    def release_album(self, album_name, *song):  # 앨범 발매
        self.new_album = {album_name: song}
        self.released_album.append(self.new_album)
        return self.new_album

    def perform(self):
        album_name = list(self.new_album.keys())[0]
        title = self.new_album[album_name][0]
        return title


class Fanclub:
    def __init__(self, f_name, idol):
        self.f_name = f_name
        self.idol = idol
        self.fanclub_member = []
        self.name = None

    def join(self, name):
        self.name = name
        self.fanclub_member.append(name)
        return self.f_name + "가입완료"

    def support(self):
        print(self.f_name + "로서 " + self.idol + "을(를) 응원합니다.")


class BroadcastingCorporation:
    def music_show(self, idol):
        return idol.perform()


class BubbleChat:
    def bb_with(self, idol):
        return idol.group_name + "와 버블하기"


if __name__ == "__main__":
    sj = Idol('슈퍼주니어')
    sj.debut_idol('동해')
    sj.debut_idol('은혁')
    sj.debut_idol('신동')
    print(sj.member)
    sj.release_album("정규 1집", "쏘리쏘리", "어쩌구 저쩌구", "이러쿵 저러쿵")
    sj.release_album("정규 2집", "미인아", "어쩌구 저쩌구", "이러쿵 저러쿵")
    print(sj.new_album)
    print(sj.released_album)  # 발매된 앨범

    elf = Fanclub('엘프', sj.group_name)
    elf.join('김엘프')
    elf.join('이엘프')
    print(elf.fanclub_member)
    elf.support()

    mbc = BroadcastingCorporation()
    print(mbc.music_show(sj))

    sj_bb = BubbleChat()
    print(sj_bb.bb_with(sj))



