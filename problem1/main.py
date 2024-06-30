# tulis solusi code disini
import math


class Bangun_datar:
    def luas(self):
        return 0

    def keliling(self):
        return 0


class Persegi(Bangun_datar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

    def keliling(self):
        return self.sisi * 4


class Segi_tiga(Bangun_datar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return int(self.alas * self.tinggi / 2)

    def keliling(self):
        sisi_miring = math.sqrt((self.alas**2) + (self.tinggi**2))
        return int(self.alas + self.tinggi + sisi_miring)


class Persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return (self.panjang + self.lebar) * 2


persegi = Persegi(4)
segitiga = Segi_tiga(3, 4)
persegi_panjang = Persegi_panjang(7, 8)

print("Luas")
print(f"Persegi : {persegi.luas()}")
print(f"Segitiga : {segitiga.luas()}")
print(f"Persegi Panjang : {persegi_panjang.luas()}")
print("\n")

print("Keliling")
print(f"Persegi : {persegi.keliling()}")
print(f"Segitiga : {segitiga.keliling()}")
print(f"Persegi Panjang : {persegi_panjang.keliling()}")
