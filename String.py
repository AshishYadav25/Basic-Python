first_name = "Ashish"
last_name = "Yadav"
 
print(first_name + " " + last_name)
print(first_name + "3")
print(first_name *3)

#User Input 
# We use Input function

name = input("Type your name") 
print("hello " +name)

#input function takes i/p always as string
age = input("What is your age? ")
print(age)   # "24" is string not integer 

name = input("enter your name : ")
age = input("enter your age : ")

#OR 
name, age = input("enter your name and age").split() #User can put 2 values at once
print(name)
print(age)