class calisan:
    def __init__(self,name , lastname =" soy ad girilmedi", age=0):
        self.name = name
        self.lastname = lastname
        self.age = age
    def show_info(self):
        print(f"İsim {self.name}   SoyAd :{self.lastname} Yaş :{self.age} ")
calisan1 = calisan("hasan", age = 23)

calisan1.show_info()