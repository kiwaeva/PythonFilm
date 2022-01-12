from myConnection import *

def showRecords():
    cursor.execute('SELECT * FROM tblFilms')
    row=cursor.fetchall()
    for record in row:
        print (record)
# showRecords()