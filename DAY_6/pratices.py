'''#task01
def calculate_sum(*args):
    total=0
    for number in args:
        total=total+number
    return total

total=calculate_sum(8,9,12,45)
print(total)
#task02
def student_details(**student_data):
    for key,value in student_data.items():
        print(f"{key} : {value}")
student_details(name="pavithra",age=21)
#task03
def student_details(name,age=21,*subject,**student_data):
    print(f"Name :{name}")
    print(f"Age :{age}")
    print(f"Subjects :{subject}")
    for key,value in student_data.items():
        print(f"{key} : {value}")
student_details("pavithra" ,22, "java" ,"python", "c",surname="Billupati",city="nellore")
#task04
def calculate_average(*numbers):
    total=0
    count=0
    for number in numbers:
        count+=1
        total=total+number
    avg=total/count
    return avg
average=calculate_average(2,8,9,6,8,56)
print(f"the average numbers {average}")
#task05
def calculate_grade(mark=50):
    if mark>=90 and mark<=100:
        return "A"
    elif mark>=75 and mark<=89:
        return "B"
    elif mark>=60 and mark<=74:
        return "C"
    elif mark>=50 and mark<=59:
        return "D"
    else:
        return "Fail"
grade=calculate_grade(87)
print(f"the grade for given marks {grade}")
#task06
def multiplication_table(number):
    table=""
    for i in range(11):
        table +=f"{number} x {i} = {i*number}\n"
    return table

result=multiplication_table(7)
print(result)
#task07
def cal_sum(*numbers):
    return sum(numbers)
print(cal_sum(5,9,7,8,90,76))
#task08
def even_num(*numbers):
    evennumbers=""
    for number in numbers:
        if number%2 == 0:
            evennumbers +=str(number)+" "
    return evennumbers
print(even_num(56,8,9,90,87,89,85,76,89))
#task09
def prime_num(number):
    for i in range(2,number):
        if number%i==0:
            return "not a prime number"
    return "prime number"
print(prime_num(10))
#task 10
def palindrome(word):
    r_word=reversed(word)
    if word==r_word:
        return "palindrome"
    return "not palindrome"
print(palindrome('pavithra'))
#task 11
def factors_num(number):
    fact=""
    for i in range(1,number+1):
        if number%i==0:
            fact +=str(i)+" "
    return fact
print(factors_num(86))
#task12
def pattern_piramid(number):
    for i in range (1,number+1):
        for j in range(number-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()
pattern_piramid(6)
#task13
def F_C(temp_in_cel):
    temp_in_fah=(temp_in_cel*(9/5))+32
    return temp_in_fah
print(F_C(32))
def C_F(temp_in_fah):
    temp_in_cal=(temp_in_fah-32)*(5/9)
    return temp_in_cal
print(C_F(43))
#task14
def even_odd(*numbers):
    evennumbers=""
    oddnumber=""
    for number in numbers:
        if number%2 == 0:
            evennumbers +=str(number)+" "
        else:
            oddnumber +=str(number)+" "
    return evennumbers ,   oddnumber
print(even_odd(56,8,9,90,87,89,85,76,89))
#task15
def shopping_total(price,quantity=1):
    total=price*quantity
    return total
print("total bill:",shopping_total(23,8))
#task16
def add_all(*numbers):
    total=0
    for number in numbers:
        total +=number
    return total
result=add_all(8,9,90,87,45)
print("the total sum :",result)
#task17
def greeting(name="pavithra",city="nellore"):
    return f"Hello {name},wellcome to {city}"
print(greeting("Venky"))
print(greeting("Somu","Anamthasagram"))'''
#task18
def minimum_num(*numbers):
    min_num=min(numbers)
    return min_num
def maximum_num(*numbers):
    max_num=max(numbers)
    return max_num
def average(*numbers):
    return sum(numbers)/len(numbers)
print("the minimum number  ",minimum_num(3,8,2,89,76,1))
print("the maximum number ",maximum_num(78,89,23,70,98,90))
print("the average is",average(4,8,97,76,98,56,23))

