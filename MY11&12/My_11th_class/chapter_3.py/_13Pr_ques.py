# Write a program to fill in a letter template given below with name and date.
# letter =  Dear <|NAME|>,

#                         You are selected!

#                         <|DATE|>

name = input("Enter the name ")
date = input("Enter date")
print("Dear ",name, "\n\tConratulations,you are selected. \n " ,"Date:" ,date)

#                 OR

Letter ='''Dear |<Name>|,
We are very happy to tell you that you are selected ..
Have a grat day ahead..
Date:|<date>|'''
name = input("Enter the name ")
date = input("Enter date")
Letter = Letter.replace("|<Name>|" , name)
Letter = Letter.replace("|<date>|" , date)
print(Letter)


