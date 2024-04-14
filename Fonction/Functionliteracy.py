#################
# Fonksiyon Okur Yazarlığı (Function Literacy)
#################

# Tek bir harf yazdırma (Printing a single letter)
print("A")
# `print` fonksiyonunun kullanımına ilişkin yardım almak için help(print) fonksiyonu kullanılabilir.
# (Use help(print) to get help on the usage of the `print` function)

# İki harfi yan yana yazdırma (Printing two letters side by side)
print("A", "B")

# İki harf arasına belirli bir ayraç ekleyerek yazdırma (Printing two letters with a custom separator)
print("A", "B", sep="__")

# `print` fonksiyonuna ilişkin detaylı yardım almak için yorumu kaldırın (Uncomment to get detailed help about the `print` function)
#help(print)


##########################
# Fonksiyon Oluşturma (Creating Functions)
##########################

# Bir sayıyı iki ile çarpan fonksiyon (Function to multiply a number by two)
def iki_ile_carp(girilen_sayi):
    return girilen_sayi * 2

# İki sayıyı toplayan fonksiyon (Function to sum two numbers)
def summer(girilen_sayi1, girilen_sayi2):
    sum_value = girilen_sayi1 + girilen_sayi2
    ekran_ciktisi = "girilen sayilarin toplamı " + str(sum_value)  # Toplam sonucunu içeren bir mesaj oluşturma (Creating a message containing the sum result)
    return ekran_ciktisi


# Kullanıcıdan bir sayı alarak çarpma işlemi yapma (Getting a number from the user to perform multiplication)
sayi1 = int(input("Lütfen 2 ile çarpım yapmak istediğiniz bir sayı giriniz:"))
print(iki_ile_carp(sayi1))  # Fonksiyonu çağırarak sonucu yazdırma (Calling the function and printing the result)

# Kullanıcıdan iki sayı alarak toplama işlemi yapma (Getting two numbers from the user to perform addition)
sayi2 = int(input("Lütfen toplama yapmak için bir sayı daha giriniz:"))
print(summer(sayi1, sayi2))  # İki sayıyı toplayan fonksiyonu çağırma ve sonucu yazdırma (Calling the function to sum two numbers and printing the result)
