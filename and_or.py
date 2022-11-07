# check two conditions at the same time
# and, or

name = 'abc'
age = 19

if name =='abc' and age == 19:
    print("condition true")

else:
    print("condition false")


if name =='abc' or age == 23:
    print("condition true")

else:
    print("condition false")


#Exercise 1

name = input("What is your name: ")
age = int(input("What is your age: "))

if (name[0] == "A" or "a") and age > 10:
    print("You can watch coco movie")

else:
    print("sorry, you cannot watch coco")


#Exercise 2

age = int(input("Your age: "))

if age == 0:
    print("Nil")

elif 1<=age<=3 :
    print("Ticket is Free")

elif 3<age<=10 :
    print("Ticket is 150")

elif 10<age<=60 :
    print("Ticket is 250")

else :
    print("Ticket is 200")


# in keyword
# if with in

name = "Ashish"

if "A" in name:
    print("Yes")
else:
    print("no")