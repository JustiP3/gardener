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
    conn = sqlite3.connect('plants.db')
    print("Opened plants database successfully");

    #insert
    conn.execute("INSERT INTO PLANTS (ID, NAME, TEMP, HUMIDITY, SOIL_MOISTURE) \
        VALUES (1, 'BASIL', 70, 30, 50 )")

    conn.commit()
    print("Record created successfully")

    conn.close()


