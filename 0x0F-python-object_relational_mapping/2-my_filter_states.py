#!/usr/bin/python3
"""

Values in the 'states'table in [DB: hbtn_0e_0_usa]
where 'name' matches argument

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
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC".format(argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
