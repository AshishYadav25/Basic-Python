# string indexing
name = "sonu"

# position(index number)

# s = 0 , -4
# o = 1 , -3
# n = 2 , -2
# u = 3 , -1

print (name[2])

# String slicing

lang = "Python" # 0, 1, 2, 3, 4, 5
# print (lang[4])
# syntax - [start argument : stop argument +1 ]

print (lang[0:3])
print (lang[2:4])
print (lang[3:6])
print (lang[:])
print (lang[2:])
print (lang[:3])

# Step argument slicing
# syntax - [start argument : stop argument +1 : step]

print ("Sonu"[1:3])

print ("Ashish" [0:4:2]) # Step argument 
print ("Ashish" [5::-1])

#Exercise
name = input("What is your name? ")
reverse = name [-1::-1]
print (f"reverse of your name is {reverse}")