"""
Program 2: FUNCTIONS IN PYTHON
event management system 
"""

#! Assumption :

# in this scenario every commodity has a base price like hotel has a base price of 10000 and in varius countries price of these commodities are a certain multiple of the base price in their respective currency

# like in India hotel price is 100001 = 10000 rs in Dubai hotel price is 100001.5 = 15000 Dirham




#? Structure:

# location --> name, time, price multiple
# food --> dish_type, price
# hotel --> price
# decoration --> price

# tax --> 10%
# discount --> discount on diff slabs
# billing --> total

# currency --> user defined
# tax --> lambda
# printdata --> generator
# hotelPrice --> recursion

# user --> time --> number of people --> dish --> price


######      #######    #######      #########
##         #       #   ##     #     ##
##         #       #   ##     #     #########
##         #       #   ##     #     ##
######      #######    #######      #########

from datetime import timedelta # for adding days 
from datetime import datetime  # from handling date
import pandas as pd # for creating the dataframe 

# define location and with availability and price   
location = [{
        "name" : "Dubai",
        "from" : datetime(2021, 6, 7), 
        "upto" : datetime(2021, 10, 7),
        "price" : 1.5
    },
    {
        "name" : "Maldives",
        "from" : datetime(2021, 5, 17), 
        "upto" : datetime(2021, 11, 17),
        "price" : 1.2
    },
    {
        "name" : "morisas",
        "from" : datetime(2021, 7, 27), 
        "upto" : datetime(2021, 9, 27),
        "price" : 1.3
    },
    {
        "name" : "Udaipur",
        "from" : datetime(2021, 2, 15), 
        "upto" : datetime(2021, 10, 15),
        "price" : 1
}]

# food price data 
food = [
    ["Indian", 10000], 
    ["Chinese", 12000], 
    ["Itallian", 15000], 
    ["Thai", 18000]
]

# hotel and decoration price
hotel = 10000
decorator = 50000

# final booking
booking = []

# lambda function to calculate tax
tax = lambda a : a * 1.1

# generator function to generate location
def printLocation(arr) : 
    for location in arr : 
        yield location

# user defined function 
# to convert price into INR
def converter(country, money) :

    if country == "Dubai" : 
        return money*19.87
   
    elif country == "Maldives": 
        return money*4.72
   
    elif country == "morisas": 
        return money*1.72 
   
    else : 
        return money 

# dummylist to append into booking 
def dummyList(name, value) : 
    dummy = [name] 
    dummy.append(value)
    return dummy

# calculate discount 
def discount(price) :
    if price > 10000000 : 
        discount = price* 0.01
    elif price > 20000000 :
        discount = price* 0.02
    elif price > 30000000 :
        discount = price* 0.05
    elif price > 50000000 :
        discount = price* 0.1
    return (discount , price-discount)

# for creating the dataframe 
def createDataFrame(arr) : 
    df = pd.DataFrame(arr, columns =['Name', 'Value'])
    return df 

# recursion 
def hotelRoomPrice(price, multiple) : 
    if multiple == 1 : 
        return price # base case 
    
    return price+hotelRoomPrice(price,multiple-1) # recursive call 

# input date 
print('enter date (YY MM DD) : ')
year, month, date = map(int, input().split())
booking.append(dummyList('Starting Date', str(year)+'-'+str(month)+'-'+str(date))) # adding to final booking

start = datetime(year, month, date)
duration = int(input('Duration of the ceremony in days : '))
booking.append(dummyList('Duration', duration)) # adding to final booking

end = start + timedelta(days = duration) # calculating end date

suggestion = [] # for available locations 
for i in range(len(location)) : 
    if start >= location[i]['from'] and end <= location[i]['upto'] : 
        suggestion.append(location[i]['name']) # creating list for available location 

proceed = True 
while len(booking) == 2 : 
    
    if len(suggestion) == 0 : 
        print('No locations available in this period')
        proceed = False 
        break

    else :
        print('Available locations for you')    

        counter = 1
        for i in printLocation(suggestion) : 
            print('enter',counter,'for',i) # printing instruction for location selection
            counter += 1 

        place = int(input('enter your choice : ')) # printing selected place 

        print('you selected', suggestion[place-1])
        booking.append(dummyList('location', suggestion[place-1])) # adding to final booking

        multiple = 1
        for i in range(len(location)) : 
            if suggestion[place-1] == location[i]['name'] :
                multiple = location[i]['price'] # defining multiple 
                break
    
    person = int(input('enter number of guests : ')) 
    print('you will need',person//2,'rooms') # required rooms 
    print('room price', hotel*multiple) # room price 

    for i in range(len(food)) : 
        print('enter', i+1, 'for',food[i][0])  # printing instruction for food selection

    dish = int(input())
    print('you have selected ',food[dish-1][0],'dish costing', food[dish-1][1]*multiple,'per plate') # per plate price
    booking.append(dummyList('Food', food[dish-1][0])) # adding to final booking

    totalFoodPrice = food[dish-1][1]*person*multiple # total food price 
    booking.append(dummyList('Total food Price', totalFoodPrice)) # adding to final booking

    hotelPrice = hotelRoomPrice(hotel,(person//2))*duration*multiple # total hotel price
    booking.append(dummyList('Hotel Price', hotelPrice)) # adding to final booking
 
    decoratorPrice = decorator*multiple*duration # total decoraton price 
    booking.append(dummyList('Decoration Price', decoratorPrice)) # adding to final booking

    total = totalFoodPrice + hotelPrice + decoratorPrice # total price in foregin currency
    booking.append(dummyList('Total Price', total)) # adding to final booking

    afterTax = int(tax(total))  # tax calculate 
    taxPrice = afterTax - total 

    booking.append(dummyList('Tax Price', taxPrice))
    booking.append(dummyList('Final Price', afterTax)) # adding to final booking

    convertedPrice = converter(booking[2][1], afterTax) # INR price 
    booking.append(dummyList('INR', convertedPrice)) # adding to final booking
    
    print('Your budget is',convertedPrice)
 
    ans = input('Confirm booking (Y/N) : ') # confirmation

    if ans.lower() == 'n' : 
        print('Ok choose another destination') # go for another destination 
        suggestion.remove(booking[2][1]) # remove that location from suggestion
        for i in range(9) : 
            booking.pop() # removing all junk info from final booking 
    
    elif ans.lower() == 'y' : 
        print('Thanks for booking')

if proceed : 
    print('Here is you bill \n')
    if booking[-1][1] < 10000000 : # discount check 
        print(createDataFrame(booking)) # print df
    else : 
        discount, discountedPrice = discount(booking[-1][1])
        booking.append(dummyList("Discounted Price", discountedPrice)) # adding to final booking
        print(createDataFrame(booking)) # print df
