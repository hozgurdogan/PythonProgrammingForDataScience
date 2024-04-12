# Tuple oluşturma (Creating a tuple)
my_tuple = (1, 2, 3, "apple", "banana")

# Tuple içeriğini yazdırma (Printing tuple contents)
print("Original Tuple:", my_tuple)

# Tuple elemanlarına erişim (Accessing elements of a tuple)
print("First element:", my_tuple[0])  # İlk eleman (first element)
print("Last element:", my_tuple[-1])  # Son eleman (last element)

# Tuple dilimleme (Slicing a tuple)
print("First three elements:", my_tuple[:3])  # İlk üç eleman (first three elements)

# Tuple içinde eleman kontrolü (Checking if an item exists in a tuple)
if "apple" in my_tuple:
    print("Apple is in the tuple")

# Tuple uzunluğunu öğrenme (Finding the length of a tuple)
print("Length of tuple:", len(my_tuple))

# Tek elemanlı tuple (Single element tuple)
single_element_tuple = ("single",)  # Virgül önemli! (Comma is important!)
print("Single element tuple:", single_element_tuple)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked:", a, b, c, d, e)

# Tuple içerisinde eleman sayısını sayma (Counting elements in a tuple)
print("Number of times 2 appears:", my_tuple.count(2))

# Elemanın indeksini bulma (Finding index of an element)
print("Index of 'banana':", my_tuple.index("banana"))

# Immutable özelliğini test etme (Testing the immutability)
try:
    my_tuple[0] = 99  # Hata verir çünkü tuple değiştirilemez (throws an error because tuples are immutable)
except TypeError as e:
    print("Error:", e)
