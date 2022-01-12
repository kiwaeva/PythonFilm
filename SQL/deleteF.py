from myConnection import *

def delFilm():
    KeyField = input("Enter ID of the film to be deleted: ")
    try:
        cursor.execute('DELETE FROM tblFilms WHERE filmID=' + KeyField)
        connection.commit()
        print("Film deleted!")

        time.sleep(2)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for film in row:
            print(film)
    except:
        print("Film not deleted")

# delFilm()