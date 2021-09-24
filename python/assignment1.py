"""
P1: Program to demonstrate the working of mutable and immutable types in Python

college registration system
"""

######      #######    #######      #########
##         #       #   ##     #     ##
##         #       #   ##     #     #########
##         #       #   ##     #     ##
######      #######    #######      #########


# import libraries 
import pandas as pd
import numpy as np

# define list of lists
bangalore = [['Date of establishment ', '28-03-1970'], 
             ['Course type' , 'Diploma'], ['Course Fess', 10000],
             ['Seats available', 50], ['Course duration', '2 years'], ['Semester' , 4]]

bangaloreCentral = [['Date of establishment ', '08-04-1960'], 
                    ['Course type' , 'Diploma'], ['Course Fess', 18000], 
                    ['Seats available', 20], ['Course duration', '2 years'], ['Semester' , 4]]

Delhi = [['Date of establishment ', '18-03-1990'],
         ['Course type', 'Degree'], ['Course Fess', 15000], 
         ['Seats available', 30], ['Course duration', '2 years'], ['Semester' , 4]]

# define dictionary
Pune = {
    'Date of establishment ' : '22-03-1998', 
    'Course type' : 'Certificate', 
    'Course Fess' : 12000, 
    'Seats available' : 40, 
    'Course duration' : '1 year', 
    'Semester' : 4
}


# creating dataframe 
bangaloreDf = pd.DataFrame(bangalore, columns = ['Name','Details'])
DelhiDf = pd.DataFrame(Delhi, columns = ['Name','Details'])
bangaloreCentralDf = pd.DataFrame(bangaloreCentral, columns = ['Name','Details'])
PuneDf = pd.DataFrame.from_dict(Pune, orient='index', columns = ['Details'])
PuneDf.reset_index(inplace =True)
PuneDf.rename(columns = {'index' : 'Name'}, inplace = True)

# dataframe list
courseDetails = [[bangaloreDf, PuneDf], [DelhiDf, bangaloreCentralDf]]

# tuple 
online = ("Bangalore", "Pune")
offline = ("Delhi", "bangalore Central")

mode = ["online", "offline"]
campusOptions = [online, offline]

registration = []

while True : 

    studentDetails = [] # student list 

    name = input('Enter your name : ')
    studentDetails.append(name) # add name 

    # error handling 
    try :
        courseType = int(input("Choose your preffered mode \n 1 for online \n 2 for offline : "))
    except : 
        courseType = int(input('Enter 1 or 2 : '))

    print('You choosed '+ str(mode[courseType-1]) + ' mode') # mode you choosed
    print("You have "+ str(len(campusOptions[courseType-1])) + "  options") # options you have

    for i in range(len(campusOptions[courseType-1])) : 
        print((i+1),' for ', campusOptions[courseType-1][i]) # instruction for each selection

    # error handling 
    try : 
        n = int(input())
    except : 
        n = int(input('enter integer : '))

    print('You choosed '+ campusOptions[courseType-1][n-1] + ' campus \nHere is your course details \n') # choosed campus 

    print(courseDetails[courseType-1][n-1]) # campus details 
    print()

    answer = input('Do you want to enroll? Y/N : ') 

    if answer.lower() == 'y' : # made the input lower case 

        age = int(input('Enter you age : '))
        phoneNumber = int(input('Enter your phone number : '))

        studentDetails.append(age)
        studentDetails.append(phoneNumber) 
        studentDetails.append(campusOptions[courseType-1][n-1]) # if yes take info and add to student list

    elif answer.lower() == 'n' : 
        answer2 = input('Do you want another campus? Y/N :')

        if answer2.lower() == 'y' : 
            continue 
        
        else : 
            studentDetails.append(np.nan)
            studentDetails.append(np.nan)
            studentDetails.append(np.nan) # if no fill places with nan value

    registration.append(studentDetails) # finally add to registration list

    answer3 = input('Want to continue? Y/N : ') # for next person 

    if answer3.lower() == 'y' : 
        continue 
    
    else : 
        break 

registrationDf = pd.DataFrame(registration, columns = ['Name','Age', 'Phone number', 'Campus'])

print('\nRegistration list : \n')
registrationDf