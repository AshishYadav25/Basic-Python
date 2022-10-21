# #if statment & else statement

# age = int(input("Enter your age "))
# if age >= 14:
#     print("You are eligible")

# else:
#     print("Not eligible")

# #pass statement

# x = 18
# if x >18:
#     pass

# #Exercise

# winning_number = 24

# guess_number = int(input("enter your any number between 1 and 100 "))

# if guess_number == winning_number:

#     print("YOU WIN !!!!")

# if guess_number > winning_number:

#     print("too high")

# if guess_number < winning_number:
    
#     print("too low")


# Another method with else

winning_number = 24

guess_number = int(input("enter your any number between 1 and 100 "))

if guess_number == winning_number: 
   print("You win !!!")
else:

    if guess_number < winning_number:
        print("too low")
    else:
        print("too high")