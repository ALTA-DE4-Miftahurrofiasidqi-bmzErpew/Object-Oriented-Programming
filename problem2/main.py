# tulis solusi code disini


class Bangun_ruang:
    def volume(self):
        return 0


class Kubus(Bangun_ruang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi**3


class Balok(Bangun_ruang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi


class Tabung(Bangun_ruang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def volume(self):
        luas_lingkaran = (self.jari_jari**2) * 22 / 7
        return int(self.tinggi * luas_lingkaran)


def hitung_volume(name, bangun_ruang):
    volume = bangun_ruang.volume()
    print(f"{name} : {volume}")


new_kubus = Kubus(10)
new_balok = Balok(3, 6, 10)
new_tabung = Tabung(7, 10)

hitung_volume("Kubus", new_kubus)
hitung_volume("Balok", new_balok)
hitung_volume("Tabung", new_tabung)
