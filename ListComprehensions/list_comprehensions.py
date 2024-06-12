#################################################
# COMPREHENSION 
#################################################
 










#################################################
#List Comprehension 
##################################################

def new_salary(salary):
    return salary * 20 / 100 + salary 

null_list = []


salaries = [1000 , 2000, 3000, 4000, 5000]
for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

for salary in null_list:
    print("Maas :" + str(salary ))


list2 = [salary*2 for salary in salaries if salary<3000]

for salary in list2:
    print("Liste2 Maas :" + str(salary ))

list3 = [salary*2 if salary<3000 else salary*0  for salary in salaries ]
for salary in list3:
    print("List Maas :" + str(salary ))


list4 = [new_salary(salary*2) if salary<3000 else new_salary(salary*0.2)  for salary in salaries ]

for salary in list4:
    print("List Maas :" + str(salary ))
