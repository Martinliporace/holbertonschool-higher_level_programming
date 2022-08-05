#!/usr/bin/python3
"""Task: 0. Get all states"""

import MySQLdb
from sys import argv

if (__name__ == "__main__"):

    con = MySQLdb.Connect(host="localhost", user=argv[1],
                          passwd=argv[2], db=argv[3], port=3306)

    cur = con.cursor()
    qryOne = "SELECT cities.id, cities.name, states.name FROM cities"
    qryTwo = " INNER JOIN states ON cities.state_id = states.id"
    cur.execute(qryOne + qryTwo)
    query = cur.fetchall()

    for x in query:
        print(x)
    cur.close()
    con.close()
