#########################################
#   List (Liste)
#########################################

#- Modifiable (Değiştirilebilir)
#- Ordered, indexing is possible (Sıralıdır, İndeksleme yapılabilir)
#- Can contain multiple data types (Farklı veri tipleri içerebilir)

grades = [1, 2, 3, 4]  # Notlar
print(type(grades))

names = ['a', 'b', 'c', 'd']  # İsimler
print(type(names))

mix_list = [1, 2, 3, "a", "b", True, [1, 2, 3]]  # Karışık Liste

# Accessing list items (Liste elemanlarına erişim)
print(mix_list[0])  # First item (İlk eleman)
print(mix_list[3])  # Fourth item ('a') (Dördüncü eleman)

print(mix_list[5])  # Sixth item (True) (Altıncı eleman)
print(type(mix_list[5]))  # Checking type (Tip kontrolü)
print(mix_list[6][1])  # Second item of the nested list (İç içe listenin ikinci elemanı)
print(type(mix_list[6][1]))  # Checking type of the nested list item (İç içe listenin elemanının tip kontrolü)

mix_list[0] = 99  # Modifying the first item (İlk elemanı değiştirme)
print(mix_list[0])

print(mix_list[0:4])  # Accessing a slice of the list (Listenin bir dilimine erişim)

#########################################
#   List Methods (Liste Metotları)
#########################################

print(dir(mix_list))  # Showing list methods (Liste metodlarını gösterme)
# Append is important (Ekleme önemli)

print(len(mix_list))  # Getting the length of the list (Listenin uzunluğunu alma)

mix_list.append(100)  # Adding an item to the list (Listeye eleman ekleme)
print(mix_list)

##########################################
#   Remove an item by index (İndekse göre eleman silme)
##########################################

mix_list.pop(0)  # Removing the first item (İlk elemanı silme)
print(mix_list)

##########################################
#   Insert an item (Eleman eklemek)
##########################################

mix_list.insert(2, "Inserted here")  # Inserting into the specified index (Belirtilen indekse ekleme)
print(mix_list)
