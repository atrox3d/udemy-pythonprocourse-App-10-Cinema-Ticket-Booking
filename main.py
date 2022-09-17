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
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", 0, 90), ("A2", "1", "100"), ("A3", "0", "80")
    """)
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM "Seat"
    """)
    result = cursor.fetchall()
    connection.close()
    return result


def select_specific_columns():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM "Seat"
    """)
    result = cursor.fetchall()
    connection.close()
    return result


def select_with_condition():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM "Seat" WHERE "price" > 80
    """)
    result = cursor.fetchall()
    connection.close()
    return result


def update_value():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    UPDATE "Seat" SET "taken"=1 WHERE "seat_id"="A3"
    """)
    connection.commit()
    connection.close()


print(f'{"select_all":>25} | ', select_all())
print(f'{"select_specific_columns":>25} | ', select_specific_columns())
print(f'{"select_with_condition":>25} | ', select_with_condition())
