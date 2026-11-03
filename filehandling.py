# Write:
# f = open("newfile.txt",'w')
# f.write("hello this is ")
# f.close()
# # # Read:
# f = open("newfile.txt",'r')
# read = f.read()
# print(read)
# f.close()
# # # Append:
# f = open("newfile.txt",'a')
# f.write("max")
# f.close()
# 
# f = open('newfile.dat','wb')
# f.write(b"hello this is me")
# f.close
# file = open('newfile.dat',"rb")
# content = file.read()
# print(content)
# file.close()
# file = open('newfile.txt','w')
# file.write('hello world')
# file.close()
# file = open('newfile.txt','r')
# lines = file.readline()
# print(lines)
# file.close()
# file = open('newfile.txt','w')
# file.writelines(['hey,'  'max,' 'anchl'])
# file.close()
# file = open('newfile.txt','r')
# lines = file.readline()
# print(lines)
# file.close()
# with open('newfile.txt','r')
# class Animal:
#     def lion(self,name):
#         print(name)
#     def cat(self,name):
#         print(name)
# object = Animal()
# object.lion("monty")
# object.cat("sonty")
# class Student:
#     school_name = "Holyangels"
#    
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
# 
#     def get__details(self):
#         print(f"Student name is {self.name} and her age is {self.age}")
# 
# o = Student("Anchl",20)
# o.get__details()
# 
# j = Student("Max",19)
# j.get__details()
# class Avenger:
#     team_name = "Avenger"   
#     def __init__(self,name,power):
#         self.name = name 
#         self.power = power
# 
#     def get__details(self):
#         print(f"{self.name} is an Avenger and his power is  {self.power}")
# 
# o = Avenger("Iron Man","Technology")
# o.get__details()
# 
# j = Avenger("Thor","Thunder")
# j.get__details()
# c = Avenger("Hulk",'Super strength')
# c.get__details()
# d = Avenger("Wanda","Mind control")
# d.get__details()
# class Animal:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
# 
#     def dog(self):
#         return(self.name,self.age)
#     def get__details(self):
#         print(f"His name is {self.name} and her age is {self.age}")
# 
# o = Animal("Coco", 3)
# o.get__details()

# class Wizard:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
#     def magic(self):
#         return(self.name,self.age)
#     def get__details(self):
#         print(f"His name is {self.name} and her age is {self.age}")
# o = Wizard("Harry potter",19)
# o.get__details()

# try:
#     print("A")
# except:
#     print("B")
# else:
#     print("C")
# def square(n):
#     return n*n
# print(square(5))
# def is_even(n):
#     return n % 2==0
# print (is_even)
# try:
#     file = open("data.txt","r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("file not found")

# def is_even(n):
#     return n % 2 ==0 
# print (is_even(2))
# print (is_even(3))
# try:
#     n = int(input("Enter a number :"))
#     print(n)
# except:
#     print("Please enter a valid number")
# def find_max(a, b, c):
#     if a >= b and a >= c:
#         return a 
#     elif b >= a and b >= c:
#         return b 
#     else:
#         return c 
# print(find_max(99,78,23))

# def safe_divide(a,b):
#     if b == 0:
#         print("cannot divide by zero")
#         return None
#         return a / b 
# print(safe_divide(2,0))

# safe_divide(2,0)
# def division(a,b):
#     try:
#         division = a / b 
#         print(division)
#     except:
        # print('cannot be divide by zero')
# a = int(input('enter a number '))
# b = int(input('enter a number '))
# division(a,b)

# def item(list,index):
#     try:
#         return list[index]
#     except:
#         print("list is out of index")
# print(item([1,2,3,4,5],2))

# def check_age(age):
#     if age < 0:
#         raise "Age cannot be negative"
#     print("Valid age")
# try:
#     check_age(8)
# except:
#     print("Invalid")

# class Grandfather:
#     def __init__(self,name,eyes):
#         self.name = name
#         self.surname = "Khan"
#         self.eyes = eyes
# 
# class Father(Grandfather):
#     def __init__(self,name,eyes,job):
#         super().__init__(name,eyes)
#         self.job = job
# 
# class child(Father):
#     def __init__(self,name,eyes,job,school):
#         super().__init__(name,eyes,job)
#         self.school = school
# 
#     def output(self):
#         print(f"{self.name} {self.eyes} {self.job} {self.school}")
# o = child("Anchl","Brown","Engineer","NSTI")
# o.output()
# print(o.surname)

