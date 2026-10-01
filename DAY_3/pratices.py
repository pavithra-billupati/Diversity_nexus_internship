'''#task-01
username=input("Enter the username :")
username1=username.strip()
low_username=username1.lower()
print(f"the user name is {low_username}")
#task-02
user_frist_name=input("enter the frist name:")
user_last_name=input("enter the last name:")
frist_name=user_frist_name.lower()
last_name=user_last_name.lower()
print(f"The full name of user is {frist_name} {last_name}")
#task3
sentance=str(input("enter any sentance :"))
length_sen=len(sentance)
frist_char=sentance[0]
last_char=sentance[-1]
spec_count=sentance.count(" ")
vowel=(sentance.lower().count("a")
    +sentance.lower().count("e")
    + sentance.lower().count("i")
    + sentance.lower().count("o")
    + sentance.lower().count("u"))
print(f"length of sentence is {length_sen}")
print(f"the frist character of sentence is {frist_char}")
print(f"last charater in the sentence is {last_char}")
print(f"{spec_count} of spaces in the sentences")
print(f"{vowel} of vowels in the sentences")
#task_04
mail_id=input("Enter the mail :")
is_endwith=mail_id.endswith(".com")
print("it ends with @","@" in mail_id,)
print("it end with .com",is_endwith)
print("at",mail_id.find("@"),"index @ is exisis ")
#task05
product_code=input("enter the product code like this counter-category-year-serial(IND-MOB-2026-001) :")
country=product_code[:3]
category=product_code[4:7]
Year=product_code[8:12]
serial=product_code[13:]
print(f"country {country}")
print(f"category {category}")
print(f"year {Year}")
print(f"serial {serial}")
#task06
name = "Pavithra"
age = 21
city = "Nellore"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")
#task07
product="phone"
price=200
quantity=4
bill=price*4
print(f"the cost of {quantity} {product} is {bill}")
#task 08
student_name = "Pavithra"
total_marks = 425
average = 85
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average}")
#task09
a = 20
b = 10
result = a + b
print(f"The sum of {a} and {b} is {result}.")'''
#task10
price = 99.5
print(f"The price is {price:.2f}")
