#task01
name=input("Enter student Name : ")
marks=int(input("Enter marks :"))
grade=''
if marks < 0 or marks > 100:
    print("Invalid marks.")
else:
    if marks>=90:
        grade="A"
    elif marks >=75:
        grade="B"
    elif marks >=60:
        grade="C"
    elif marks >=50:
        grade="D"
    else:
        grade="F"
print(f" {name} got {marks} marks grade is {grade} ")   

#task02
age=int(input("Enter the age  of the Student:"))
Percentage=float(input("Enter your percentage:"))
Backlog=int(input("enter your backlogs :"))
if age>=18 and age<=24:
    if Percentage>= 75 and Backlog ==0:
        print(" you are Eligible")
    elif Backlog > 2 or Percentage > 60:
        print("you are not eligible")
    else:
        print("you are not eligible")
else:
    print("you are not eligible")

#task03
int_balance=1000
balance=float(int_balance)
option=int(input("Enter the option :"))
if option == 1:
    print(f"your balance is {balance}")
elif option ==2:
    deposit=int(input("Enter the amount to deposite :"))
    balance=balance+deposit
    print(f"successfully add your amount \n your balance is {balance}")
elif option ==3:
    with_draw=int(input("Enter the amount to withdraw :"))
    balance=balance-with_draw
    print(f"successfully debited \n your balance is {balance}")
elif option ==4:
    print("thank you")
    exit()
else:
    print("invalid")
#task04
Username="pavithra_4313"
password="pavi123"
enter_Username=input("Enter the username:")
if enter_Username==Username:
    enter_password=input("Enter the password :")
    if enter_password==password:
        User=input("enter the user:")
        if User=="admin":
            print("successfully login")
        else:
            print("verification is needed")
    else:
        print("Password is incorrect")
else:
    print("username is not matched")
#task05
order_amount=int(input("enter order amount:"))
Distance=int(input("enter distance to your location :"))
membership=input("are you member in this app :(Yes/No):")
peak_time=input("are you busy at peak_time (yes/no):")
Delivery_charge=0
Total=0
discount=0
if order_amount>=1000:
    print("-> Free Delivery?")
    Delivery_charge=0
    print(f"delivery charge is {Delivery_charge}")
else:
    if Distance<=3:
        Delivery_charge=30
        print(f"delivery charge is {Delivery_charge}")
    elif Distance <=7:
        Delivery_charge=70
        print(f"delivery charge is {Delivery_charge}")
    elif Distance <=10:
        Delivery_charge=100
        print(f"delivery charge is {Delivery_charge}")
    else:
        print("not available for delivery")
if membership.lower()=="yes"and peak_time.lower()=="no":
    discount=20
elif membership=="yes"and peak_time=="yes":
    discount=10
else:
    discount=0
print(f"your discount {discount} and order amount {order_amount}")
print(f"the total bill = {order_amount+Delivery_charge-discount}")
    

   