# class Grandfather:
#     def __init__(self,name,eyes):
#         self.name = name
#         self.surname = "khan"
#         self.eyes = eyes
# 
# class Father:
#     def __init__(self,job):
#         self.job = job   
# 
# class child(Grandfather,Father):    
#     def __init__(self,name,eyes,job,school):
#         # super().__init__(self,name,eyes,job,school)
#         Grandfather.__init__(self,name,eyes)
#         Father.__init__(self,job)
#         self.school = school
#     def output(self):
#         print(f"{self.name} {self.eyes} {self.job} {self.school}")
# o = child('Gauri','brown','student','nsti')
# o.output()
# print(o.surname)

# class Grandfather:
#     def __init__(self,name,eyes):
#         self.name = name
#         self.surname = "K"
#         self.eyes = eyes

# class Father(Grandfather):
#     def __init__(self,name,eyes,job):
#         super().__init__(name,eyes)
#         self.job = job

# class child(Grandfather):
#     def __init__(self,name,eyes,school):
#         super().__init__(name,eyes) 
#         self.school = school

#     def output(self):
#         print(f"{self.name} {self.eyes} {self.school}")
# o = child('Max','Brown','Nsti')
# o.output() 
# print(o.surname)

# class BankAccount:
#     def __init__(self,account_number,holder_name,intial_balance):
#         self.__account_number = account_number
#         self.__holder_name = holder_name
#         self.__balance = intial_balance
#     def deposit(self,amount):
#         if amount > 0 :
#             self.__balance += amount
#             print("deposit successful")
#         else:
#             print("Deposit amount must be positive")
#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print("withdraw successful")
#         else:
#             print("Invalid amount")
# def get_balance(self):
#     print('balance:',self.__balance)
# def __str__(self):
#     return(f"account_number:{self.__account_number}\n"
#            f"holder_name:{self.__holder_name}\n"
#            f"intial_balance:₹{self.__intial_balance:.2f}")
# account = BankAccount("12345/9","Sara",1400)
# account.deposit(900)
# account.withdraw(700)

# class Father:
#     def __init__(self):
#                 self.__salary = 150000
#     def __upi(self,amount):
#                 self.__salary -= amount
#     def __send_receipt(self):
#                 print(f"Current balance is {self.__salary}")
#     def main(self):
#         amount = int(input("Enter the amount: "))
#         self.__upi(amount)
#         self.__send_receipt()
# Father=Father()
# Father.main()
 
# class Dog:
#         def sound(self):
#                 print("bark")
# class Cat:
#         def sound(self):
#                 print("Meow")
# Dog = Cat()
# Dog.sound()

# class calculator():
#         def add(self,a,b=0,c=0):
#                 print(a+b+c)
# c = calculator()
# c.add(5)
# c.add(3,6)
# c.add(5,6,7)

# class UPI:
#         def pay(self,amount):
#                 print(f"{amount} is paid via UPI")
# class Cash:
#         def pay(self,amount):
#                 print(f"{amount} is paid via Cash")
# def checkout(method,amount):
#         method.pay(amount)
# checkout(UPI(), 50000)
# checkout(Cash(), 3000)

# def demo(name,age):
#         print(name,age)
# demo("Kelly", 25)       

# def func1(*args):
#         print("Printing values: ")
#         for i in args:
#                 print(i)
# func1(20,40,60)
# func1(80,100)

# def calculator(a, b):
#         sum = a + b 
#         difference = a - b
#         return sum, difference
# result = calculator(40,10)
# print(result)

# def show_employee(name, salary = 9000):
#         print("Name:",name,"salary:",salary)
# show_employee("Ben",12000)
# show_employee("Jessa")

# def outer(a, b):
#         def inner():
#                 return a + b 
#         result = inner() + 5
#         return result
# print(outer(5,10))

# def addition(num):
#         if num == 0:
#                 return 0
#         else:
#                 return num + addition(num - 1)
# print(addition(10))

# def dispaly_student(name,age):
#         print(name,age)
# show_student = dispaly_student
# show_student("Emma", 26)

# def even_numbers():
#         return list(range(4, 30, 2))
# print(even_numbers())

# def largest(x):
#         big = x[0]
#         for num in x:
#                 if num > big:
#                         big = num
#         return big
# x = [4,6,8,24,12,2]
# print(largest(x))

# def print_info(**kwargs):
#         for key, value in kwargs.items():
#                 print(key + ":", value)
# print_info(name = "Alice", age = 30, city = "New York")

# def factorial(n):
#         if n == 0 or n == 1:
#                 return 1
#         else:
#                 return n * factorial(n - 1)
# number  = 5
# print("The factorial of",number, "is",factorial(number))

# global_var = 10
# def change_value():
#         global global_var
#         global_var = 20
# print("Intial:",global_var)
# change_value()
# print("Modified:",global_var)

# def describe_pet(animal_type,pet_name):
#         print("I have a",animal_type + ".")
#         print("My",animal_type + "'s name is",pet_name + ".")
# describe_pet("hamster","Harry")
# describe_pet(animal_type="dog",pet_name = "Willie")


