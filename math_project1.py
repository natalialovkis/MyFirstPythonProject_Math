# -*- coding: utf-8 -*-
 
#Math learning program
import random

print("Hello Dear User!")
name = input("Please, enter your name: ")
print()
print("Hello %s! Let`s learn the Math!" % name)
print()

    
num_of_ex = 0
while True:
    try:
        num_of_ex = int(input("How many exercises are you going to solve? Enter a number from 1 to 10: "))
        if 1 <= num_of_ex <= 10:
            break
        print("try again")
    except ValueError:
        print("That's not an int!")

user_try = 0
while user_try < num_of_ex:
    first = random.randint(1,11) #generate number between 1 and 100
    second = random.randint(1,11)
    action = random.randint(1,4) # 1=+; 2=-; 3=*; 
    
    if action == 1:
        answer = first + second
        try:
            user_input = int(input("What is result of %d + %d :" %(first,second)))
            if user_input == answer:
                print("Good!")
            else:
                print("Not right")
            
        except ValueError:
            print("That's not an int!")    
       
    elif action == 2:
        answer = first - second
        try:
            user_input = int(input("What is result of %d - %d :" %(first,second)))
            if user_input == answer:
                print("Good!")
            else:
                print("Not right")
            
        except ValueError:
            print("That's not an int!")   
            
    else:
        answer = first * second
        try:
            user_input = int(input("What is result of %d * %d :" %(first,second)))
            if user_input == answer:
                print("Good!")
            else:
                print("Not right")
            
        except ValueError:
            print("That's not an int!")    

            
    user_try += 1
    
print()
print("Good job! Bye!")
print()
input("Press enter to exit.")

        
    