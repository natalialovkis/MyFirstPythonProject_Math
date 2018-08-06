# -*- coding: utf-8 -*-
# Math learning program
import random
import math
import turtle
import matplotlib.pyplot as plt
from name_class import NameClass

print("Hello Dear User!")
name = str(input("Please, enter your name: "))
name2 = str(input("Please, enter your last name: "))

my_user = NameClass(name, name2)
print(my_user.say_hello())

num_of_ex = 0
while True:
    try:
        num_of_ex = int(input("How many exercises are you going to solve? "
                              "Enter a number from 1 to 10: "))
        if 1 <= num_of_ex <= 10:
            break
        print("try again")
    except ValueError:
        print("That's not an int!")

user_try = 0
solved_size = 0
while user_try < num_of_ex:
    first = random.randint(1, 11)  # generate number between 1 and 100
    second = random.randint(1, 11)
    action = random.randint(1, 4)  # 1=+; 2=-; 3=*;

    if action == 1:
        answer = first + second
        try:
            user_in = int(input("What is result "
                                "of %d + %d :" % (first, second)))
            if user_in == answer:
                print("Good!")
                solved_size += 1
            else:
                print("Not right")

        except ValueError:
            print("That's not an int!")

    elif action == 2:
        answer = first - second
        try:
            user_in = int(input("What is result "
                                "of %d - %d :" % (first, second)))
            if user_in == answer:
                print("Good!")
                solved_size += 1
            else:
                print("Not right")

        except ValueError:
            print("That's not an int!")

    else:
        answer = first * second
        try:
            user_in = int(input("What is result "
                                "of %d * %d :" % (first, second)))
            if user_in == answer:
                print("Good!")
                solved_size += 1
            else:
                print("Not right")

        except ValueError:
            print("That's not an int!")
    user_try += 1

# make pi chart
labels = 'Unsolved...', 'Done!'
solved_percent = int(solved_size * 100 / user_try)
unsolved_percent = 100 - solved_percent
sizes = [unsolved_percent, solved_percent]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

print()
print("Good job! Bye!")
print()
input("Press enter to see a surprise.")

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Surprize")

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20
for i in range(num_of_ex + 20):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

wn.exitonclick()
