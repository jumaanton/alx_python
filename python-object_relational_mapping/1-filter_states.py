#!/usr/bin/env python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor
        cursor = db.cursor()

        # Filter the rows by name starting with N
        rows = cursor.filter(
            "SELECT * FROM states WHERE name LIKE 'N' ORDER BY id ASC")

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if db:
            db.close()


if __name__ == "__main__":
    main()
