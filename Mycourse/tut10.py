#Python dictionary

Student = {"Name":"Ahmad",
 "Age":18,
  "Department":"Computer Science",
   "Registration No":5396}

x = Student.get("Name")         #Here I use get function.
print(x)

print(Student)
print(type(Student))
print(len(Student))
print(Student.keys())
# print(Student.items())
# a = Student.update("a"  "4")
# print(a)