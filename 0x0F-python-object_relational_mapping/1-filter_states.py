#!/usr/bin/python3
"""

States starting with 'N' from [DB: hbtn_0e_0_usa]

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
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        if state[1].startswith('N'):
            print(state)
    cursor.close()
    db.close()
