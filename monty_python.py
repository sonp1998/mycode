#!/usr/bin/env python3 

counter = 0 

while True: 
    counter += 1 
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess --> ")
    if answer.capitalize() == 'Brian': 
        print('correct')
        break
    elif counter ==3: 
        print('sorry, the asswer was Brian')
        break
    else:
        print("sory try again")
