def metini_degisitirme(girilen_metin):
    """
    Verilen metinde, çift indeksli karakterleri büyük harfe,
    tek indeksli karakterleri küçük harfe dönüştürür.

    Args:
        girilen_metin (str): Değiştirilecek metin.

    Returns:
        str: Her bir çift indeksli karakteri büyük harf,
             tek indeksli karakteri küçük harf yapılmış yeni metin.
    """

    new_string = ""  # Yeni metni saklamak için boş bir string oluştur.
    i = 0  # Harflerin hangi indekste olduğunu kontrol etmek amacı ile bir sayaç oluştur.

    # Girilen metin üzerinde döngü kur ve her karakter için:
    for harf in girilen_metin:
        # Eğer indeks çift ise:
        if i % 2 == 0:
            new_string = new_string + harf.upper()  # Karakteri büyük harfe çevir ve yeni stringe ekle.
        else:
            new_string = new_string + harf.lower()  # Karakteri küçük harfe çevir ve yeni stringe ekle.
        i = i + 1  # İndeksi bir artır.

    return new_string  # Dönüştürülmüş yeni stringi döndür.


# Kullanıcıdan metin girmesini iste (Request a text input from the user)
girilen_metin = str(input("Lütfen bir metin giriniz: "))

# Girilen metni dönüştür ve yazdır (Convert the entered text and print it)
print(metini_degisitirme(girilen_metin))
