# tulis solusi code disini
class Pengiriman_barang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat
        self.harga_per_kg = 5000
        self.volume_minimal = 50

    def hitung_vulume(self):
        return self.tinggi * self.panjang * self.lebar

    def cek_harga(self):
        volume = self.hitung_vulume()
        if 0 < volume <= self.volume_minimal and self.berat >= 1:
            return self.harga_per_kg * self.berat
        else:
            return 0


barang = Pengiriman_barang(5, 2, 4, 1)
harga_ongkir = barang.cek_harga()

print(f"Harga : {harga_ongkir}")
