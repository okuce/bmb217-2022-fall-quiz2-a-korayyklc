"""Koray Kılıç 
20217170060
1.grup"""


class Otobus:

    def _init_(self, plaka, gidis, gelis, kapasite):
        self.plaka = plaka
        self.gelis = gelis
        self.gidis = gidis
        self.dolu_koltuk = 0
        self.bos_koltuk = kapasite

    def bilet_al(self):
        self.dolu_koltuk += 1
        self.bos_koltuk -= 1

    def bilet_iade(self):
        self.bos_koltuk += 1
        self.dolu_koltuk -= 1

    def durum_yaz(self):
        print(self.gidis + "," + self.gelis + "," + self.plaka + "," + self.bos_koltuk + "," + self.dolu_koltuk)
