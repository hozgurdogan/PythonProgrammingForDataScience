class kisi:
    zam_orani = 1.1

    personel_sayiai = 0

    def __init__(self,isim , maas ):
        self.isim = isim
        self.maas = maas
        kisi.personel_sayiai += 1

    def bilgilerini_soyle(self): #instance Method
        return  f"Ad:{self.isim} Yas : {self.maas}"
    @classmethod
    def kisiSayisiniSoyle(cls): # class method
        return cls.personel_sayiai

    @classmethod
    def string_ileOlusutr(cls , str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)
kisi1 = kisi("Ali" , 20 )
print(f"kisi sayisi {kisi.kisiSayisiniSoyle()}")
kisi3 = kisi.string_ileOlusutr("Hasoooo-23")

print(kisi1.bilgilerini_soyle())
print(kisi3.bilgilerini_soyle())
print(f"kisi sayisi {kisi.kisiSayisiniSoyle()}")