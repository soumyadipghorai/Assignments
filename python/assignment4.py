"""
ATM PIN change 
"""

#! Algo :

# choose 

# ATM --> 11 (account num) --> 10 (ph num) --> 4 (OTP) --> new 

# SMS --> PIN CCCC AAAA --> OTP 

# BANKING --> ID PASSWORD --> SERVICE DROP DOWN --> ATM PIN --> ACCOUNT NUM --> DEBIT CARD NUM --> 2 DIGIT --> 2 SEND --> ENTER 4 DIGIT 

# IVRS --> 1800 425 3800/ 1800 1122 11 / 080 26599990 --> LAST 5 DIGIT OF CARD NUM --> 1ST 5 OF ACC NUM --> OTP --> TIME 2 DAYS --> NEW PIN 


######      #######    #######      #########
##         #       #   ##     #     ##
##         #       #   ##     #     #########
##         #       #   ##     #     ##
######      #######    #######      #########

import pandas as pd
import random

# main data structure 
detailsDict = [{
    'accountNum' : 98198723821, 
    'debitCard' : 1223133146469873, 
    'PIN' : 9873,
    'phoneNum' : 9173731221,
    'id' : 'abcd@gmail.com',
    'password' : 'abcdefgh'
    }, 
    {
    'accountNum' : 98168223821, 
    'debitCard' : 1243143146469874, 
    'PIN' : 1873,
    'phoneNum' : 9172731221,
    'id' : 'abcd2@gmail.com',
    'password' : 'abcdefghi'
}]



# parent class
class Bank(object) : 
    
    def displayBankDetails(self, target) : 
        
        try :
            account = self.findID(target)
            account = self.findWithAccountNum(target)
        except : 
            pass

        accountList = []
        for key in account.keys() : 
            valueList = [key]
            valueList.append(account[key])
            accountList.append(valueList)

        df = pd.DataFrame(accountList, columns = ['Name', 'Details'])
        print(df)

    def createOTP(self, digit) : 
        
        if digit == 4 : 
            OTP = random.randint(1000,9999)  
            return OTP
        elif digit == 2: 
            OTP = random.randint(10,99) 
            return OTP 

    def enterOTP(self) : 
        alert = True 
        OTP = self.createOTP(4)
        print(f'Your OTP is {OTP}')
        try :
            val = int(input('Enter OTP : '))
        except : 
            print('Wrong OTP')
            alert = False 

        if val != OTP and alert: 
            print('Wrong OTP')
            self.enterOTP()
    
    def setPIN(self, target) : 

        account = self.findWithAccountNum(target)
        try : 
            password = int(input('Enter new PIN of 4 digit : '))
            if len(str(password)) != 4 : 
                self.setPIN()
            else : 
                account['PIN'] = password
                return print('PIN updated!') 
        except : 
            password = int(input('Enter 4 digit number : '))
            account['PIN'] = password 

    def findWithAccountNum(self, target) : 

        for i in range(len(detailsDict)) : 
            if detailsDict[i]['accountNum'] == target : 
                return detailsDict[i]
        else : 
            return False 

    def findID(self, target) : 

        for i in range(len(detailsDict)) : 
            if detailsDict[i]['id'] == target : 
                return detailsDict[i]
        else : 
            return False 

    def matchDebitAcc(self, target, category) : 

        if category == 1 :
            for i in range(len(detailsDict)) : 
                if int(str(detailsDict[i]['debitCard'])[-4:]) == target : 
                    return detailsDict[i]
            else : 
                return False

        if category == 2 : 
            for i in range(len(detailsDict)) : 
                if int(str(detailsDict[i]['debitCard'])[-5:]) == target : 
                    return detailsDict[i]
            else : 
                return False 

# --------------------------------------------child class------------------------------------------- 
class ATM(Bank) :

    def __init__(self, accountNum, phoneNum) : 
        self.accountNum = accountNum
        self.phoneNum = phoneNum 
        self.flag = True 
        self.count = 0

    def check(self) : 
        
        if self.findWithAccountNum(self.accountNum) :

            if self.findWithAccountNum(self.accountNum)['phoneNum'] != self.phoneNum : 
                self.phoneNum = int(input(f'Enter the correct Phone Num you have {3-self.count} try left  : '))
                self.count += 1 
                if self.count == 3 : 
                    self.flag = False  
                    print('Your account is blocked!') 
                    return False 
                if self.flag : 
                    self.check()

        else : 
            self.accountNum = int(input(f'Enter the correct Account Num you have {3-self.count} try left  : ')) 
            self.count += 1 
            if self.count == 3 : 
                self.flag = False  
                print('Your account is blocked!')
                return False 
            if self.flag : 
                self.check()

        return True 

    def updatePIN(self) : 
        self.setPIN(self.accountNum)

    def display(self) : 
        self.displayBankDetails(self.accountNum)

