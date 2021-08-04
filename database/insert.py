import sqlite3


def insert(i, n, t, h, s): 

    # need to validate data 

    conn = sqlite3.connect('plant.db')
    print("Opened plant database successfully");

    #insert

    conn.close()

