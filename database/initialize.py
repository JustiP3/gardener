import sqlite3


def init(): 
    conn = sqlite3.connect('plant.db')
    print("Opened plant database successfully");

    conn.execute('''CREATE TABLE PLANT
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            TEMP            INT     NOT NULL,
            HUMIDITY        INT     NOT NULL,
            SOIL_MOISTURE   INT     NOT NULL
            );''')
    print("Plant table created successfully");

    conn.close()

