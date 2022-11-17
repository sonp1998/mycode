#!/usr/bin/env python3 

def main(): 
    user_name = input("what is the users name?")
    day_week = input("what day of week is it?")
#METHOD 1: CONCATENATION
    # print("Hello, " + user_name + "! Happy " + day_week + "!") 

#METHOD 2: FORMAT METHOD 
    # print("Hello {}! Happy {}!".format(user_name,day_week)

#METHOD 3: F-STRING
    print(f"Hello, {user_name}! Happy {day_week}!")

main()

