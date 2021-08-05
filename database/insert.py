import sqlite3

#SCHEMA
# (ID INT PRIMARY KEY     NOT NULL,
#           NAME           TEXT    NOT NULL,
#           TEMP            INT     NOT NULL,
#           HUMIDITY        INT     NOT NULL,
#           SOIL_MOISTURE   INT     NOT NULL

def insert(n, t, h, s): 

    # need to validate data 
    print("data", n, t, h, s)
    # sqlite3 doesn't auto-increment id??
    id = 2 

    conn = sqlite3.connect('plants.db')
    print("Opened plants database successfully");

    #insert
    statement = f" INSERT INTO PLANTS VALUES ('{id}', '{n}', '{t}', '{h}', '{s}') "
    conn.execute(statement)

    conn.commit()
    print("Record created successfully")

    conn.close()



