#!/usr/bin/env python3 

wordbank = ["identation", "spaces"]
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input("Input number between 0-20\n>"))
#num =int(input("pick student number"))
student_name = tlgstudents[num] 
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


