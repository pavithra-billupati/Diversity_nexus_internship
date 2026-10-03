#task01
'''1. ATM PIN Attempts — while + break
An ATM gives the user 3 chances to enter the correct PIN.

Ask for PIN repeatedly.
If correct → print "Access Granted" and stop.
After 3 wrong attempts → print "Card Blocked".'''

ATM_pin=123
i=1
while i<=3:
    pin=int(input("Enter your pin :"))
    if pin==ATM_pin:
        print("Access Granted")
        break
    if i == 3 and pin != ATM_pin:
        print("Card Blocked")
        break
    i=i+1  


'''1. College Attendance System

A teacher wants to enter attendance for 7 days.

P = Present
A = Absent
If the user enters anything else, use continue.
Count total present and absent days.
Calculate attendance percentage.
If attendance falls below 75%, display a warning.

Topics: for, range(), continue'''
#task02
Present=0
Absent=0
for day in range(1,8):
    attendence=input(f"Enter the day {day} attendences (P/A):").lower()
    if attendence=="p":
        Present=Present+1
    elif attendence=="a":
        Absent=Absent+1
    else:
        continue
percentage=int((Present/7)*100)
if percentage < 75:
    print(f"the attendences is below 75 ( {percentage} )")
else:
    print(f"attendences percentages is {percentage}")
#task03
number=int(input("enter the number:"))
for i in range(11):
    print(f"{number} x {i} = {i*number}")
#task04
n=int(input("Enter the number :"))
sum=0
for i in range(n+1):
    sum=sum+i
print(f"the sum of whole number from 1 to {n} is {sum}")
#task05
num=int(input("Enter the number:"))
even_count=0
odd_count=0
for i in range(1,num+1):
    if i%2 == 0:
        even_count +=1
    else:
        odd_count +=1
print(f"the number of even numbers in range of 1 to {num} are {even_count}")
print(f"the number of odd numbers in range of 1 to {num} are {odd_count}")
#task06
number1=int(input("enter the number which you want to check (prime /not )"))
for i in range (2,number1):
    if number1%i == 0:
        print(f"{number1} not a prime number")
        break
else:
    print(f"{number1} is a prime number.")
#task07
number2=int(input("enter the number: "))
num1=number2
r_number2=0
while num1!=0:
    digit=num1%10
    r_number2=(r_number2*10)+digit
    num1=int(num1//10)
if number2==r_number2:
    print(f"{number2} is a palindrome number")
else:
    print(f"{number2} not a palindrome number.")
#task08
number3=int(input("enter the number :"))
print("the factors are :")
for i in range (1,number3+1):
    if number3%i== 0:
        print(i)
#task09
for i in range(1,101):
    if i%7 == 0 and i%9 == 0:
        print(f"the frist number for 1 to 100 which is divisible my both 7 and 9 is {i}")
        break
#task10
for i in range(1,51):
    if i%3==0:
        continue
    print(i,end=" ")
#task11
for i in range(1,6):
    print("*"*i)
print("-----------------------------")
for i in range(1,6):
    print("*"*(6-i))
print("-----------------------------")
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
#task12
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("-------------------")
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()


    


