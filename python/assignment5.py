import sqlite3 as sq

class CricketDataBase :

    def __init__(self, identity) : 
        self.identity = identity

    def connectToDataBase(self) : 
        if self.identity == 'selector' or self.identity == 'chairperson' or self.identity == 'skipper' : 
            connection = sq.connect('SelectionBoard.db')
            cursor = connection.cursor()
            print('Connected to the database')
            connection.close()
            return True 
        else : 
            print('you are not allowed to access')
            return False 

    def createTable(self) : 
        if self.connectToDataBase() : 
            connection = sq.connect('SelectionBoard.db')
            cursor = connection.cursor()
            sql_command = """CREATE TABLE team 
                (player_id INTEGER PRIMARY KEY, 
                player_name VARCHAR(20) NOT NULL, 
                player_type VARCHAR(20), wickets INTEGER, 
                batting_avg INTEGER, score_against_pak INTEGER);"""

            cursor.execute(sql_command)
            print('table created')
            connection.close()

    def dropTable(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        cursor.execute('DROP TABLE team')
        print('table dropped')
        connection.close()

    def insert_value(self, player_id, player_name, player_type, wickets, batting_avg, score_against_pak) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()

        command = f"""INSERT INTO team VALUES ({player_id}, 
        "{player_name}", "{player_type}", {wickets}, 
        {batting_avg}, {score_against_pak});"""

        cursor.execute(command)
        connection.commit()
        # print(command)
        connection.close()

    def display_data(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM team')
        ans = cursor.fetchall()

        for i in ans : 
            print(i)
        connection.close()

    def update_values(self, column_name, value, primary_key) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = f"""UPDATE team SET {column_name} = "{value}" 
        WHERE player_id = {primary_key};"""
        
        cursor.execute(command)
        connection.close()

    def delete_data(self, primary_key) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        command = f"""DELETE FROM team WHERE player_id = {primary_key};"""
        cursor.execute(command)
        connection.close()

############################ filter with sql 
    def find_top_batsman(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = """SELECT player_name FROM team WHERE player_type = 'Batsman' ORDER BY batting_avg DESC LIMIT 3;"""
        
        cursor.execute(command)
        ans = cursor.fetchall()
        for i in ans : 
            print(i)
        connection.close()

    def find_top_fast_bowler(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = """SELECT player_name FROM team WHERE player_type = 'fast bowler' ORDER BY wickets DESC LIMIT 3;"""
        
        cursor.execute(command)
        ans = cursor.fetchall()
        for i in ans : 
            print(i)

        connection.close()

    def find_top_spinner(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = """SELECT player_name FROM team WHERE player_type = 'spinner' ORDER BY wickets DESC LIMIT 3;"""
        
        cursor.execute(command)
        ans = cursor.fetchall()
        for i in ans : 
            print(i)

        connection.close()

    def find_top_allrounder(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = """SELECT player_name FROM team WHERE player_type = 'Batsman' ORDER BY wickets DESC LIMIT 3;"""
        
        cursor.execute(command)
        ans = cursor.fetchall()
        for i in ans : 
            print(i)
            
        connection.close()

    def find_top_performer_against_pak(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = """SELECT player_name FROM team WHERE player_type = 'Batsman' ORDER BY score_against_pak DESC LIMIT 3;"""
        
        cursor.execute(command)
        ans = cursor.fetchall()
        for i in ans : 
            print(i)
            
        connection.close()

    def find_top_middle_order(self) : 
        connection = sq.connect('SelectionBoard.db')
        cursor = connection.cursor()
        
        command = """SELECT player_name FROM team WHERE player_type = 'middle' ORDER BY batting_avg DESC LIMIT 3;"""
        
        cursor.execute(command)
        ans = cursor.fetchall()
        for i in ans : 
            print(i)
            
        connection.close()

if __name__ == "__main__" : 
    identity = input('Enter your identity : ')
    db = CricketDataBase(identity)
    db.connectToDataBase()
    # db.dropTable()
    db.createTable()
    n = int(input('How many players you want to insert : '))
    for i in range(n) :
        id = int(input('Enter player_id : '))
        name = input('Enter name : ')
        player_type = input('Enter player_type : ')
        wickets = int(input('Enter number of wickets taken by the player : '))
        batting_avg = float(input('Enter batting_avg of the player : '))
        score_against_pak = int(input('Enter score_against_pak of the player : '))
    
        db.insert_value(id, name, player_type, wickets, batting_avg, score_against_pak)

    print('display table')
    db.display_data()
    print('top 3 batsman')
    db.find_top_batsman()
    print('top 3 fast bowlers')
    db.find_top_fast_bowler()
    print('top 3 spinners')
    db.find_top_spinner()
    print('top 3 all rounders')
    db.find_top_allrounder()
    print('top 3 performer against pakistan')
    db.find_top_performer_against_pak()
    print('top 3 middle order')
    db.find_top_middle_order()