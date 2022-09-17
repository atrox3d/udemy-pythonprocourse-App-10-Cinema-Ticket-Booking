"""
CREATE TABLE "Seat" (
    "seat_id"   TEXT,
    "taken" INTEGER,
    "price"	REAL
)
"""

import sqlite3


def create_table():
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


def insert_record():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", "0", "90"), ("A2", "1", "100"), ("A3", "0", "80")
    """)
    connection.commit()
    connection.close()

insert_record()
