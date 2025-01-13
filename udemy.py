""" #Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")

"""
# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the '+' sign.")
# print("e.g. print('Hello ' + 'world')")
# print(("New lines can be created with a backslash and n."))



'''
# print(len (input("what is your name ") ) )'''


'''#day1:0012'''
# 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")

# c = a
# a = b
# b = c

# print("a: " + a)
# print("b: " + b)

'''program that generate bandname by combining cityname + petname'''
# print("Welcome to the Band Generator.")
# cityname = input("What's your name of the city you grew up in?\n")
# petname = input("What's your pet's name?\n")
# print("Your band name could be "+ cityname + ' ' + petname )



# two_digit_number = input("Type a two digit number: ")
# a =int (two_digit_number[0])
# b =int (two_digit_number[1])
# print(a+b)


'''
()
/*
-+

# print(3*3/3-3+3)'''


''' body mass index BMI=weight(kg)/height**(m**)'''
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# height =float(height)
# weight =int(weight)
# BMI =int (weight/height ** 2)
# print(BMI)

''' program to find out the remaining life spain if the person live for 90 years'''

# age = input("what is your current age")
# age = int(age)
# year = int(90-age)
# days = int(year*365)
# week = int(90*365/7)
# month = int(90*365/30)
# print(f"you have{year}year,{days}days,{week}week,{month}months left")

''' program tip claculator to calculate tip and split the total bill into given people'''
# print("Welcome to tip calculator")
# totalbill = input("what was the total bill?")
# tip_percent = input('what percentage tip would you like to give?')
# totalbill = int(totalbill)
# tip_percent = int(tip_percent)
# tippercent = (totalbill*tip_percent/100)
# new_total_percent = (totalbill + tippercent)

# dividbill=input("how many people to split the bill")
# billperperson = (float(new_total_percent)/float(dividbill))
# print(f"Each person pay RS{billperperson}")


''' program to check whether the number is odd or even'''

# number = int(input("Enter the number you want to check "))

# if number % 2 == 1: 
#     print("The number is odd")
# else:
#     print("The number is even")


'''program to check if the person can ride rollercoaster and how much do the person pay for it.'''

# print("Welcome to the rollcoaster")
# height = int(input("Enter your height in cm:"))
# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("what's your age"))
#     if age <= 12:
#         print("you have to pay RS 50.")
#     elif age <= 18: 
#         print("you have to pay RS 100.")
#     elif age >= 45 and age <=55:
#         print("you  dont have to pay")
#     else:
#         print("you have to pay RS 150.")   
# else:
#     print("you can't ride the rollercoaster")


'''body mass index BMI=weight(kg)/height**(m**)
 program that interpretation the body mass index based on uder weight and height.'''
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# height =float(height)
# weight =int(weight)
# BMI =round(weight/height ** 2,2)
# print("Your BMI is ",BMI)
# if BMI < 18.5:
#     print("you are under weight")
# elif BMI > 18.5 and BMI < 25:
#     print("you have a normal weight")
# elif BMI > 25 and BMI <30:
#     print("you are over weight")
# elif BMI > 30 and BMI <35:
#     print("you are obese")
# else:
#     print("you are clinically obese")


''' program to check whether the year is leap year or not '''

# year = int(input("Which year do you want to check? "))

# # Correct leap year logic
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")


# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


''' Automatic pizza order program '''

# print("Welcome to python pizza deliveries")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want to add pepperoni? Y, or N: ")
# extra_cheese = input("Do you want to add extra cheese? Y, or N: ")
# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else :
#     bill = 25
# # else:S
# #     print("Invalid size")
# #     exit()

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:  # M or L
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total bill is ${bill}")



    
''' program love calculator '''

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name?\n") 
# name2 = input("What is your name?\n") 

# name1 .lower()
# T=name1 .count("t")
# R=name1 .count("r")
# U=name1 .count("u")
# E=name1 .count("e")

