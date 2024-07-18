def decorator(fonk):
    def wrapper():
        print("Fonksiyon çalışmadan önce ki işlemler")
        fonk()
        print("Fonksiyon çalıştırıldıktan sonra ki işlemler")
    return wrapper
@decorator
def fonksiyon():
    print("Fonksiyon çalışıyor")

fonksiyon()
