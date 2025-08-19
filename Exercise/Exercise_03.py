# -------------------------------
# Predict the Output Questions
# -------------------------------

# 1
a = 10
b = 20
a, b = b, a
print(a)  # Output : 20
print(b)  # Output : 10

# 2
x = 15
y = 25
y, x = x, y
print(x)  # Output : 25
print(y)  # Output : 15

# 3
a = 10
b = 15
a, b = b + 5, a
print(a)  # Output : 20
print(b)  # Output : 10

# 4
a = 20
b = 30 + a
a, b = b, a
print(a)  # Output : 50
print(b)  # Output : 20

# 5
x = 20
y = 70 + x
x, y = y, x + y
print(x)  # Output : 90
print(y)  # Output : 110

# 6
x = 20
y = 70 - x
x, y = y, y + x
print(x)  # Output : 50
print(y)  # Output : 70

# 7
a, b = 2, 10
c, b = a * 5, a / 2
print(a, b, c)  # Output : a: 2, b: 1, c: 10

# 8
a = 20
b = 5
a, b = a // 20, a ** b
print(a, b)  # Output : a:1, b: 3200000

# 9
print(print(20))  # 1st Output : 20, 2nd Output : None

# 10
print(print(int(50.50)))  # 1st Output : 50, 2nd Output : None

# 11
print(print("shalini"))  # 1st Output : shalini, 2nd output : None

# 12
a, b, c = 5, 10, 15
a, b, c = c, a, b
print(a, b, c)  # Output : a: 15, b: 5, c: 10

# 13
x, y = 7, 14
x, y = x * y, x + y
print(x, y)  # Output : x: 98, y: 21

# 14
a, b = 100, 50
a, b = b - 10, a + 20
print(a, b)  # Output : a: 40, b: 120

# 15
a, b, c = 1, 2, 3
a, b, c = b + c, a + b, a
print(a, b, c)  # Output : a: 5, b: 3, c: 1

# 16
x = 40
y = x // 10
x, y = y, x % 7
print(x, y)  # Output : x: 4, y: 5

# 17
a, b = 8, 4
a, b = a ** b, b ** a
print(a, b)  # Output : a: 4096, b: 65536

# 18
p, q = 3, 6
p, q = q // p, q % p
print(p, q)  # Output : p: 2, q: 0

# 19
x, y, z = 2, 4, 6
x, y, z = y * z, x * z, x + y
print(x, y, z)  # Output : x: 24, y: 12, z: 6

# 20
m, n = 12, 18
m, n = n - m, m + n
print(m, n)  # Output : m: 6, n: 30

# 21
a = 5
a, b = a * 2, a + 10
print(a, b)  # Output : a: 10, b: 15

# 22
x, y = 2, 3
x, y = x ** y, y ** x
print(x, y)  # Output : x: 8, y: 9

# 23
a, b = 4, 9
a, b = (a + b) // 2, (a * b)
print(a, b)  # Output : a: 6, b: 36

# 24
num1, num2 = 15, 25
num1, num2 = num2 % num1, num1 % num2
print(num1, num2)  # Output : num1: 10, num2: 15

# 25
x = 7
y = 3
x, y = (x + y) // y, (x * y) // y
print(x, y)  # Output : x: 3, y: 7
