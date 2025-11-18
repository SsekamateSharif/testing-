from student_class import student
from student_class import department 

Student_1 = student("Sharif", 2, "CSE", 21, 8)
Student_2 = student("Latif", 1, "IB", 18, 7)
Student_3 = student("Ikhsan", 3, "CSE", 23, 9)
Student_4 = student("Gravy", 3, "Medicine", 25, 6)
 
print(Student_1.name)
print(Student_2.name)
print(Student_3.name)
print(Student_4.name)
# these are the their specialities 
print(Student_1.speciality)
print(Student_2.speciality)
print(Student_3.speciality)
print(Student_4.speciality)

Department_1 = department("CSE", 150, 10, "Patel Block", "East Wing")
Department_2 = department("Medicine", 250, 20, "Gupta Block", "Central")
Department_3 = department("COBAMS", 300, 12, "CTF 1", "Western wing")
Department_4 = department("CEES", 1000, 18, "Education Block", "Southern Wing")
# printing the department names 
print(Department_1.depart_name)
print(Department_2.depart_name)
print(Department_3.depart_name)
print(Department_4.depart_name)
# printing the department blocks 
print(Department_1.Building)
print(Department_2.Building)
print(Department_3.Building)
print(Department_4.Building)
#printing the department locations 
print(Department_1.location)
print(Department_2.location)
print(Department_3.location)
print(Department_4.location)
