#!/usr/bin/python3
"""This module establishes a connection with
our database and prints the results of a query"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    cursor = db.cursor()
    db = MySQLdb.connect(host="localhost", user=username,
                         password=password, database=database, port=3306)
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
