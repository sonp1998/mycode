#!/usr/bin/env python3 
import os 


#unique answers based on input provided
#control user errors 
#use at leaset 1 while loop
#What food matches your personality? 



def main():
#THIS WILL CLAER THE SCREEN. VERY NEAT GIO
    os.system('clear')   

    #What were you like in high school? LIST #1
    highschool_list = ['Messy', 'Regular', 'Class Clown']

    #How do you spend your free time? LIST #2
    freetime_list = ['Really Going For It', 'Chillin', 'Partying'] 

    #Pick a celeb LIST #3
    celeb_list = ['Miley Cyrus', 'Ryan Gosling' , 'Beyonce']
    
    #define variables
    highschool = ''
    freetime = ''
    celeb = ''
    play_again = True

    start_quiz = input('Would you like to start the personality quiz? (y or n)\n>')
    if start_quiz == 'y':
        while play_again == True:
        # if play_again == 'n': 
            # break 
            #user input on 3 questions

            #if play_again.lower() == 'y':

            highschool = input('\nWhat were you like in highschool? (Messy, Regular, Class Clown)\n>')
            freetime = input("\nHow do you spend your free time? Really Going For It', 'Chillin', 'Partying'\n>")
            celeb = input("\nPick a celebrity.('Miley Cyrus', 'Ryan Gosling' , 'Beyonce')\n>")

            #first batch start : messy with any
            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[0]: 
                        #print("Congrats! You are a messy Miley cyrus that goes for it!")
                        print("\nYou are spaghetti and meatballs. You're classic and fun and a little messy. Sometimes even a little out of control. AND you have many wonderful talents (those are the meatballs).")
                        break
            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[1]: 
                        print("\nCongrats! You are a messy Ryan that goes for it!")
                        break
            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[2]: 
                        print("\nCongrats! You are a messy Beyonce that goes for it!")
                        break
            #first batch end


            #second batch start : regualr with any
            if highschool.title() == highschool_list[1]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[0]: 
                        print("\nCongrats! You are a regular Miley cyrus that goes for it!")
                        break

            if highschool.title() == highschool_list[1]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[1]: 
                        print("\nCongrats! You are a regular Ryan that chills!")
                        break
                    


            if highschool.title() == highschool_list[1]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[2]: 
                        print("\nCongrats! You are a regular Beyonce that chills!")
                        break
                        
            #second batch end

            #third batch start class clown with any
            if highschool.title() == highschool_list[2]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[0]: 
                        print("\nCongrats! You are a class clown Miley cyrus that goes for it!")
                        break

            if highschool.title() == highschool_list[2]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[1]: 
                        print("\nCongrats! You are a class clown Ryan that goes for it!!")
                        break
                    


            if highschool.title() == highschool_list[2]:
                if freetime.title() == freetime_list[0]:
                    if celeb.title() == celeb_list[2]: 
                        print("\nCongrats! You are a class clown Beyonce that goes for it!!")
                        break
            #third batch end

            #fourth batch start chills with any 
            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[1]:
                    if celeb.title() == celeb_list[0]: 
                        #print("Congrats! You are a messy Miley cyrus that chills!")
                        print("\nOh my god. You're pizza. You're effortlessly cool. You have very few enemies. And some people have strong opinions about you. But that's OK. You're flawless.")
                        break

            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[1]:
                    if celeb.title() == celeb_list[1]: 
                        print("\nCongrats! You are a messy Ryan that chills!!")
                        break
                    


            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[1]:
                    if celeb.title() == celeb_list[2]: 
                        print("\nCongrats! You are a messy Beyonce that chills!!")
                        break
            #fourth batch end

            #fifth batch start parties with any
            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[2]:
                    if celeb.title() == celeb_list[0]: 
                        print("\nCongrats! You are a messy Miley cyrus that parties!")
                        break
            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[2]:
                    if celeb.title() == celeb_list[1]: 
                        print("\nCongrats! You are a messy Ryan that parties!!")
                        break


            if highschool.title() == highschool_list[0]:
                if freetime.title() == freetime_list[2]:
                    if celeb.title() == celeb_list[2]: 
                        print("\nCongrats! You are a messy Beyonce that parties!!")
                        break
            #fifth batch end

    #Ask to play again y or n start
    
        play_again = input("\nWould you like to play again? (y or n) \n>")
        if play_again == "y":
            main()
            #play_again = True
                #HOW DO I MAKE THE LOOP RUN AGAIN??
        elif play_again == 'n':
            play_again = False
            print("\nGoodbye, you have chosen not to play again!!!!")
        else: 
            print("\nPlease input y or n")
            # elif play_again == 'n': 
            #     print('Goodbeye')

            # else:
            #     play_again = input('Would you like to play again? (y or n)') 
            #     if play_again == 'y':
            #         play_again = True
            #     else:
            #         play_again = False
                #contine (try to get code to ask would you like to play again / start of loop)
    else: 
        start_quiz == False
        print("\nGoodbye, you have opted to not start the quiz!")

#run main
if __name__ == "__main__":
   main()