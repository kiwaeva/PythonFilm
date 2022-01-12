from printAllF import *
from add  import *
from updateF import *
from deleteF import *

def menuOptions():
    options = 0
    while options not in ["1","2","3","4","5"]:
        print("\nMenu Options")
        print("1. Print Film details")
        print("2. Add a new film")
        print("3. Update film details")
        print("4. Delete film")
        print("5. Exit")
        options = input("\nEnter one of the options above: ")
        if options not in ["1","2","3","4","5"]:
            print("Option is not in the list")
        return options

mainProgram = True

while mainProgram == True:
    mainMenu = menuOptions()

    if mainMenu == "1" :
        showRecords()
    elif mainMenu == "2":
        addFilm()
    elif mainMenu == "3":
        updateFilm()
    elif mainMenu == "4":
        delFilm()
    else:
        mainProgram = False
    input("Press enter to exit")

    # menuOptions()





