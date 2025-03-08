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

'''program to show the sum of total hight of students'''


# student_heights = input("Input the list of student heights").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)

# #avg height
# total_height = 0
# for height in student_heights:
#   total_height += height
#   print(total_height)

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
# sum_of_total_height = round(total_height / number_of_students)
# print(sum_of_total_height)

'''Program To find the sum of all even numbers from 1 to 100 '''
# total = 0
# for number in range(1,101):
#   if number % 2==0:
#     total += number
#     print(total)


# total = 0
# for number in range(2,101,2):
#   total += number
# print(total)


# '''Program that prints fizz if the number is divisible by 3 and print buzz if the number is divisible by 5 ,if the number is 
# divisible by both 3 and 5 it prints fizz buzz'''

# for number in range(1,101):
#   if number % 3==0 and number % 5==0:
#    print("fizz buzz")
#   elif number % 3==0:
#    print("fizz")
#   elif number % 5==0:
#    print("buzz")
  
#   else:
#    print(number)

'''Program to generate the random password'''

# import random 
# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ["!", "@", "#", "$", "%", "+", "&", "*", "(", ")"]

# print("Welcome To The PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many number would you like?\n"))

# password = []
# for char in range(1,nr_letters + 1):
#   password +=random.choice(letters)
   
# for char in range(1,nr_symbols +1):
#   password +=random.choice(symbols)

# for char in range(1,nr_numbers +1):
#   password +=random.choice(numbers)
# random.shuffle(password)
# pasword = ""
# for char in password:
#   pasword += char
# print(f"Your password is {pasword}")

# ''' project  hangman game '''
# import random
# from wordlist import stages
# from wordlist import logo
# print(logo)
# from wordlist import word_list
# chosen_word = random.choice(word_list)
# lives = 6

# print(f'Pssst, the solution is {chosen_word}.')
# display =[]

# for letter in chosen_word:
#   display += "_"
# End_of_game = False
# while not End_of_game:
#     guess  = input("Guess the  letter:").lower() 
#     if guess in display:
#       print(f"You've already guessed {guess}")
    
#     for position in range(len(chosen_word)):
#       letter = chosen_word[position]
      
#       if letter == guess:
#         display[position] = letter
       
     
#     if guess not in chosen_word:
#       if guess in chosen_word:
#         print(f"You guess a letter :{guess}") 
#       else:
#         print(f"you guessed {guess}, that's not in the word.you lose a life.")
#       lives -= 1
#       if lives == 0:
#         End_of_game = True
#         print("You Lose")
#     print(f"{' '.join(display)}")
     

    
#     if "_" not in display:
#       End_of_game = True
#       print("You won")
#     print(stages[lives])





''' function'''
# def greeting():
#   print("Hello")
#   print("Hi")
#   print("Namaste")


# greeting()


# def greeting(name, location):
#   print(f"Hello {name}")
#   print(f"what is it like in {location} ")
 


# greeting(location = "ktm",name ="luffy")

''' program that calculate how many cans of paint we need to buy for a given 
surface area of wall.'''
# import math
# def paint_calc(height,width,cover):
#     area = height * width
#     numberofcans = math.ceil(area / cover)
#     print(f"the number of cans we need to by is {numberofcans}")
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

    
# paint_calc(height=test_h, width=test_w, cover=coverage)

''' program to check the number is prime or not '''
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number%i == 0:
#       is_prime = False
#   if is_prime:
#       print("It's a prime number.")
#   else:
#       print("It's not a prime number.")

# n = int(input("Check this number:"))
# prime_checker(number=n)


'''  program caesar cipher encription algorithm '''

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# should_continue = True
# while should_continue:
#   direction = input("Type 'encode'to encrypt Type 'decode' to decrypt:\n")
#   Text = input("Enter the text:\n")
#   shift = int(input("Type the shift number:\n"))
#   def caeser(plain_text, shift_amount,direc):
#     cypher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         if direc == "encode":            
#           new_position = (position + shift_amount)% 26
#           new_letter = alphabet[new_position] 
#           cypher_text += new_letter
    
#         elif direc == "decode":
#           new_position = (position - shift_amount)% 26
#           new_letter = alphabet[new_position] 
#           cypher_text += new_letter
#     print(f"The {direc} message is {cypher_text}")
#   caeser(plain_text = Text,direc=direction,shift_amount=shift)
#   result = input("Type 'Yes' if you want to continue again , Otherwise type 'no'.\n")
#   if result == "no":
#     should_continue = False
#     print("Good bye")


''' grading program '''

# student_score = {
#   "harry": 81,
#   "Ram": 91,
#   "luffy": 71,
#   "nami": 61,
#   "zoro": 99,
# }
# student_grade = {}
# for student in student_score:
#   score = student_score[student]
#   print(score)
#   if score >= 91 and score  <= 100:
#     student_grade[student] = "outstanding"
#   elif score >=81 :
#     student_grade[student] = "excallent"
#   elif score >=61 :
#     student_grade[student] = "good"
#   else:
#     student_grade[student] = "fail"
    


 
  
# print(student_grade)


''' nesting dictionary in a disctionary'''
# travel_log = {
#   "france": {"cities_visited": ["paris","lille","daijon"],"total_visits":12},
  
# }



''' Nesting dictionary in a list'''
# travel_log = [
#   {
#     "country":"france",
#     "cities_visited": ["paris","lille","daijon"],
#     "total_visits": 12
#   },
#   {
#     "country":"nepal",
#     "cities_visited": ["ktm","pokhara","kavre"],
#     "total_visits": 5
#   }
# ]

# print(travel_log)

''' program blind auction'''
# import os

# from wordlist import logo1
# print(logo1)
# bids = {}
# bidding_finished = False
# def find_highest_bidder(biding_record):
#   heighest_bid = 0
#   for bidder in biding_record:
#     bid_amount = biding_record[bidder]
#     if bid_amount > heighest_bid:
#       heighest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid {heighest_bid}")
# def clear_console():
#     os.system('clear' if os.name == 'nt' else 'clear') 
# while not bidding_finished:
#   name = input("what is your name?")
#   price = int(input("what is your bid? $"))
#   bids[name] = price
#   should_continue = input("Are there any bidders? type 'yes' or 'no'.").lower()
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear_console() 
  
''' Functions with outputs'''
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "you didn't provide valid inputs."
#     format_f_name = (f_name.title()) 
#     format_l_name = (l_name.title())
#     return  f"{format_f_name}{format_l_name }"   
 
# print(format_name(input("what is your first name ?"),input("what is your last name?"))) 
  

''' leap year'''


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year , month):
#   if month >12 or month < 1:
#     return "Invalid Month"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and month == 2:
#     return 29  
#   return month_days[month -1] 
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)   


''' program to cleate a calculator'''
import os
from wordlist import calculator_logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
    print(calculator_logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations: 
        print(symbol)

    should_continue = True


    while should_continue:

        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start new calculation:").lower()
        def clear_console():
            os.system('clear' if os.name == 'nt' else 'clear')
        if should_continue == "y":
            num1 = answer
        elif should_continue == "n":
            should_continue = False  
            clear_console()
            calculator()
calculator()

    



