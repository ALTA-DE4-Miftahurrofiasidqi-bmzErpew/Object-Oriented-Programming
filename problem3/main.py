# tulis solusi code disini
class Calculator:
    def __init__(self):
        pass

    def penjumlahan(self, angka_dasar, angka_oprasi):
        return angka_dasar + angka_oprasi

    def pengurangan(self, angka_dasar, angka_oprasi):
        return angka_dasar - angka_oprasi

    def perkalian(self, angka_dasar, angka_oprasi):
        return angka_dasar * angka_oprasi

    def pembagian(self, angka_dasar, angka_oprasi):
        return int(angka_dasar / angka_oprasi)


#


class Calculator:
    def __init__(self, angka_dasar, angka_oprasi):
        self.angka_dasar = angka_dasar
        self.angka_oprasi = angka_oprasi

    def hitung(self):
        pass


class Penjumlahan(Calculator):
    def __init__(self, angka_dasar, angka_oprasi):
        super().__init__(angka_dasar, angka_oprasi)

    def hitung(self):
        return self.angka_dasar + self.angka_oprasi


class Pengurangan(Calculator):
    def __init__(self, angka_dasar, angka_oprasi):
        super().__init__(angka_dasar, angka_oprasi)

    def hitung(self):
        return self.angka_dasar - self.angka_oprasi


class Perkalian(Calculator):
    def __init__(self, angka_dasar, angka_oprasi):
        super().__init__(angka_dasar, angka_oprasi)

    def hitung(self):
        return self.angka_dasar * self.angka_oprasi


class Pembagian(Calculator):
    def __init__(self, angka_dasar, angka_oprasi):
        super().__init__(angka_dasar, angka_oprasi)

    def hitung(self):
        return int(self.angka_dasar / self.angka_oprasi)


new_penjumlahan = Penjumlahan(3, 4)
new_pengurangan = Pengurangan(15, 4)
new_perkalian = Perkalian(10, 10)
new_pembagian = Pembagian(12, 3)


def perhitungan(opration_name, objek):
    hasil_oprasi = objek.hitung()
    print(f"{opration_name} : {hasil_oprasi}")


perhitungan("Penjumlahan", new_penjumlahan)
perhitungan("Pengurangan", new_pengurangan)
perhitungan("Perkalian", new_perkalian)
perhitungan("Pembagian", new_pembagian)
