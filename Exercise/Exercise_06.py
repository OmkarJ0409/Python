# 1. Accept marks of 5 subjects and calculate total, percentage, and display division (First, Second, Third, Fail)
while True:
    print("-------------- Enter Marks Below ---------------------------")
    Marks = {"English": int(input("Enter English Marks: ")),
             "Maths": int(input("Enter Maths Marks: ")),
             "Science": int(input("Enter Science Marks: ")),
             "History": int(input("Enter History Marks: ")),
             "Hindi": int(input("Enter Hindi Marks: "))
             }

    Total_marks = Marks['English'] + Marks['Maths'] + Marks['Science'] + Marks['History'] + Marks['Hindi']
    Percentage = round(Total_marks / 500 * 100, 2)

    print("--------------------- Record -------------------------------")
    print("Total marks :", Total_marks)
    print("Percentage: ", Percentage)
    if Percentage >= 90:
        print("First Grade")
    elif Percentage >= 65:
        print("Second Grade")
    elif Percentage >= 45:
        print("Third Grade")
    else:
        print("Fail")
    break

# 2. Accept temperature and display whether it is Hot, Moderate, or Cold.
temperature = int(input("Enter the temperature: "))
if temperature > 32:
    print("Temperature is High")
elif 10 < temperature < 32:
    print("Temperature is Moderate")
else:
    print("Temperature is Low")

# 3. Accept a number and check whether it is Armstrong number or not (e.g., 153 = 1³+5³+3³).
num = int(input("Enter a number: "))
temp = num
power = len(str(num))
sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** power
    temp //= 10
print("Armstrong number" if num == sum_of_powers else "Not Armstrong")

# 4. Accept a number and check whether it is a perfect number (sum of divisors = number).
n = int(input("Enter a number: "))
sum_of_divisor = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_divisor += i
if sum_of_divisor == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")

# 5. Accept a character and check whether it is uppercase, lowercase, digit, or special symbol.
character = input("Enter a character: ")
if chr(48) <= character <= chr(57):
    print("It's a digit")
elif chr(65) <= character <= chr(90):
    print("It's a uppercase character ")
elif chr(97) <= character <= chr(122):
    print("It's a lowercase character")
elif character.isascii():
    print("It's a Special character")
else:
    print("Enter a valid character")

# 6. Accept a string and check whether it is a palindrome string.
Str = input("Enter a string: ")
if Str == Str[::-1]:
    print("String is Palindrome")
else:
    print("String is NOT Palindrome")

# 7. Accept age and check the ticket price:
#    - Age < 5 → Free
#    - Age 5–12 → Rs 100
#    - Age 13–59 → Rs 200
#    - Age >=60 → Rs 150
Age = int(input("Enter your age to check ticket fare: "))
if Age <= 5:
    print("Ticket is Free for you")
elif 5 < Age <= 12:
    print("Your ticket Fare is RS100")
elif 13 <= Age <= 59:
    print("Your ticket Fare is RS200")
elif Age >= 60:
    print("Your ticket Fare is RS150")
else:
    print("Enter appropriate Age")

# 8. Accept income from user and calculate tax as per given slabs:
#   - Income ≤ 2,50,000 → No Tax
#   - 2,50,001–5,00,000 → 5%
#   - 5,00,001–10,00,000 → 20%
#   - Above 10,00,000 → 30%
Income = int(input("Enter the Income: "))
if Income >= 1000000:
    Tax = Income * (30/100)
elif 500001 <= Income < 1000000:
    Tax = Income * (20 / 100)
elif 250001 <= Income <= 500000:
    Tax = Income * (5 / 100)
else:
    Tax = "No Tax for You"
print("Tax Amount: ", round(Tax, 2))

# 9. Accept a number and check whether it is a Harshad number (divisible by sum of its digits).
num = int(input("Enter a number: "))
temp = num
sum_digits = 0
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
if num % sum_digits == 0:
    print(f"{num} is a Harshad Number")
else:
    print(f"{num} is not a Harshad Number")

# 10. Accept 3 numbers and check whether they can form a Pythagorean triplet (a²+b²=c²)(3, 4, 5),(5, 12, 13).
a, b, c = map(int, input("Enter the 3 Sides of Triangle: ").split())
if (a ** 2) + (b ** 2) == c ** 2 or \
        (a ** 2) + (c ** 2) == b ** 2 or \
        (b ** 2) + (c ** 2) == a ** 2:
    print("It forms a Pythagorean triplet")
else:
    print("It does NOT form a Pythagorean triplet")

# 11. Print numbers from 1 to 10 but skip number 5 using continue.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in A:
    if num == 5:
        continue
    print(num)

# 12. Print numbers from 1 to 10 but stop when number 7 comes using break.
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in A:
    if num == 7:
        break
    print(num)

# 13. Use a loop with pass inside if condition to demonstrate null statement.
c = [1, 2, 3, 4, 5]
for C in c:
    pass

# 14. Accept a number and print whether it is prime or not, but break the loop if a factor is found.
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")

# 15. Accept 10 numbers from user and print only the positive numbers (skip negatives using continue).
num = map(int, input("Enter 10 numbers: ").split())
for n in num:
    if n < 0:
        continue
    print(n)

# 16. Accept a number and check whether it is divisible by both 5 and 11.
num = int(input("Enter a number: "))
if num % 5 == 0:
    if num % 11 == 0:
        print("It is Divisible by both 5 and 11")
