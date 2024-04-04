# Character Strings (Karakter Dizileri)

#####################################

print("John")  # İngilizce ismi yazdırır

print('john')  # Küçük harfle ismi yazdırır

"John"  # Bu satırda John string'i yazılır ama herhangi bir çıktı üretmez

name = "John"  # 'name' değişkenine 'John' değerini atar
print(name)  # 'name' değişkeninin değerini yazdırır


###################################
# Multi-Line Strings (Çok Satırlı Karakter Dizileri)
###################################

# Uzun bir string'i üç tırnak işareti kullanarak birden çok satıra yayabiliriz
long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
Liste, Sözlük (Dictionary), Demet (Tuple), Küme (Set),
Mantıksal Değerler (TRUE-FALSE): bool"""

# Character string elements access (Karakter dizisi elemanlarına erişim)

name = "Name"  # 'name' değişkenine 'Name' değerini atar

name[0]  # 'N' harfine erişir
name[1]  # 'a' harfine erişir
name[2]  # 'm' harfine erişir
name[3]  # 'e' harfine erişir

# Slicing in character strings (Karakter dizilerinde dilimleme)
name = "John"  # 'name' değişkenine 'John' değerini atar
name[0:2]  # 'Jo' çıktısını üretir (0. ve 1. indeks arası karakterleri alır)

long_str[0:10]  # 'Veri Yapıla' çıktısını üretir (ilk 10 karakter)

######################################
# Searching for characters within a string (String içinde karakter arama)
######################################
"Veri" in long_str  # long_str içinde 'Veri' ifadesini arar, True veya False döner

"veri" in long_str  # Büyük/küçük harf duyarlıdır, bu nedenle False döner
