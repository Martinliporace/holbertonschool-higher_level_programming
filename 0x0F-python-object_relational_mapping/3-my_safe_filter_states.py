#!/usr/bin/python3
"""Task: 0. Get all states"""

import MySQLdb
from sys import argv

if (__name__ == "__main__"):

    con = MySQLdb.Connect(host="localhost", user=argv[1],
                          passwd=argv[2], db=argv[3], port=3306)

    input = argv[4]
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                [argv[4]])
    query = cur.fetchall()

    for x in query:
        print(x)
    cur.close()
    con.close()
