"""! Syntex If Else

        if <condition>:
            <code>

        elif <condition>:
            <code>

        elif <condition>:
            <code>

        else:
            <code>
"""
a = 10

if a==10:
    print("value is correct")
else:
    print("value is not correct")



name = input("Enter your name: ")

if name=="rakib":
    print("My name is Rakib")

elif name=="hassan":
    print("My name is Hassan")

elif name=="tanin":
    print("My name is Tanin")

elif name=="emon":
    print("My name is Emon")

else:
    print("Anonimous  Name")



f_number = int(input("Given a first number: "))
s_number = int(input("Given a second number: "))

operator = input("Select operator (+, -, * , /, %, //, **): ")

result = 0

if operator=="+":
    result = f_number + s_number

elif operator=="-":
    result = f_number - s_number

elif operator=="*":
    result = f_number * s_number

elif operator=="/":
    result = f_number / s_number

elif operator=="%":
    result = f_number % s_number

elif operator=="//":
    result = f_number // s_number

elif operator=="**":
    result = f_number ** s_number

else:
    print("Invalid Operator Selected!")


print("My Result: ", result)



import re
cgpa = float(input("Give your CGPA:"))

if cgpa < 2.0 :
    print(f"Your GPA = {cgpa}, so, your grade: F")

elif cgpa >=2.0 and cgpa <2.25 :
    print(f"Your GPA = {cgpa}, so, your grade = D")

elif cgpa >=2.25 and cgpa <2.50 :
    print(f"Your GPA = {cgpa}, so, your grade = C")

elif cgpa >=2.50 and cgpa <2.75 :
    print(f"Your GPA = {cgpa}, so, your grade = C+")

elif cgpa >=2.75 and cgpa <3.00 :
    print(f"Your GPA = {cgpa}, so, your grade = B-")

elif cgpa >=3.00 and cgpa <3.25 :
    print(f"Your GPA = {cgpa}, so, your grade = B")

elif cgpa >=3.25 and cgpa <3.50 :
    print(f"Your GPA = {cgpa}, so, your grade = B+")

elif cgpa >=3.50 and cgpa <3.75 :
    print(f"Your GPA = {cgpa}, so, your grade = A-")

elif cgpa >=3.75 and cgpa <4 :
    print(f"Your GPA = {cgpa}, so, your grade = A")

elif cgpa == 4:
    print(f"Your GPA = {cgpa}, so, your grade = A+")

else:
    print("Invalid CGPA")



 