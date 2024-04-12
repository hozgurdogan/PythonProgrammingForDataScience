# Set oluşturma (Creating a set)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Set içeriğini yazdırma (Printing set contents)
print("Set 1:", set1)
print("Set 2:", set2)

# Set'e eleman ekleme (Adding elements to a set)
set1.add(6)  # 6 sayısını set1'e ekler (adds 6 to set1)
print("Set 1 after adding:", set1)

# Set'ten eleman çıkarma (Removing elements from a set)
set1.remove(6)  # 6 sayısını set1'den çıkarır, eleman yoksa hata verir (removes 6 from set1, throws an error if the element does not exist)
print("Set 1 after removing:", set1)

# Set'ten eleman çıkarma, eleman yoksa sessizce geç (Discard element from set, pass silently if the element does not exist)
set1.discard(10)  # 10 yoksa hata vermez (does not throw an error if 10 is not present)
print("Set 1 after discarding:", set1)

# Set'ten rastgele bir eleman çıkar (Remove a random element from a set)
element = set1.pop()  # set boş ise KeyError verir (throws KeyError if set is empty)
print("Popped element:", element)
print("Set 1 after pop:", set1)

# Set içinde eleman kontrolü (Check if an element is in a set)
print(2 in set1)  # 2 set1'in bir elemanı mı diye kontrol eder, True/False döner (checks if 2 is an element of set1, returns True/False)

# Set birleşimi (Union of sets)
union_set = set1.union(set2)  # set1 ve set2'nin birleşimini döner (returns the union of set1 and set2)
print("Union of set1 and set2:", union_set)

# Set kesişimi (Intersection of sets)
intersection_set = set1.intersection(set2)  # set1 ve set2'nin kesişimini döner (returns the intersection of set1 and set2)
print("Intersection of set1 and set2:", intersection_set)

# Set farkı (Difference of sets)
difference_set = set1.difference(set2)  # set1'den set2'yi çıkarır (subtracts set2 from set1)
print("Difference of set1 from set2:", difference_set)

# Set simetrik farkı (Symmetric difference of sets)
symmetric_difference_set = set1.symmetric_difference(set2)  # İki set arasındaki simetrik farkı döner (returns the symmetric difference between two sets)
print("Symmetric difference between set1 and set2:", symmetric_difference_set)

# Set güncelleme (Update a set)
set1.update([10, 11, 12])  # set1'e birden fazla eleman ekler (adds multiple elements to set1)
print("Set 1 after update:", set1)

# Set kesişimini güncelleme (Update set intersection)
set1.intersection_update([1, 2, 10, 11])  # set1'in sadece belirtilen elemanlarla kesişimini saklar (keeps only the elements of set1 that are mentioned)
print("Set 1 after intersection update:", set1)

# Set farkını güncelleme (Update set difference)
set1.difference_update([2])  # set1'den belirtilen elemanları çıkarır (removes the specified elements from set1)
print("Set 1 after difference update:", set1)

# Setin alt kümesi olup olmadığını kontrol etme (Check if a set is a subset of another)
is_subset = {1, 11}.issubset(set1)  # {1, 11} set1'in bir alt kümesi mi diye kontrol eder (checks if {1, 11} is a subset of set1)
print("Is {1, 11} a subset of set1?", is_subset)

# Setin süper kümesi olup olmadığını kontrol etme (Check if a set is a superset of another)
is_superset = set1.issuperset({1, 11})  # set1 {1, 11}'in bir süper kümesi mi diye kontrol eder (checks if set1 is a superset of {1, 11})
print("Is set1 a superset of {1, 11}?", is_superset)

# İki setin ayrık (disjoint) olup olmadığını kontrol etme (Check if two sets are disjoint)
are_disjoint = set1.isdisjoint(set2)  # set1 ve set2'nin ortak hiç elemanı yoksa True döner (returns True if set1 and set2 have no common elements)
print("Are set1 and set2 disjoint?", are_disjoint)

# Set temizleme (Clear all elements from a set)
set1.clear()
print("Set 1 after clear:", set1)
