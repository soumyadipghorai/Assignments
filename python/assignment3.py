"""
Lab Program3: Inheritance

tokyo olympic 
"""

#! Algo :

# 1st we cosider the olympic parent class :
# from there we have 3 child class viz paralympic, summer olympic, winter olympic (Hierarchical Inheritance)
# there we have functions to find winners in each category in each sports
# then we have worldrecord class to find the ultimate champ among all the 3 categories (Multiple Inheritance)

######      #######    #######      #########
##         #       #   ##     #     ##
##         #       #   ##     #     #########
##         #       #   ##     #     ##
######      #######    #######      #########

# import module
from tabulate import tabulate
import pandas as pd

# defining sports data structure 
sprint = {
    'summer' : [],
    'winter' : [],
    'paralympic' : []
} 

swim = {
    'summer' : [],
    'winter' : [],
    'paralympic' : []
}

country = {}

# parent class 
class Olympic :

    # constructor 
    def __init__(self, name, age, country, category = None, sports = "", time = 0) :
        self.name = name 
        self.age = age 
        self.country = country 
        self.category = category
        self.sports = sports 
        self.time = time

    # to print elements 
    def display(self) : 
        print('Name : ',self.name)
        print('Age : ', self.age)
        print('Counrty : ', self.country)
        print('category : ', self.category)
        print('sport : ', self.sports)
        print('time : ', self.time)

    # dummy list to add 
    def createDummy(self) : 
        return [self.name, self.time, self.country]

    # print sports list 
    def displayList(self, sport) : 
        if sport == 'sprint' : 
            print(sprint)
        elif sport == 'swim' : 
            print(swim)

    # print all name with their timings 
    def displayTable(self, sport) :
        data = [] 
        if sport == 'sprint' : 
            for player in (sprint[self.category]) : 
                data.append([player[0], player[1], player[2]])
        elif sport == 'swim' : 
            for player in (swim[self.category]) : 
                data.append([player[0], player[1], player[2]])

        head = ["Name", "Time", "Country"]
        print(tabulate(data, headers=head, tablefmt="grid")) 

    def displayNameIn(self, sport) : 
        if sport == 'sprint' : 
            for player in (sprint[self.category]) : 
                print(player[0], 'finished in', player[1], 'secs')
        elif sport == 'swim' : 
            for player in (swim[self.category]) : 
                print(player[0], 'finished in', player[1], 'secs')

    def displayCountry(self) : 
        countryList = []
        for key in country.keys() : 
            dummy = [key, country[key]]
            countryList.append(dummy)
        
        df = pd.DataFrame(countryList, columns = ['country', 'total medal'])

        df.sort_values(by = ['total medal'], inplace = True)

        print(df) 

# child class 1
class Paralympic(Olympic) : 

    # constructor 
    def __init__(self, name, age, country, sports,time) : 
        super().__init__(name, age, country)
        self.category = 'paralympic'
        self.sports = sports 
        self.time = time 

    # adding the player to sports data structure 
    def addSports(self) :

        if self.sports == 'sprint' : 
            sprint['paralympic'].append(self.createDummy())
        elif self.sports == 'swim' : 
            swim['paralympic'].append(self.createDummy())

    def paraSortedList(self, sport) : 
        if sport == 'sprint' : 
            sortedList = sorted(sprint['paralympic'], key = lambda x: (x[1]))
        elif sport == 'swim' : 
            sortedList = sorted(swim['paralympic'], key = lambda x: (x[1])) 
        
        return sortedList 

    # sorting the list wrt individual time and find out the best performer
    def bestInPara(self, sport) :  
        return self.paraSortedList(sport)[0]

    # find the top performers and give medals 
    def medalsIn(self, sport) :

        print('Gold medal goes to',self.paraSortedList(sport)[0][0])
        print('Silver medal goes to',self.paraSortedList(sport)[1][0])
        print('Bronze medal goes to',self.paraSortedList(sport)[2][0])

        for i in range(3) : 
            if self.paraSortedList(sport)[i][2] not in country.keys() : 
                country[self.paraSortedList(sport)[i][2]] = 1 
            else : 
                country[self.paraSortedList(sport)[i][2]] += 1

# child class 2
class SummerOlympic(Olympic) : 

    # constructor 
    def __init__(self, name, age, country, sports, time) : 
        super().__init__(name, age, country)
        self.category = 'summer'
        self.sports = sports 
        self.time = time

    # adding the player to sports data structure
    def addSports(self) :

        if self.sports == 'sprint' : 
            sprint['summer'].append(self.createDummy())
        elif self.sports == 'swim' : 
            swim['summer'].append(self.createDummy())

    def summerSortedList(self, sport) : 
        if sport == 'sprint' : 
            sortedList = sorted(sprint['summer'], key = lambda x: (x[1]))
        elif sport == 'swim' : 
            sortedList = sorted(swim['summer'], key = lambda x: (x[1])) 
        
        return sortedList 

    # sorting the list wrt individual time and find out the best performer
    def bestInSummer(self, sport) :  
        return self.summerSortedList(sport)[0]

    # find the top performers and give medals 
    def medalsIn(self, sport) :

        print('Gold medal goes to',self.summerSortedList(sport)[0][0])
        print('Silver medal goes to',self.summerSortedList(sport)[1][0])
        print('Bronze medal goes to',self.summerSortedList(sport)[2][0])

        for i in range(3) : 
            if self.summerSortedList(sport)[i][2] not in country.keys() : 
                country[self.summerSortedList(sport)[i][2]] = 1 
            else : 
                country[self.summerSortedList(sport)[i][2]] += 1

