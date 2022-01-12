import sqlite3
import time
#create or open a database called c2Music.db
connection = sqlite3.connect('filmflix.db')
cursor = connection.cursor()