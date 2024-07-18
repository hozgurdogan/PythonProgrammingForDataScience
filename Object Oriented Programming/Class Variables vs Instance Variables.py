class calisan:
    zam_orani = 1.1

    personel_sayiai = 0

    def __init__(self,isim , maas ):
        self.isim = isim
        self.maas = maas
        calisan.personel_sayiai += 1

calisan1 = calisan("hasan" ,50000)

calisan2 = calisan("ozgur" , 80000)


calisan1.zam_orani = 1.3

print(calisan.zam_orani)

print(calisan1.zam_orani)

print(calisan2.zam_orani)


print(calisan2.__dict__)
print(calisan1.__dict__)
print(calisan.__dict__)