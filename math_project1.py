# -*- coding: utf-8 -*-

# Math learning program
import random
import math
import turtle

print("Hello Dear User!")
name = input("Please, enter your name: ")
print()
print("Hello %s! Let`s learn the Math!" % name)
print()


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
            else:
                print("Not right")

        except ValueError:
            print("That's not an int!")
    user_try += 1

print()
print("Good job! Bye!")
print()
input("Press enter to see a surprise.")

radius = 100
petals = num_of_ex


def draw_arc(b, r):
    c = 2*math.pi*r
    ca = c/(360/60)
    n = int(ca/3)+1
    l = ca/n
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))


def draw_petal(b, r):
    draw_arc(b, r)
    b.lt(180-60)
    draw_arc(b, r)
    b.rt(360/petals-30)
bob = turtle.Turtle()

for i in range(petals):
    draw_petal(bob, radius)
    bob.lt(360/4)
