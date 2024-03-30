"""
                            Intermediate Marksheet Generator Tool

Intermediate marksheet generator tool is python based project which is used to generate intermediate marksheet for students

"""

import os


print("********** Intermediate Marksheet Generator**********")

#Input for Academic Details
roll_number = int(input("Enter Roll Number : "))
enrollment_number = int(input("Enter Enrollment Number : "))  
board_name = input("Enter Board Name : ").upper()
school_name = input("Enter School/College Name : ").upper()

#Input For Personal Details
name = input("Enter Student Name : ").upper()
father_name = input("Enter Father's Name : ").upper()
mother_name = input("Enter Mother's Name : ").upper()

#For Date of Birth
while True:
    dob = input("Enter Date Of Birth (DD-MM-YYYY) : ")

    #check dob  format
    if len(dob) == 10 and dob[2] == dob[5] == "-" :
            break
    else:
            print("Invalid Format! Please Enter Date in DD-MM-YYYY : ")

gender = input("Enter Gender : ").upper()
pincode = int(input("Enter Pin Code : "))

#Input for Intermediate Examination Passing Year
passing_year = int(input("Enter Intermediate Examination Passing Year (YYYY) : "))
    

#1st Subject input 
sub_1 = input("Enter Subject 1 : ").upper()
sub_1_mark = int(input(f"Enter {sub_1} Obtained Marks : "))

#2nd Subject input
sub_2 = input("Enter Subject 2 : ").upper()
sub_2_mark = int(input(f"Enter {sub_2} Obtained Marks : "))

#3rd Subject input
sub_3 = input("Enter Subject 3 : ").upper()
sub_3_mark = int(input(f"Enter {sub_3} Obtained Marks : "))

#4th Subject input
sub_4 = input("Enter Subject 4 : ").upper()
sub_4_mark = int(input(f"Enter {sub_4} Obtained Marks : "))

#5th Subject input
sub_5 = input("Enter Subject 5 : ").upper()
sub_5_mark = int(input(f"Enter {sub_5} Obtained Marks : "))

#checking failing subject and inserting it into a list 
fail_subject = []

# checking Subjects  For Failure :

#Inserting of Failed Subject Into The List
if sub_1_mark<33:
    fail_subject.append("Sub_1")   
if sub_2_mark<33:
    fail_subject.append("Sub_2")
if sub_3_mark<33:
    fail_subject.append("Sub_3")
if sub_4_mark<33:
    fail_subject.append("Sub_4")
if sub_5_mark<33:
    fail_subject.append("Sub_5")

#Check if failed subject is more than 1
if len(fail_subject)>=2:
    status = "FAIL"
else:
     status = "PASS"


#creating list for Obtained Marks

#  subject marks
total_obtained = [sub_1_mark,sub_2_mark,sub_3_mark,sub_4_mark,sub_5_mark]

#Calculating total marks
total_marks = sum(total_obtained)  

#maximum marks
max_marks = 100

#total maximum 
total_max = len(total_obtained)*max_marks

#Calculating Percentage
total_percentage = (total_marks/total_max)*100

#Calculating Grade
if total_percentage >= 85:
    grade = 'A+'
elif 75 <= total_percentage < 85:
    grade = 'A'
elif 65 <= total_percentage < 75:
    grade = 'B+'
elif 55 <= total_percentage < 65:
    grade = 'B'
elif 45 <= total_percentage < 55:
    grade = 'C'
elif 35 <= total_percentage < 45:
    grade = 'D'
else:
    grade = 'F'


os.system('cls') # Use for clear ing the console screen

print("************************ Intermediate Marksheet Generator***********************************")
print(f""" 
                                        {board_name}
                            Intermediate Examination-{passing_year}
----------------------------------------------------------------------------------------------------
School/College Name : {school_name:<40}
Roll Number         : {roll_number:<40} Enrollment Number  : {enrollment_number}
Name                : {name:<40} Date of Birth      : {dob}
Father Name         : {father_name:<40} Mother Name        : {mother_name}
Gender              : {gender:<40} Pin Code           : {pincode} 

____________________________________________________________________________________________________
Subjects       Max.Marks        Obtained Marks         Grand Total
____________________________________________________________________________________________________
{sub_1:<15}   {max_marks:<15}   {sub_1_mark:<15}   {total_marks}/{total_max}
{sub_2:<15}   {max_marks:<15}   {sub_2_mark:<15}
{sub_3:<15}   {max_marks:<15}   {sub_3_mark:<15}   {grade}/{status}  
{sub_4:<15}   {max_marks:<15}   {sub_4_mark:<15}
{sub_5:<15}   {max_marks:<15}   {sub_5_mark:<15}   
____________________________________________________________________________________________________


""")
   
os.system('pause')