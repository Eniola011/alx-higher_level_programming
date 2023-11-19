#!/usr/bin/python3
"""

All Cities[DB: hbtn_0e_0_usa]

"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
    LEFT JOIN states ON cities.state_id = states.id ORDER BY \
    cities.id"
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
