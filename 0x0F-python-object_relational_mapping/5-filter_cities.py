#!/usr/bin/python3
"""

Cities of a named state from [DB: hbtn_0e_0_usa]

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
    query = """
    SELECT cities.name FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (argv[4], ))
    cities = cursor.fetchall()
    print(', '.join([city[0] for city in cities]))
    cursor.close()
    db.close()