# child class 3
class WinterOlympic(Olympic) : 

    # constructor 
    def __init__(self, name, age, country, sports, time) : 
        super().__init__(name, age, country)
        self.category = 'winter'
        self.sports = sports 
        self.time = time

    # adding the player to sports data structure
    def addSports(self) :

        if self.sports == 'sprint' : 
            sprint['winter'].append(self.createDummy())
        elif self.sports == 'swim' : 
            swim['winter'].append(self.createDummy())
            
            
    def winterSortedList(self, sport) : 
        
        if sport == 'sprint' : 
            sortedList = sorted(sprint['winter'], key = lambda x: (x[1]))
        elif sport == 'swim' : 
            sortedList = sorted(swim['winter'], key = lambda x: (x[1])) 

        return sortedList 

    # sorting the list wrt individual time and find out the best performer
    def bestInWinter(self, sport) :  
        return self.winterSortedList(sport)[0]

    # find the top performers and give medals 
    def medalsIn(self, sport) :

        print('Gold medal goes to',self.winterSortedList(sport)[0][0])
        print('Silver medal goes to',self.winterSortedList(sport)[1][0])
        print('Bronze medal goes to',self.winterSortedList(sport)[2][0])

        for i in range(3) : 
            if self.winterSortedList(sport)[i][2] not in country.keys() : 
                country[self.winterSortedList(sport)[i][2]] = 1 
            else : 
                country[self.winterSortedList(sport)[i][2]] += 1

# Multiple Inheritance class:
class WorldRecord(Paralympic, WinterOlympic, SummerOlympic): 

    sprint_record = 9.58
    swim_record = 46.91
    # constructor 
    def __init__(self, sport, name= None, age= None, country= None, time = None) : 
        self.sport = sport 

    # def show1(self) : 
    #     print(self.bestInSummer('sprint'))

    # finding the champ 
    def checkChamp(self, sport) : 
        ans = [self.bestInPara(sport), self.bestInSummer(sport), self.bestInWinter(sport)]
        sortedList = sorted(ans, key = lambda x: (x[1]))
        
        if sortedList[0][1] < self.sprint_record : 
            print('New world champion in',self.sport,'is',sortedList[0][0],'from',sortedList[0][2],'with timing',sortedList[0][1], 'secs')
        else :
            print('Champion of this year in',self.sport,'is',sortedList[0][0],'from',sortedList[0][2],'with timing',sortedList[0][1], 'secs')

if __name__ == "__main__" : 
    print('----------------Paralympic---------------------')
    print()
    p1 = Paralympic('name1', 12, 'India', 'sprint', 9)
    p1.addSports()
    p2 = Paralympic('name2', 13, 'China', 'sprint', 10)
    p2.addSports()
    p3 = Paralympic('name3', 14, 'India', 'sprint', 11)
    p3.addSports()
    p4 = Paralympic('name4', 15, 'China', 'sprint', 8)
    p4.addSports()
    p4.medalsIn('sprint')
    print()
    print('----------------Summer Olympic---------------------')
    print()
    s1 = SummerOlympic('name5', 12, 'England', 'sprint', 21)
    s1.addSports()
    s2 = SummerOlympic('name6', 13, 'China', 'sprint', 19)
    s2.addSports()
    s3 = SummerOlympic('name7', 14, 'USA', 'sprint', 20)
    s3.addSports()
    s4 = SummerOlympic('name8', 15, 'England', 'sprint', 22)
    s4.addSports()
    s4.medalsIn('sprint')
    print()
    print('----------------Winter Olympic---------------------')
    print()
    w1 = WinterOlympic('name9', 12, 'USA', 'sprint', 7)
    w1.addSports()
    w2 = WinterOlympic('name10', 13, 'England', 'sprint', 6)
    w2.addSports()
    w3 = WinterOlympic('name11', 14, 'France', 'sprint', 5)
    w3.addSports()
    w4 = WinterOlympic('name12', 15, 'France', 'sprint', 10)
    w4.addSports()
    # print( w4.sortedList('sprint'))
    w4.medalsIn('sprint')
    print()
    print('--------------country---------------------------')
    print()
    w4.displayCountry()
    print()
    print('--------------table-----------------------------')
    print()
    w4.displayTable('sprint')
    print()
    print('--------------World Record-----------------------------')
    print()
    w = WorldRecord('sprint')
    w.checkChamp('sprint')