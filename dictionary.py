"""informations={
    "name":"kifayat hussain",
    "subject":"pythone",
    "university":"DUET",
    "semester":"third",
    "department":"computer system engineering",

}
print(informations)
print(type(informations))
print(len(informations))
print(informations.get("name"))
semester_update={"semester":4,"CGPA":3.67}
informations.update(semester_update)
print(informations)
dictionary={"cat":"a small animal",
            "table":["a pice of furnitures","list of facts and figures"]}
print(dictionary)
print(dictionary.get("table"))
print(tuple(dictionary))
print(tuple(dictionary.get("table")))"""
#other programme
marks={}
student1=input("enter a name of student 1:")
studnt1_mark=int(input("enter a marks of student1:"))
marks[student1] = "student1_mark"
student2=input("enter a name of student 2:")
studnt2_mark=int(input("enter a marks of student 2:"))
marks[student2] = "student2_mark"
student3=input("enter a name of student 3:")
studnt3_mark=int(input("enter a marks of student 3:"))
marks[student3] = "student3_mark"
print(marks)

