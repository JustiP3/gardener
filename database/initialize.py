import sqlite3


def init(): 
    conn = sqlite3.connect('plants.db')
    print("Opened plants database successfully");

    conn.close()
    #check if table exists   ** needs work ** 
    #try to select plant table
    #conn.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='plants' ''')

    #if conn.fetchone()[0]==1 : 
        #AttributeError: 'sqlite3.Connection' object has no attribute 'fetchone'
        #need to figure this out 
        #table exists
     #   print('Plants table already exists')
   # else :
        #table does not exist -> create table
    #    conn.execute('''CREATE TABLE PLANTS
    #    (ID INT PRIMARY KEY     NOT NULL,
     #   NAME           TEXT    NOT NULL,
     #   TEMP            INT     NOT NULL,
     #   HUMIDITY        INT     NOT NULL,
    #    SOIL_MOISTURE   INT     NOT NULL
     #   );''')
    #    print("Plants table created successfully");    

    