else:
    print("It is not divisible by 5 and 11")

# 17. Accept a string and check whether it contains both alphabets and digits.
Str = input("Enter a string: ")
has_alphabets = False
has_digits = False
for s in Str:
    if s.isalpha():
        has_alphabets = True
    if s.isdigit():
        has_digits = True
    if has_alphabets and has_digits:
        break
if has_alphabets and has_digits:
    print("String contains both alphabets and digits")
elif has_digits:
    print("String contains only digits")
elif has_alphabets:
    print("String contains only alphabets")
else:
    print("String does NOT contain any alphabets or digits")

# 18. Accept a number and check whether it is both a prime number and odd.
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        if num % 2 != 0:
            print("It is Prime and odd both")

# 19. Accept a year and check whether it is a century year (e.g., 1900, 2000).
year = int(input("Enter the Year: "))
if year % 100 == 0:
    print(f"{year} is a century year")
else:
    print(f"{year} is a normal year")

# 20. Accept two numbers and check whether the first is a multiple of the second.
a, b = map(int, input("Enter 2 numbers: ").split())
if a % b == 0:
    print("first is multiple of second")
else:
    print("first is not multiple of second")

# 21. ATM Program: Accept withdrawal amount and check conditions:
#     - Amount multiple of 100
#     - Minimum balance of 500 must remain
#     - Deduct and display remaining balance
while True:
    print("------------------------ATM--------------------------------")
    print("1. Withdraw amount")
    print("2. Exit")

    choice = int(input("Enter Your Choice : "))
    Available_Amount = 5000
    Min_balance = 500

    if choice == 1:
        Amount = int(input("Enter the amount you want to withdraw: "))
        if Amount % 100 != 0:
            print("Amount Should be Multiple of 100")
            continue
        if Amount > Available_Amount:
            print("Insufficient funds !")
            continue
        if (Available_Amount - Amount) < Min_balance:
            print(f"Withdrawal not allowed. At least {Min_balance} should be kept in Account")
            continue
        if Amount <= Available_Amount:
            print(f"{Amount} RS Withdrawn from Account")
            Remaining_Balance = Available_Amount - Amount
            print(f"{Remaining_Balance} Rs Remaining in account")

    if choice == 2:
        break

# 22. Railway Ticket Discount: Accept age and class type (AC/General) → Provide discount:
#     - Child (<12) → 50% off
#     - Senior citizen (>=60) → 40% off
#     - Otherwise → No discount
Ticket = 100
Person = {"Age": int(input("Enter Your Age: ")),
          "Class Type": input("Enter Class Type(G or A/C): ")
          }
if Person['Age'] <= 12:
    if Person['Class Type'] == 'A/C':
        Fare = Ticket
    else:
        Fare = Ticket * 0.50
elif Person['Age'] >= 60:
    if Person['Class Type'] == 'A/C':
        Fare = Ticket * 0.75
    else:
        Fare = Ticket * 0.60
else:
    if Person['Class Type'] == 'A/C':
        Fare = Ticket * 1.5
    else:
        Fare = Ticket
print(f"Fare: {Fare} Rs")

# 23. Cinema Hall Program: Accept movie type (Normal/3D/IMAX) and age → Show ticket price accordingly.
Movie = {'Movie_type': input("Enter movie type(Normal/3D/IMAX): "),
         'age': int(input("Enter your age: "))
         }
Price = {'Normal': 200,
         '3D': 250,
         'IMAX': 300
         }
if Movie['age'] >= 18:
    if Movie['Movie_type'] == 'Normal':
        Ticket_Price = Price['Normal']
        print(Ticket_Price)
    elif Movie['Movie_type'] == '3D':
        Ticket_Price = Price['3D']
        print(Ticket_Price)
    elif Movie['Movie_type'] == 'IMAX':
        Ticket_Price = Price['IMAX']
        print(Ticket_Price)
else:
    if Movie['Movie_type'] == 'Normal':
        Ticket_Price = Price['Normal'] * 0.5
        print(Ticket_Price)
    elif Movie['Movie_type'] == '3D':
        Ticket_Price = Price['3D'] * 0.5
        print(Ticket_Price)
    elif Movie['Movie_type'] == 'IMAX':
        Ticket_Price = Price['IMAX'] * 0.5
        print(Ticket_Price)

# 24. Online Shopping: Accept purchase amount →
#     - ≥ 5000 → 20% discount
#     - ≥ 2000 → 10% discount
#     - Otherwise → No discount
Purchase_Amount = int(input("Shopping Expenses Amount: "))
if Purchase_Amount >= 5000:
    Discounted_Price = Purchase_Amount - (Purchase_Amount * 0.20)
    print("20 % Discount Applied")
elif Purchase_Amount >= 2000:
    Discounted_Price = Purchase_Amount - (Purchase_Amount * 0.10)
    print("10 % Discount Applied")
else:
    Discounted_Price = Purchase_Amount
    print("NO Discount Applied")
print("Discounted Price: ", Discounted_Price)

# 25. Grading with Remark: Accept marks and display grade + remark (e.g., A → Excellent, B → Good, etc.).
Subject = int(input("Enter marks: "))
if Subject >= 90:
    print("Grade A\nExcellent")
elif Subject >= 75:
    print("Grade B\nVery Good")
elif Subject >= 60:
    print("Grade C\nGood")
elif Subject >= 45:
    print("Grade D\nBad")
else:
    print("Grade E\nFail")
