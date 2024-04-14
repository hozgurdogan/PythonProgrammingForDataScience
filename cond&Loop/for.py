###################################
# FOR Döngüsü (FOR Loop)
###################################

# Öğrenci listesi tanımlama (Defining a list of students)
students = ["John", "Mark", "Vanessa", "Mariam"]

# Listenin elemanlarını tek tek dönen ve her birini büyük harfe çeviren döngü (Loop through the list elements and convert each to uppercase)
i = 0  # Index için sayaç tanımlama (Initializing counter for index)
for student in students:
    # Öğrencinin ismini yazdırma (Printing the student's name)
    print(student, end=" ")  # Öğrenci ismini yan yana yazdırma (Print student names side by side)

    # Öğrencinin ismini büyük harflerle güncelleme (Updating the student's name to uppercase)
    student = student.upper()

    # Liste içerisindeki öğrencinin ismini büyük harfe çevirip güncelleme (Updating the list with the student's name in uppercase)
    students[i] = student
    i = i + 1  # Index'i arttırma (Incrementing the index)

# Boş bir satır yazdırma (Printing a blank line for separation)
print(" ")

# Listenin güncellenmiş haliyle tekrar döngü (Looping again with the updated list)
for student in students:
    # Güncellenmiş öğrenci isimlerini yazdırma (Printing the updated student names)
    print(student, end=" ")  # Öğrenci isimlerini yan yana yazdırma (Print student names side by side)
