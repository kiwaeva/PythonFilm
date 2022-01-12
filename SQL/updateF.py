from myConnection import *

def updateFilm():
    keyField = input("Enter ID of the film to be updated: ")
    field = input ("Which field do you want to update:(title, yearReleased, rating, duration, genre)")
    newFieldVal = input("Enter the new value: ")
    print(newFieldVal)
    newFieldVal = "'" + newFieldVal + "'"
    print(newFieldVal)

    try:
        cursor.execute("UPDATE tblFilms SET " + field + "=" + newFieldVal + "WHERE filmID=" + keyField)
        connection.commit()
        print("Film updated!")

        time.sleep(2)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Film is not updated.")

# updateFilm()