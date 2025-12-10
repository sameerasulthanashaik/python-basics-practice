#Split Values to Integer List

values = input("Enter comma-separated values: ")
lst = values.split(",")
lst = [int(x) for x in lst]
print(lst)

print()

#Swap and Convert Types

a = "100"
b = 200

a, b = b, a

a = int(a)
b = str(b)

print(a, type(a))
print(b, type(b))

print()
#Check the type of values
a = 10
b = 3.5
c = "hello"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


print()
#Perform +, -, *, /, %, //, ****
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

print()
#BMI Calculator

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height * height)
print("BMI =", bmi)

print()
#AND, OR, NOT
a = True
b = False

print(a and b)
print(a or b)
print(not a)

print()
