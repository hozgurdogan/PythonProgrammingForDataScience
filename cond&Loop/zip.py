# Öğrenci isimlerini içeren liste
students = ["Jhon", "Mark", "Venessa", "Mariam"]

# Bölüm isimlerini içeren liste
departments = ["mathematics", "statistics", "physics", "astronomy"]

# Öğrenci yaşlarını içeren liste
ages = [23, 30, 26, 22]

# Üç listeyi zip fonksiyonu ile birleştirerek her bir öğrenciyi, bölümünü ve yaşını bir araya getiriyoruz
s = list(zip(students, departments, ages))

# Ziplenmiş listeyi döngü ile yazdırma
for student, department, age in s:
    # Her bir öğrenci için, ismini, bölümünü ve yaşını formatlı bir şekilde yazdırıyoruz
    print(f"Student: {student}, Department: {department}, Age: {age}")
