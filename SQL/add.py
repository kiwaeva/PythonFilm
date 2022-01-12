from myConnection import *

def addFilm():
    tblFilms = []
    filmID = cursor.lastrowid
    print(filmID)
    title= input("Enter film title: ")
    yearReleased= input("Enter the year of release: ")
    rating= input("Enter film rating: ")
    duration= input("Enter duration of the film: ")
    genre= input ("Enter genre of the film: ")

    tblFilms.append(filmID)
    tblFilms.append(title)
    tblFilms.append(yearReleased)
    tblFilms.append(rating)
    tblFilms.append(duration)
    tblFilms.append(genre)

    try:
        cursor.execute('INSERT INTO tblFilms VALUES (?,?,?,?,?,?)',tblFilms)
        connection.commit()
        print("Film Added")

        time.sleep(3)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record not added, try again!")

# addFilm()