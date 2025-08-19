# 1. Check whether a number is divisible by 7.
num = int(input("Enter a number:"))
if num % 7 == 0:
    print("Number is Divisible by 7")
else:
    print("Number is Not-Divisible by 7")

# 2. Check whether a given number is even or odd.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# 3. Check whether a given number is positive, negative, or zero.
num = int(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 4. Check whether the character 'a' is present in the string "Python" or not.
Str = "python"
if 'a' in Str:
    print("A is present")
else:
    print("A is Not-Present")

# 5. Accept three numbers and find the largest number among them.
a, b, c = 10, 2, 5
if a > b and a > c:
    print("A is Largest")
elif b > c:
    print("B is largest")
else:
    print("C is largest")

# 6. Check whether a given year is a leap year or not.
year = int(input("Enter the Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a Leap Year.")
else:
    print("It's Not a Leap Year.")

# 7. Calculate attendance percentage and check eligibility for exams (>=75%).
Days = {'Total Days': int(input("Enter total days: ")), 'Present Days': int(input("Enter present days: "))}
attendance = ((Days['Present Days'] / Days['Total Days']) * 100)
if attendance >= 75:
    print(f"Your attendance is {attendance}%. You are eligible for exam.")
else:
    print(f"Your attendance is low ({attendance}%). You CANNOT give the exam.")

# 8. Check whether the entered character is a vowel or not.
S = input("Enter a character:")
if S.lower() in 'aeiou':
    print("Character is a Vowel")
else:
    print("Character is not a Vowel")

# 9. Accept a number from 1 to 7 and print the day of the week (1=Sunday, 2=Monday, …).
A = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
num = int(input("Enter a number between 1- 7: "))
if num in A:
    print(A[num])

# 10. Accept a city name and display its monument.
City = {
    'Delhi': 'Red Fort',
    'Agra': 'Taj Mahal',
    'Jaipur': 'Jal Mahal'
}
c = input("Enter city name:")
if c in City:
    print(City[c])

# 11. Check whether a person is eligible to vote (age >=18).
age = int(input("Enter your age: "))
if age >= 18 <= 85:
    print("You are eligible to vote")
else:
    print("You are Minor")

# 12. Make a simple calculator (add, subtract, multiply, divide) using if-elif.
a, b = map(int, input("Enter two numbers: ").split())
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    Addition = a + b
    Subtraction = a - b
    Division = a / b
    Multiplication = a * b
    choice = int(input("Enter the number of operation: "))
    if choice == 1:
        print(Addition)
    elif choice == 2:
        print(Subtraction)
    elif choice == 3:
        print(Division)
    elif choice == 4:
        print(Multiplication)
    elif choice == 5:
        break

# 13. Check whether a figure is square or not by comparing length and breadth.
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
if length == breadth:
    print("Figure is a Square")
else:
    print("Figure is not a Square")

# 14. Accept percentage from user and display grade.
percentage = int(input("Enter your Percentage: "))
if percentage >= 80:
    print("A+")
elif 60 <= percentage < 80:
    print("A")
elif 50 <= percentage < 60:
    print("B+")
elif 45 <= percentage < 50:
    print("B")
elif 25 <= percentage < 45:
    print("C")
else:
    print("D")

# 15. Accept three sides of a triangle and check whether it is equilateral, isosceles, or scalene.
a, b, c = map(int, input("Enter sides of triangle: ").split())
if a == b == c:
    print("Equilateral Triangle")
elif a == b or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# 16. Accept three sides of a triangle and check whether the triangle is valid (sum of any two sides > third side).
a, b, c = map(int, input("Enter sides of triangle: ").split())
if (a + b > c) and (a + c > b) and (b + c > a):
    print("It is an Valid Triangle")
else:
    print("It is NOT a Valid Triangle")

# 17. Check whether a key exists in a dictionary or not.
person = {"name": "Omkar", "age": 24, "city": "Navi Mumbai"}
key = input("Enter key to check: ")
if key in person:
    print(f"Yes, '{key}' exists in the dictionary.")
else:
    print(f"No, '{key}' does not exist in the dictionary.")

# 18. Check whether a number is a three-digit number or not.
number = int(input("Enter a number: "))
number = str(number)
if len(number) == 3:
    print("It is a three digit number")
else:
    print("It is NOT a three-digit number")

# 19. Accept electricity units and calculate bill.
units = int(input("Enter the electricity unit: "))
if units == 100:
    print("It's Free. You don't have to pay")
elif 100 <= units < 300:
    price = units * 2
    print(f"You have to pay {price} RS")
else:
    price = units * 5
    print(f"You have to pay {price} RS")

# 20. Accept age, sex (M/F), number of working days, and calculate wages/day as per rules.
person = {'Age': int(input("Enter your age: ")), 'Sex': input("Enter Sex(M/F): "),
          'Days': int(input("Enter number of days worked: "))}
if 18 < person['Age'] <= 30:
    if person['Sex'] == 'M':
        print(f"Your wages are {700 * person['Days']}")
    elif person['Sex'] == 'F':
        print(f"Your wages are {750 * person['Days']}")
elif 30 < person['Age'] <= 40:
    if person['Sex'] == 'M':
        print(f"Your wages are {800 * person['Days']}")
    elif person['Sex'] == 'F':
        print(f"Your wages are {850 * person['Days']}")
else:
    print("Enter Appropriate Age")

# 21. Accept three numbers and display the second-largest number.
a, b, c = map(int, input("Enter three numbers: ").split())
if (b < a < c) or (b > a > c):
    second = a
elif (a < b < c) or (a > b > c):
    second = b
else:
    second = c
print("Second Largest number is ", second)

# 22. Accept number of days late for library book submission and calculate fine.
days = int(input("Enter the number of days delayed for Book Submission: "))
if days <= 5:
    print(f"Your fine is {2 * days}")
elif 5 < days <= 10:
    print(f"Your fine is {3 * days}")
elif 10 < days <= 15:
    print(f"Your fine is {4 * days}")
elif days > 15:
    print(f"Your fine is {5 * days}")

# 23. Accept a number and check whether it is a prime number.
num = int(input("Enter a number:"))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")

# 24. Accept a number and check whether it is a palindrome number (same when reversed).
num = int(input("Enter a number:"))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if num == rev:
    print("It's Palindrome number")
else:
    print("It is NOT Palindrome")

# 25. Accept a string and check whether it is an anagram of another string (e.g., "care" → "race").
Str = input("Enter 2 strings: ").split()
if sorted(Str[0]) == sorted(Str[1]):
    print("Strings are Anagrams")
else:
    print("Strings are NOT Anagrams")
