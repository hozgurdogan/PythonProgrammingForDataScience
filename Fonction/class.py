class veriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

print(veriBilimci.sql)

veriBilimci.sql = 'hayır'

print(veriBilimci.sql)

veriBilimci.sql = 2
print(veriBilimci.sql)

# Sinif Orneklendirmesi (instantiation)

ozgur = veriBilimci()

ozgur.bildigi_diller.append('Python')

print(ozgur.bildigi_diller)

veli = veriBilimci()

print(veli.bildigi_diller)


# ornek özelikleri

class VeriBilimcia():
    bildigi_diller = ['R','C']
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self , yeni_dil ):
        self.bildigi_diller.append(yeni_dil)




hassoooo = VeriBilimcia()
hassoooo.bildigi_diller.append('sql')
hassoooo.bildigi_diller.append('pythonn')
hassoooo.dil_ekle('Garip dil')
print(hassoooo.bildigi_diller)
print(VeriBilimcia.bildigi_diller)


print(dir(VeriBilimcia))



# Miras yapıları

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Addres = ""

class DataScientists(Employees):
    def __init__(self):
        self.programming =""

class Marketting():
    def __init__(self):
        self.StoryTelling = ""


veribilimici1 = DataScientists()



a=3

def deneme(b):
    print(a+b)

deneme(4)