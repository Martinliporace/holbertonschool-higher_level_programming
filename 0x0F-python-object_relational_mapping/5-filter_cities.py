#!/usr/bin/python3
"""Task: 0. Get all states"""

import MySQLdb
from sys import argv

if (__name__ == "__main__"):

    con = MySQLdb.Connect(host="localhost", user=argv[1],
                          passwd=argv[2], db=argv[3], port=3306)

    cur = con.cursor()

    qryOne = "SELECT cities.name FROM cities INNER JOIN "
    qryTwo = "states ON cities.state_id = states.id "
    qryThree = "WHERE states.name = %s ORDER BY cities.id"
    cur.execute(qryOne + qryTwo + qryThree, [argv[4]])
    query = cur.fetchall()

    output = []
    for x in query:
        output.append(str(x)[2:-3])
    print(', '.join(output))
    cur.close()
    con.close()
