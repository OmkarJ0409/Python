# 1. Take two variables of number and character and concatenate it.
name = 'Omkar'
birth_year = 2001
print(f"{name}" + f"{birth_year}")

# 2. Take three variables. Example: email_id.
username = 'omkarjagtap'
domain = '@gmail'
extension = '.com'
print(username + domain + extension)

# 3. Take three variables and print your full name.
first_name = 'Omkar'
middle_name = 'Dilip'
last_name = 'Jagtap'
print(first_name + ' ' + middle_name + ' ' + last_name)

# 4. Find out the percentage of the student using input from users.
subject_marks = map(int, input("Enter marks of 5 subjects with spaces : ").split())
print(f"Percentage: {sum(subject_marks)/500 * 100}")

# Q5. Find out Area of Rectangle using user input.
length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
area_of_rectangle = length * breadth
print("Area of rectangle is ", area_of_rectangle)

# 6. Find out Area of Square using user input.
side = int(input("Enter the side of square: "))
area_of_square = side * side
print("Area of Square is ", area_of_square)

# 7. Find out Area of Circle using user input.
radius = int(input("Enter the radius of circle: "))
area_of_circle = 3.14 * radius * radius
print("Area of Circle is ", area_of_circle)

# 8. Find out Perimeter of Rectangle.
length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
perimeter_of_rectangle = (2 * length) + (2 * breadth)
print("Perimeter of Rectangle is ", perimeter_of_rectangle)

# 9. Find out Perimeter of Square.
side = int(input("Enter the side of square: "))
perimeter_of_square = 4 * side
print("perimeter of Square is ", perimeter_of_square)

# 10. Find out Circumference of Circle.
radius = int(input("Enter the radius of circle: "))
circumference_of_circle = 2 * 3.14 * radius
print("circumference of circle is ", circumference_of_circle)

# 11. Find out Volume of Cube.
side = int(input("Enter the side of cube: "))
Volume_of_cube = side ** 3
print("Volume of cube is ", Volume_of_cube)

# 12. Find out Volume of Cuboid.
length = int(input("Enter the length of Cuboid: "))
breadth = int(input("Enter the breadth of Cuboid: "))
height = int(input("Enter the height of Cuboid: "))
Volume_of_cuboid = length * breadth * height
print("Volume of Cuboid is ", Volume_of_cuboid)

# 13. Find out Total Surface Area of Cube.
side = int(input("Enter the side of Cube: "))
Total_surface_area_of_cube = 6 * side * side
print("Total Surface Area of Cube is ", Total_surface_area_of_cube)

# 14. Find out Total Surface Area of Cuboid.
L = int(input("Enter the length of Cuboid: "))
B = int(input("Enter the breadth of Cuboid: "))
H = int(input("Enter the height of Cuboid: "))
Total_Surface_Area_of_Cuboid = 2 * (L * B + B * H + H * L)
print("Total Surface Area of Cuboid is ", Total_Surface_Area_of_Cuboid)

# 15. Take a number from the user and check whether it is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# 16. Take a number from the user and check whether it is positive, negative, or zero.
num = int(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 17. Take marks of 3 subjects and find the average marks.
marks = {
    'physics': 89,
    'chemistry': 77,
    'biology': 75
}
Average = (marks['physics'] + marks['chemistry'] + marks['biology']) / 3
print("Average marks are ", Average)

# 18. Take temperature in Celsius from the user and convert it into Fahrenheit.
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")

# 19. Take temperature in Fahrenheit from the user and convert it into Celsius.
f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5/9
print(f"{f}°F = {c}°C")

# 20. Take principal, rate of interest, and time from the user and calculate Simple Interest.
principal = int(input("Enter the principal amount: "))
rate_of_interest = int(input("Enter the rate of interest: "))
time = int(input("Enter the time: "))
Simple_interest = (principal * rate_of_interest * time) / 100
print("The Simple Interest is ", Simple_interest)

# 21. Take base and height from the user and find the area of a triangle.
base = int(input("Enter the base of triangle: "))
height = int(input("Enter the height of triangle: "))
Area_of_triangle = 0.5 * base * height
print("Area of triangle is ", Area_of_triangle)

# 22. Take two numbers and find the maximum and minimum using Python functions.
n = [10, 45]
print("Maximum number is", max(n), "and Minimum number is", min(n))

# 23. Take a string from the user and find its length.
Str1 = input("Enter a string: ")
length_of_string = len(Str1)
print("Length of string is", length_of_string)

# 24. Take a string from the user and reverse it.
Str2 = input("Enter a string: ")
reverse = Str2[::-1]
print("Reversed String is", reverse)

# 25. Take a number from the user and print its square and cube.
n = int(input("Enter a number: "))
square = n * n
cube = n ** 3
print(f"Square of {n} is {square} and Cube is {cube}")
