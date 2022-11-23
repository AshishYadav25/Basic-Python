

# sum = 0
# i = 1
# n = int(input())

# while i <= n:
#     sum = sum + i
#     i = i + 1 
#     print (sum)

# n = input("Enter more than 1 digit number")
# sum = 0
# i = 0 
# # 1 4 5 3 6 .. [0 1 2 3 4 .. ] i = index

# # sum = int(n[0]) + int(n[1]) + int(n[2]) + .. + int(n[n-1])

# while i <= (len(n) - 1):
#     sum += int(n[i])
#     i += 1

# print (sum) 


# n = input("full name ")
# i = 0
# temp_var = ""
# total = 0
# while i< len(n):
#     if n[i] not in temp_var:
#         temp_var += n[i]
#         print (f"{(n[i])} : {n.count(n[i])}")
#     i += 1
    
# for i in range(3,8):
#     print(f"Hello World : {i}")

# sum= 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)


# sum = 0
# n = input("enter your number: ")
# for i in range (0, len(n)):
#     sum = sum + int(n[i])
# print(sum)


# n = input("enter name: ")
# var = ""

# for i in range (len(n)):

#     if n[i] not in var:
#         var += n[i]      
#         print(f"{n[i]} : {n.count(n[i])}")
# print(var)


# Exercise (Guessing number)

# import random
# winning_number = random.randint(1,100)

# n = int(input ("guess the number between 0 and 100: "))
# guess = 1
# game_over = False

# while not game_over:
#     if n == winning_number:
#         print(f"you win, you guessed the number in {guess} times")
#         game_over = True 

#     else:
#         if n < winning_number:
#             print ("too low")
#             guess += 1
#             n = int(input("enter another number: "))

#         else: 
#             print("too high")
#             guess += 1
#             n = int(input("enter another number: "))

num = input("enter your number: ")
sum = 0
for i in num:
    sum += int(i)
print(sum)
