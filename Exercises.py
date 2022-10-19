
#Exercise1

# name = input("What is your name ")
# print (f"Reverse of your name is {name[::-1]}")

#Exercise2

name, char = input("Enter your name and character ").split(",")
print (len(name))
print(name.upper().count(char.upper())) #Make name Upper case and character upper case
# char.upper()
# print (name.count(char))

# new way with removing spaces

name, char = input("Enter your name and character ").split(",") # "  Ashish  " --> "Ashish" --> "ASHISH" // "  h  " --> "h" --> "H"
print (len(name.strip()))
print (name.strip().upper().count(char.strip().upper())) 