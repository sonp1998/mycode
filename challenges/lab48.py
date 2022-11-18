#!/usr/bin/env python3 

#unique answers based on input provided
#control user errors 
#use at leaset 1 while loop

#What food matches your personality? 
#What were you like in high school? 
highschool_list = ['Messy', 'Regular', 'Class Clown']

#How do you spend your free time? 
freetime_list = ['Really Going For It', 'Chillin', 'Partying'] 

#Pick a celeb 
celeb_list = ['Miley Cyrus', 'Ryan Gosling' , 'Beyonce']
#user input on 3 questions
play_again = input('Would you like to start the personality quiz? (y or n)')

highschool = ' '
freetime = ''
celeb = ''

if play_again.lower() == 'y':

    highschool = input('What were you like in highschool? (Messy, Regular, Class Clown)\n>')
    freetime = input("How do you spend your free time? Really Going For It', 'Chillin', 'Partying'\n>")
    celeb = input("Pick a celebrity.('Miley Cyrus', 'Ryan Gosling' , 'Beyonce')\n>")

#first batch start : messy with any
if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[0]: 
            print("Congrats! You are a messy Miley cyrus that goes for it!")
if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[1]: 
            print("Congrats! You are a messy Ryan that goes for it!")
if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[2]: 
            print("Congrats! You are a messy Beyonce that goes for it!")
#first batch end


#second batch start : regualr with any
if highschool.title() == highschool_list[1]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[0]: 
            print("Congrats! You are a regular Miley cyrus that goes for it!")

if highschool.title() == highschool_list[1]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[1]: 
            print("Congrats! You are a regular Ryan that chills!")
        


if highschool.title() == highschool_list[1]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[2]: 
            print("Congrats! You are a regular Beyonce that chills!")
            
#second batch end

#third batch start class clown with any
if highschool.title() == highschool_list[2]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[0]: 
            print("Congrats! You are a class clown Miley cyrus that goes for it!")

if highschool.title() == highschool_list[2]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[1]: 
            print("Congrats! You are a class clown Ryan that goes for it!!")
        


if highschool.title() == highschool_list[2]:
    if freetime.title() == freetime_list[0]:
        if celeb.title() == celeb_list[2]: 
            print("Congrats! You are a class clown Beyonce that goes for it!!")
#third batch end

#fourth batch start chills with any 
if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[1]:
        if celeb.title() == celeb_list[0]: 
            print("Congrats! You are a messy Miley cyrus that chills!")

if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[1]:
        if celeb.title() == celeb_list[1]: 
            print("Congrats! You are a messy Ryan that chills!!")
        


if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[1]:
        if celeb.title() == celeb_list[2]: 
            print("Congrats! You are a messy Beyonce that chills!!")
#fourth batch end

#fifth batch start parties with any
if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[2]:
        if celeb.title() == celeb_list[0]: 
            print("Congrats! You are a messy Miley cyrus that parties!")

if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[2]:
        if celeb.title() == celeb_list[1]: 
            print("Congrats! You are a messy Ryan that parties!!")
        


if highschool.title() == highschool_list[0]:
    if freetime.title() == freetime_list[2]:
        if celeb.title() == celeb_list[2]: 
            print("Congrats! You are a messy Beyonce that parties!!")
#fifth batch end


elif play_again.lower() == 'n': 
    print('Goodbeye')

# else: 
#     print("Please type either y or n")




