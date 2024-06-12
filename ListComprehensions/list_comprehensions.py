#################################################
#List Comprehension
##################################################

def new_salary(salary):
    return salary * 20 / 100 + salary

null_list = []

# Örnek 1: Bir listenin her elemanını yeni bir değerle değiştirerek yeni bir liste oluşturma
salaries = [1000 , 2000, 3000, 4000, 5000]
for salary in salaries:
    null_list.append(new_salary(salary))

# Yukarıdaki işlemi list comprehension ile yapma
null_list = [new_salary(salary) for salary in salaries]

# Örnek 2: Belirli bir koşula göre liste elemanlarını değiştirerek yeni bir liste oluşturma
null_list = []
for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

# Yukarıdaki işlemi list comprehension ile yapma
null_list = [new_salary(salary) if salary > 3000 else new_salary(salary*2) for salary in salaries]

# Oluşturulan listeyi ekrana yazdırma
for salary in null_list:
    print("Maas :" + str(salary ))

# Örnek 3: List comprehension ile filtreleme yaparak yeni bir liste oluşturma
list2 = [salary*2 for salary in salaries if salary<3000]

# Oluşturulan listeyi ekrana yazdırma
for salary in list2:
    print("Liste2 Maas :" + str(salary ))

# Örnek 4: List comprehension ile koşullu ifade kullanarak yeni bir liste oluşturma
list3 = [salary*2 if salary<3000 else salary*0  for salary in salaries ]

# Oluşturulan listeyi ekrana yazdırma
for salary in list3:
    print("List Maas :" + str(salary ))

# Örnek 5: List comprehension ile karmaşık koşullu ifade kullanarak yeni bir liste oluşturma
list4 = [new_salary(salary*2) if salary<3000 else new_salary(salary*0.2)  for salary in salaries ]

# Oluşturulan listeyi ekrana yazdırma
for salary in list4:
    print("List Maas :" + str(salary ))

# Örnek 6: List comprehension ile string elemanları işleme uygulama
students = ["Jhon" , "Mark" , "Venessa" , "Mariam"]
students_no = ["Jhon" , "Venessa"]

list5 = [student.lower() if student in students_no  else student.upper() for student in students]
for student in list5:
    print("isim :" + str(student ))
