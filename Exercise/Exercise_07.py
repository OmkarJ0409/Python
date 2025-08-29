# 1. Write a program to print the first 10 even numbers.
count = 0
num = 2
while count < 10:
    print(num)
    num += 2
    count += 1

# 2. Write a program to print the first 10 odd numbers.
c = 0
n = 1
while c < 10:
    print(n)
    n += 2
    c += 1

# 3. Write a program to print the first 10 even numbers in reverse order.
number = []
for i in range(10, 0, -1):
    number.append(2 * i)
print(number)

# 4. Write a program to find the factorial of a number using a for loop.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")

# 5. Write a program to check whether a number is prime or not.
num = int(input("Enter a number: "))
if num <= 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 6. Write a program to print numbers from 1 to 20 except multiples of 2 and 3.
for i in range(1, 21):
    if i % 2 != 0 and i % 3 != 0:
        print(i)

# 7. Write a program to accept 10 numbers from the user and display their average.
nums = list(map(int, input("Enter 10 numbers with spaces between them: ").split()))
total = 0
for i in nums:
    total += i
avg = total / len(nums)
print(avg)

# 8. Write a program to accept 10 numbers from the user and display the largest and smallest numbers.
nums = list(map(int, input("Enter 10 numbers with spaces between them: ").split()))
smallest = nums[0]
largest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i
print(f"List: {nums}")
print(f"Smallest: {smallest} , Largest: {largest}")

# 9. Write a program to print only odd numbers from the given list using a for loop.
L = [23, 45, 32, 25, 46, 33, 71, 90]
for i in L:
    if i % 2 != 0:
        print(i)

# 10. Reverse the word "develearn" and print it using a for loop.
word = 'develearn'
word = word[::-1]
for i in word:
    print(i, end=" ")

# 11. Count the number of vowels in the word "education".
words = 'Education'
vowels = 'aeiouAEIOU'
vowel_count = 0
for i in words:
    if i in vowels:
        vowel_count += 1
print(vowel_count)

# 12. Print all prime numbers up to a number (input from user).
num = int(input("Enter a number: "))
for n in range(2, num + 1):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")

# 13. Print odd numbers from 1 to 10 using a while loop.
i = 0
while i < 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 14. Find the factorial of a number using a while loop.
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} is {fact}")

# 15. Print only the domain names using set comprehension.
emails = {'aman@xmail.com', 'devesh@gmail.com', 'diya@ymail.com', 'jeba@zmail.com'}
s = set(x.split('@')[1] for x in emails)
print(s)

# 16. Write a program to print the following pattern:
#     5 5 5 5 5
#     4 4 4 4
#     3 3 3
#     2 2
#     1
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

# 17. Predict the output:
x = 5
while x < 15:
    print(x**2)
    x += 3      # Output: 25 64 121 196

# 18. Predict the output:
a = 7
b = 5
while a < 9:
    print(a+b)
    a += 1      # Output: 12 13

# 19. Predict the output:
b = 15
while b > 9:
    print("Hello")
    b = b-2         # Output: Hello Hello Hello

# 20. Convert the following while loop into a for loop:
# x = 4
# while x <= 8:
#     print(x*10)
#     x += 2
for i in range(4, 9, 2):
    print(i * 10)

# 21. Predict the output:
x = 3
if x > 2 or x < 5 and x == 6:
    print("Bye")
else:
    print("Thankyou")           # Output: Bye

# 22. Predict the output:
x, y = 2, 4
if x+y == 10:
    print("Thankyou")
else:
    print("Bye")            # Output: Bye

# 23. Trace the output:
x = 10
y = 1
while x > y:
    x = x-4
    y = y+3
    print(x)            # Output: 6 2

# 24. Trace the output:
i = 9
while True:
    if i % 3 == 0:
        break
    print("A")          # Output: No output(while loop breaks before print("A"))

# 25. Trace the output:
n = 20
for i in range(2, n//4):
    if n % i == 0:
        print("Python output based questions")
    else:
        print("Bye")
# Output: Python output based questions
#         Bye
#         Python output based questions
