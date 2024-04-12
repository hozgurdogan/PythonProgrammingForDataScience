########################
# Sözlük (Dictionary)
########################

# KEY_VALUE

# Bir sözlük oluşturuluyor (Creating a dictionary)
dictionary = {
    "Reg": "Regression",  # Regresyon tanımı (Definition of Regression)
    "CART": "Classification and Regression",  # Sınıflandırma ve Regresyon tanımı (Classification and Regression definition)
    "LOG": "Logistic Regression"  # Lojistik Regresyon tanımı (Logistic Regression definition)
}

# LOG anahtarına karşılık gelen değeri yazdırma (Printing the value corresponding to the LOG key)
print(dictionary["LOG"])


# Listeler içeren bir sözlük oluşturuluyor (Creating a dictionary containing lists)
dictionary_ListForm = {
    "REG": ["Rmse", 10, 20],
    "LOG": ["MSE", 20, "Hasan"]
}
# REG anahtarına karşılık gelen listeyi yazdırma (Printing the list corresponding to the REG key)
dictionary_ListForm["REG"]

# value değerinin içindeki spesifik bir elemana ulaşmak (Accessing a specific element inside a value)
dictionary_ListForm["REG"][1]

# Key Sorgulama (Key Inquiry)
"REG" in dictionary_ListForm

# Key'e göre Value'ye erişmek (Accessing the Value by Key)
dictionary_ListForm.get("REG")

# Value değerini değiştirmek (Changing the Value)
dictionary_ListForm["REG"] = ["YSA", 100]  # YSA ve 100 değerlerine güncelleniyor (Updating to values YSA and 100)
dictionary_ListForm["REG"][1]

# Tüm key'lere ulaşmak için (To access all keys)
dictionary_ListForm.keys()

# Tüm value'lere erişmek için (To access all values)
dictionary_ListForm.values()

# Tüm key-value çiftlerine erişmek için (To access all key-value pairs)
dictionary_ListForm.items()

# Sözlüğü güncellemek için (To update the dictionary)
dictionary_ListForm.update({"REG": 11})  # REG anahtarını 11 ile güncelleme (Updating the REG key to 11)

# Güncellenmiş key-value çiftlerini yazdırma (Printing the updated key-value pairs)
dictionary_ListForm.items()
