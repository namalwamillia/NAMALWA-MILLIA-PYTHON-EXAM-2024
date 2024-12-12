# 1(i) Python function named "circle_area" with radius as parameter and returns area of a circle

# we define a function
def circle_area(radius):
    
# we state the value of pi
    pi = 3.14 
#we calculate the area from the given formula
    area = pi * (radius ** 2)
    return area

# we test the function with radius 4
result = circle_area(4)
print("The Area of a Circle with radius 4 is:",result)



# 1(ii) integers [4, 7, 2, 9, 12, 15],getting the sum of odd numbers using for loop
 
numbers = [4, 7, 2, 9, 12, 15]

sum_of_odd_numbers = 0

# Looping through the list
for num in numbers:
    
# Check if the number is odd
    if num != num // 2 * 2:
        sum_of_odd_numbers += num 
#print
print("The sum of all odd numbers in the list is:", sum_of_odd_numbers)


     
#1(iii)funtion that takes 2 numbers as inputs and returns sum,difference,product, qoutient

#funtion defining
def calculate_operations(num1, num2):
# returning the results
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2 

# nunber inputs
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

sum, difference, product, quotient = calculate_operations(first_num, second_num)

# printing results
print("The Sum is:", sum)
print(" The Difference is:", difference)
print("The Product is:", product)
print("The Quotient is:", quotient)


#1(iv) Given dictionary in qn below

student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Updating the 'age' to 26
student_info['age'] = 26

# Adding a new key-value pair ('city', 'Kampala')
student_info['city'] = 'Kampala'

# Printing the updated info in a dictionary 
print("The updated Dictionary is:",student_info)



