name = "Ashish"
age = 25
print ("Hello " + name + " your age is " + str(age))

print("Hello {} your age is {} ".format(name,age)) #Python3 formatting

print(f"Hello {name} your age is {age}") #Python3.6 formatting --> Never forget f
print(f"Hello {name} your age is {age +2}") 

#Exercise 
#Method 1

a= int(input("number_1"))
b= int(input("number_2"))
c= int(input("number_3"))

avg = int((a+b+c)/3)
print("Average of all number is " + str(avg))

#Method 2

a, b, c = input("three numbers are ").split(",")
avg = (int(a)+int(b)+int(c))/3
print("Average of all number is " + str(avg))