# name2 .lower()
# L=name2 .count("l")
# O=name2 .count("o")
# V=name2 .count("v")
# E=name2 .count("e")
# Lovescore1 = str(T+R+U+E) 
# Lovescore2 = str(L+O+V+E)
# totalscore = (Lovescore1 + Lovescore2)
# if int(totalscore) <=10 or int(totalscore) >= 90:
#     print(f"Your score is {totalscore},you go like coke and mentos.")
# elif int(totalscore) >=40 or int(totalscore) <= 50:
#     print(f"Your score is {totalscore},you are alright together.")
# else:
#     print(f"your score is{totalscore}")

# program simple tresure game
# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/
# *******************************************************************************''')
# print("Welcome to Tresure Island. Your mission is to find the treasure.")
# print("You are at the cross road.Where do you want to go?")
# direction = input('Type "left" or "right" ').lower()

# if direction == "right":
#     print("you come to a lake .There is a Island in the middle of the lake.") 
#     direction1 = input('Type "wait" to wait for a boat.Type "swim" to swim across').lower()  
#     if direction1 == "wait":
#         print("You arrive at the Island unharmed.")   
#         direction2 = input('There is a house with 3 doors one "red" one "yellow" one "blue" which color do you want to choose?').lower()  
#         if direction2 == "yellow":
#          print("You Win!")  
#         elif direction2 == "blue":
#          print("Eaten by beasts.Game Over") 
#         elif direction2 == "red": 
#          print("Burned bu fire Game Over")
#         else:
#             print("Game Over")
#     elif direction1 == "swim":
#         print("You have been Attacked by trout.Game over")

#     else:
#         print("Game Over")
# elif direction == "left":
#     print("You fall into a hole.Game over")

# else : 
#      print("Game Over")


''' program using random module that creat head and tail game'''
# import random
# player1 = input('Head"head" or Tail "tail"').lower()
# if player1 == "head":
#     print("Head")
# else:
#     print("Tail")

# random_integer = random.randint(1,100)
# player2 = random_integer
# if player2 % 2 == 0:
#     print("Head")
# else:
#     print("Tail")


'''program that choose random person from the list to pay the bill'''
# import random
# name_string = input("Give me everybody's names, seperated by comma,")
# names = name_string.split(",")
# lenth = len(names)
# random_choice = random.randint(0,lenth -1)
# person_who_pay_bill = names[random_choice]
# print(f"The persion who will be paying bill is\n{person_who_pay_bill}")


'''program to put X mark in given place in the nestedlist'''

# row1 = ["😊","😊","😊"]
# row2 = ["😊","😊","😊"]
# row3 = ["😊","😊","😊"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("where do you want to put the treasure?")


# horizonal = int(position[0])#2
# vertical = int(position[1])#3

# selected_row = map[vertical-1]
# selected_row[horizonal - 1]="x"
# print(f"{row1}\n{row2}\n{row3}")
  


''' program
 rock
  paper
   seasor
    game
'''
# import random
# user_choice = int(input('What do you want to choose ? Type "0"for rock or "1" for scissor or "2" for scissor\n'))
# if user_choice == 0:
#     rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#     print(rock)
# elif user_choice == 1:
#     paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#     print(paper)
# elif user_choice == 2:
#     scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#     print(scissors )
# else:
#     print("invalid choice")
# print("Computer\n")
# random_integer = random.randint(0,2)
# if random_integer == 0:
#     rock1 = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#     print(rock1)
# elif random_integer == 1:
#     paper1 = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#     print(paper1)
# elif random_integer == 2:
#     scissors1 = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#     print(scissors1)

 
# if user_choice == random_integer:
#     print("Draw")
# elif user_choice == 0 and random_integer == 1 or user_choice == 1 and random_integer == 2:
#     print("you lose")
# else:
#     print("You win")

student_heights = input("Input the list of student heights").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#avg height
total_height = 0
for height in student_heights:
  total_height += height

number_of_students = 0
for student in student_heights:
  number_of_students += 1
  

sum_of_total_height = round(total_height / number_of_students)
print(sum_of_total_height)


