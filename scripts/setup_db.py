import sqlite3

with open('../db/schema.sql') as db_setup:
    query = db_setup.read()

with sqlite3.connect('../db/recipes.db') as connection:
    cur = connection.cursor()
    cur.executescript(query)
    cur.close()