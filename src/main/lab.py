"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = "TODO: Create a database connection"
cursor = "TODO: create a cursor with the connection"


# Created for you: A dogs table with autoincrementing ID
def create_dogs_table():

    # Create a table called "dogs"
    cursor.execute("CREATE TABLE IF NOT EXISTS dogs (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "name TEXT, "
                   "breed TEXT, "
                   "age INTEGER)")


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(id, name, breed, age):

    """TODO"""


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():

    # return the rows
    return """TODO"""
