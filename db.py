'''
    Module for interaction with database
'''

import sqlite3
from enum import Enum

DB_NAME = 'categories.db'


class State(Enum):
    ok = True
    error = False


def get_db_connection():
    try:
        global connection
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
    except Exception:
        print("Error connection db {0}".format(DB_NAME))
        connection.close()
        return

    return cursor


def close_db_connection():
    try:
        connection.close()
    except Exception:
        print("Error closing connection")


def create_new_category(name_of_category):
    state = State.ok

    try:
        cursor = get_db_connection()
        query = "CREATE TABLE {0} (word varchar(15) primary key, weight real)".format(name_of_category)
        cursor.execute(query)
    except Exception:
        state = State.error
        print("Error with creating new category")
    finally:
        close_db_connection()

    return state


def get_category_data(name_of_category):
    state = State.ok
    data = list()

    try:
        cursor = get_db_connection()
        query = "SELECT * from {0} ORDER BY weight DESC".format(name_of_category)
        for row in cursor.execute(query):
            data.append(row)
    except Exception:
        state = State.error
        print("Error with getting data from {0} category".format(name_of_category))
    finally:
        close_db_connection()

    return state, data


def set_category_data(name_of_category, data):
    state = State.ok

    try:
        cursor = get_db_connection()
        query = "INSERT INTO {0} VALUES(?,?)".format(name_of_category)
        cursor.executemany(query, data)
    except Exception:
        state = State.error
        print("Error with setting data to database in {0} category".format(name_of_category))
    finally:
        close_db_connection()

    return state