#!/usr/bin/python3
"""fetch states module"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password,
        db=db_name,
        charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == searched_name:
            print(row)
    cur.close()
    conn.close()
