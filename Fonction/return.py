def calculate(varm, moisture, charge):
    """
    Belirtilen değişkenleri işleyip dört farklı değer döndürür.

    Args:
        varm (int, float): İlk değer.
        moisture (int, float): İkinci değer.
        charge (int, float): Üçüncü değer.

    Returns:
        tuple: İşlenmiş varm, moisture, charge ve hesaplanan sonuç içeren bir tuple döner.

    Processes the given variables and returns four different values.

    Args:
        varm (int, float): The first value.
        moisture (int, float): The second value.
        charge (int, float): The third value.

    Returns:
        tuple: A tuple containing the processed varm, moisture, charge, and the calculated output.
    """
    # Verilen değerleri işleme (Processing the given values)
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    # Değerleri bir tuple olarak döndürme (Returning the values as a tuple)
    return varm, moisture, charge, output

# Fonksiyonun kullanımı (Using the function)
# Fonksiyonu çağır ve döndürülen değerleri değişkenlere ata (Call the function and assign the returned values to variables)
result = calculate(98, 12, 78)
print(result)  # Çıktı: (196, 24, 156, 1.4102564102564104)

# Fonksiyonun dönüş tipini kontrol etme (Checking the type of the function return)
print(type(result))  # Çıktı: <class 'tuple'>

# Döndürülen değerleri ayrı ayrı değişkenlere ata (Assign the returned values to separate variables)
varm, moisture, charge, output = calculate(98, 12, 78)
print(varm, moisture, charge, output)  # Çıktı: 196 24 156 1.4102564102564104
