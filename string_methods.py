print (len("Hello")) # len() to count characters

name = "AsHiSh YAdAv" # len() function counts spaces 

print (len(name))

print(name.lower()) #lower method

print(name.upper()) #upper method

print(name.title()) #title method

print(name.count("A"))

#Exercise

name, char = input("Enter your first name and char ").split(",")
print (f"length of name is {len(name)}")


#replace method
#find method

string= "He is adonisss and he is chapri"
print(string.replace(" ","_"))
print(string.replace("is","was",1)) #replacing is with was for number of times 1

print(string.find("is", 5)) #finding position of is starting from index number 5

is_pos = string.find("is")

print(string.find("is", is_pos + 1))

#center method

name = "Ashish"
# **Ashish**, 10

print(name.center(10,"*"))

name = input("enter your name " )
print(name.center(len(name) + 8 , "*"))