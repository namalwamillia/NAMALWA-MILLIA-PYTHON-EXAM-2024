#SECTION B
# 2(i) student Details, name=Gloria Arinda,Reg no.= SEP23/BCS/088U/F, Programming=90, Data 
#Science= 87,Computer applications=77).

#inputs of the information  required from student

student_name = str(input("Enter student name: "))
student_no = str(input("Enter student Reg.no: "))

Programming_marks = int(input("Enter student programming marks: "))
data_science_marks= int(input("Enter student Data Science marks: "))
computer_application_marks =int(input("Enter student computer application marks: "))


number_of_course_units = 3
#total marks for all course units
total_marks = Programming_marks + data_science_marks + computer_application_marks

#print total marks
print(f"total_marks is: {total_marks}")

#Average marks 
average_marks = total_marks / number_of_course_units

print(f"The average_marks for a Student is: {average_marks:.3f}")

#full Details
print("\nStudent Details:")
print(f"Name: {student_name}")
print(f"Student Number: {student_no}")
print(f"Programming Marks: {Programming_marks}")
print(f"Data Science Marks: {data_science_marks}")
print(f"Computer Applications Marks: {computer_application_marks}")
print(f"Average Mark: {average_marks:.3f}")


#2(ii)A car's miles per gallon

# user input

milesDriven = float(input("Enter the number of miles driven: "))
gallonsOfGasUsed = float(input("Enter the number of gallons of gas used: "))

# Calculating miles per gallon (MPG)

if gallonsOfGasUsed != 0:
    MPG = milesDriven / gallonsOfGasUsed
    
# printing results
    print(f"The car's miles per gallon (MPG) is: {MPG:.2f}")
else:
    print("Gallons used cannot be zero.")
    
    
#2(iii) numbers from 1 to 100 not divisible by 2,(odd number)
    
# Loop through all the numbers from 1 to 100
for number in range(1, 101):
    
# Check if the number is not divisible by 2

    if number // 2 * 2 != number:
        
        print(number)
        


