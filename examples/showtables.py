import sqlite3


def connect(dbpath):
    connection = sqlite3.connect(dbpath)                                        # create connection
    cursor = connection.cursor()                                                # create cursor
    return connection, cursor                                                   # return both


def getcolumns(cursor):
    """
    print(
        'cursor.description',
        type(cursor.description).__name__,
        len(cursor.description),
        sep=' | '
    )                                                                           # cursor.description | tuple | 3
    print(f'cursor.description: {cursor.description}')                          # cursor.description: (('seat_id', None, None, None, None, None, None), ('taken', None, None, None, None, None, None), ('price', None, None, None, None, None, None))
    print(f'*cursor.description: ', *cursor.description)                        # *cursor.description: ('seat_id', None, None, None, None, None, None), ('taken', None, None, None, None, None, None), ('price', None, None, None, None, None, None)
    print(f'*cursor.description[0]: ', *cursor.description[0])                  # *cursor.description[0]: seat_id None None None None None None
    print('list(zip(*cursor.description)): ',
        list(
            zip(
                *cursor.description
            )
        )
    )                                                                           # list(zip(*cursor.description)):  [('seat_id', 'taken', 'price'), (None, None, None), (None, None, None), (None, None, None), (None, None, None), (None, None, None), (None, None, None)]
    print('list(zip(*cursor.description))[0]: ',
        list(
            zip(
                *cursor.description
            )
        )[0]
    )                                                                           # ('seat_id', 'taken', 'price')
    print(list(description[0] for description in cursor.description))           # ['seat_id', 'taken', 'price']
    print(tuple(description[0] for description in cursor.description))          # ('seat_id', 'taken', 'price')
    """
    columns = tuple(description[0] for description in cursor.description)       # aggregate in tuple
    # OR
    columns = list(zip(*cursor.description))[0]                                 # zip the unpacked tuples of cursor.description
                                                                                # get a list from iterator and get the first tuple
    return columns


def gettables(dbpath, *tables):
    results = {}                                                                # empty dict
    connection, cursor = connect(dbpath)                                        # get connection and cursor
    for table in tables:                                                        # iterate over table names
        cursor.execute(f'SELECT * FROM {table}')                                # execute select
        columns = getcolumns(cursor)                                            # save column names
        result = cursor.fetchall()                                              # save recordset
        results[table] = [columns, *result]                                     # create a new dict item with
                                                                                # table name as key and
                                                                                # a list with column names and unpacked results
    connection.close()
    return results


if __name__ == '__main__':

    results = gettables('../cinema.db', 'seat')
    for table, recordset in results.items():
        print(f'{table:<20}: {recordset}')                                      # print table and recordset
        print(list(zip(*recordset)))                                            # print columns and values

