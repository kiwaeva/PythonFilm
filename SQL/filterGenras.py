from myConnection import *

def filterRecords():
    cursor.execute('SELECT * FROM tblFilms ORDER BY title ASC ')
    