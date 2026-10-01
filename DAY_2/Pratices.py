#task01
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print("Hello, my name is", name, "I am", age, "years old and I live in", city)
#task02
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = quantity * price
print("Item:", item_name)
print("Total Bill:", total)
#task04
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
#task05
markes1 = float(input("Enter marks in  Subject 1: "))
markes2 = float(input("Enter marks in Subject 2: "))
markes3 = float(input("Enter marks in Subject 3: "))
total = markes1+markes2+markes3
average = total / 3
print("Total Marks:", total)
print("Average:", average)
#task06
age = int(input("Enter your current age: "))
print("Age after 5 years:", age + 5)
print("Age after 10 years:", age + 10)
print("Age after 20 years:", age + 20)
#task07
value = input("Enter a whole number: ")
print("Original:", value, type(value))
int_val = int(value)
print("As Integer:", int_val, type(int_val))
float_val = float(value)
print("As Float:", float_val, type(float_val))
#task08
bill = float(input("Enter bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))
tip_amount = bill * (tip_percent / 100)
total_amount = bill + tip_amount
print("Total Bill:", total_amount)
print("Amount per person:", total_amount / people)
#task09
integer = 10
decimal = 5.5
text = "Hello"
boolean = True
empty = None
print(integer, type(integer))
print(decimal, type(decimal))
print(text, type(text))
print(boolean, type(boolean))
print(empty, type(empty))
print("Converted Int to Float:", float(integer))
print("Converted Float to String:", str(decimal))
#task10
name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
is_student = bool(int(input("Student? (1 for Yes, 0 for No): ")))
phone = input("Enter phone number: ")
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Student:", is_student, type(is_student))
print("Phone:", phone, type(phone))