class SMS(Bank) : 
    
    def __init__ (self, debitCard, accNum) : 
        self.debitCard = debitCard
        self.accNum = accNum
        self.flag = True 
        self.count = 0

    def check(self, category) : 

        if category == 1 :
            cardPos, numPos, digit = 'last', 'last', 4
        else : 
            cardPos, numPos, digit = 'last', 'first', 5

        if self.matchDebitAcc(self.debitCard, category) :

            if category == 1 : 
                if int(str(self.matchDebitAcc(self.debitCard, category)['accountNum'])[-4:]) != self.accNum : 
                    self.accNum = int(input(f'Enter the correct {numPos} {digit} digits of acc num! you have {3-self.count} try left  : '))
                    self.count += 1 
                    if self.count == 3 : 
                        self.flag = False  
                        print('Your account is blocked!')
                        return False 
                    if self.flag : 
                        self.check(category) 

            elif category == 2 :
                if int(str(self.matchDebitAcc(self.debitCard, category)['accountNum'])[:5]) != self.accNum : 
                    self.accNum = int(input(f'Enter the correct {numPos} {digit} digits of acc num! you have {3-self.count} try left  : '))
                    self.count += 1 
                    if self.count == 3 : 
                        self.flag = False  
                        print('Your account is blocked!')
                        return False 
                    if self.flag : 
                        self.check(category)
             
        else :  
            self.debitCard = int(input(f'Enter the correct {cardPos} {digit} digits of debit card! you have {3-self.count} try left  : '))
            self.count += 1 
            if self.count == 3 : 
                self.flag = False  
                print('Your account is blocked!') 
                return False 
            if self.flag : 
                self.check(category) 
        
        return True 

    def updatePIN(self) : 
        account = self.matchDebitAcc(self.debitCard, 1)
        self.setPIN(account['accountNum'])

    def display(self) : 
        account = self.matchDebitAcc(self.debitCard, 1)
        self.displayBankDetails(account['accountNum'])

class BANKING(Bank) :
    
    def __init__(self, ID, password) : 
        self.ID = ID 
        self.password = password 
        self.flag = True 
        self.count = 0

    def check(self) :

        if self.findID(self.ID) :

            if self.findID(self.ID)['password'] != self.password : 
                self.password = input(f'Enter the correct password! you have {3-self.count} try left  : ')
                self.count += 1 
                if self.count == 3 : 
                    self.flag = False  
                    print('Your account is blocked!') 
                    return False 
                if self.flag : 
                    self.check() 

        else : 
            self.ID = input(f'Enter the correct email! you have {3-self.count} try left  : ')
            self.count += 1 
            if self.count == 3 : 
                self.flag = False  
                print('Your account is blocked!') 
                return False 
            if self.flag : 
                self.check()

        return True
        
    def returnAccDebit(self) : 
        account = self.findID(self.ID)

        return account['accountNum'], account['debitCard']

    def generatePIN(self) :
        return random.randint(10,99) 

    def newPIN(self, first) : 

        account = self.findID(self.ID)

        alert = True
        last = self.generatePIN()
        PIN = int(str(first) + str(last)) 
        print(f'Your last two digit is {last}')
        try :
            val = int(input('Enter your pin : ')) 
        except : 
            print('Wrong pin')
            alert = False 
        
        if val != PIN and alert: 
            print('Wrong PIN')
            self.newPIN(first) 
        else : 
            account['PIN'] = PIN 

    def display(self) : 
        self.displayBankDetails(self.ID)

class IVRS(SMS) : 
    
    def __init__(self, debitCard, accNum) : 
        self.debitCard = debitCard
        self.accNum = accNum
        self.flag = True 
        self.count = 0

    def updatePINIVRS(self) : 
        account = self.matchDebitAcc(self.debitCard, 2)
        self.setPIN(account['accountNum'])

    def displayIVRS(self) : 
        account = self.matchDebitAcc(self.debitCard, 2)
        self.displayBankDetails(account['accountNum'])
        
# driver code 

# data for driver code
options = ['ATM', 'SMS', 'BANKING', 'IVRS']
nums = ['1800 425 3800', '1800 1122 11', '080 26599990']
sevice = ['service1', 'service2', 'ATM PIN', 'service4']

# takes input for the option
for i in range(len(options)) : 
    print(f'Press {i+1} for {options[i]}')
n = int(input())

if n == 1 : 
    accountNum = int(input('Enter you account Num : '))
    phoneNum = int(input('Enter you phone Num : '))
    user = ATM(accountNum, phoneNum) 
    if user.check() : 
        user.enterOTP() 
        user.updatePIN()
        user.display()

if n == 2 : 
    debitCard = int(input('Enter last 4 digits of your Debit card : '))
    accNum = int(input('Enter last 4 digits of your acc num : '))
    user = SMS(debitCard, accNum) 
    if user.check(1) : 
        user.enterOTP() 
        user.updatePIN() 
        user.display() 

if n == 3 :
    id = input('Enter email : ')
    pwd = input('Enter password : ')
    user = BANKING(id, pwd) 
    if user.check() : 
        for i in range(len(sevice)) : 
            print(f'Type {i + 1} for {sevice[i]}')
        val = int(input())
        if val == 3 : 
            print('Your Account Num is', user.returnAccDebit()[0])
            print('Your Debit card Num is', user.returnAccDebit()[1])
            try : 
                first = int(input('Enter the 1st two digit of the new PIN : '))
            except : 
                first = int(input('Enter two digit : '))
            user.newPIN(first) 
            user.display() 

        else : 
            print('OK!')

if n == 4 : 
    for phnum in range(len(nums)) : 
        print(f'Type {phnum + 1} for {nums[phnum]}')
    val = int(input())
    debitCard = int(input('Enter last 5 digits of your Debit card : '))
    accNum = int(input('Enter first 5 digits of your acc num : '))
    user = IVRS(debitCard, accNum) 
    if user.check(2) : 
        user.enterOTP() 
        user.updatePINIVRS() 
        user.displayIVRS() 
