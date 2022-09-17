"""
CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
)
"""

import sqlite3

connection = sqlite3.connect('cinema.db')
connection.execute("""
CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
)
""")
connection.commit()
connection.close()

