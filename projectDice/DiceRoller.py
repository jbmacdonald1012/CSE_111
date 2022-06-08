import csv
from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk,Image

def main():
    global root
    root = Tk()
    mainFrame = root

    root.title('Dice Roller')

    populateMainWindow(mainFrame)
    
    root.mainloop()


def populateMainWindow(mainFrame):

    def clear():
        rollDisplay.delete(0, END)

# This will build and populate the GUI

    rollDisplayLabel = Label(root, text='Dice Roll')    
    rollDisplay = Entry(root, borderwidth=5, width=35)
    d100Button = Button(root, text='D-100', width= 20, padx=5, pady=5, command=lambda: rollDice(100))
    d20Button = Button(root, text='D-20', width= 20, padx=5, pady=5, command=lambda: rollDice(20))
    d12Button = Button(root, text='D-12', width= 20, padx=5, pady=5, command=lambda: rollDice(12))
    d10Button = Button(root, text='D-10', width= 20, padx=5, pady=5, command=lambda: rollDice(10))
    d8Button = Button(root, text='D-8', width= 20, padx=5, pady=5, command=lambda: rollDice(8))
    d6Button = Button(root, text='D-6', width= 20, padx=5, pady=5, command=lambda: rollDice(6))
    d4Button = Button(root, text='D-4', width= 20, padx=5, pady=5, command=lambda: rollDice(4))
    d3Button = Button(root, text='D-3', width= 20, padx=5, pady=5, command=lambda: rollDice(3))
    clearButton = Button(root, text='Clear', width=20, command=clear)
    buttonQuit = Button(root, text='Exit program', width=20, command=root.quit)
    
    rollDisplayLabel.grid(row=0, column=0, columnspan=3, )
    rollDisplay.grid(row=1, column=0, columnspan=3)
    d100Button.grid(row=2, column=0, columnspan=2)
    d20Button.grid(row=2, column=3, columnspan=2)
    d12Button.grid(row=3, column=0, columnspan=2)
    d10Button.grid(row=3, column=3, columnspan=2)
    d8Button.grid(row=4, column=0, columnspan=2)
    d6Button.grid(row=4, column=3, columnspan=2)
    d4Button.grid(row=5, column=0, columnspan=2)
    d3Button.grid(row=5, column=3, columnspan=2)
    clearButton.grid(row=3, column=5, columnspan=2)
    buttonQuit.grid(row=5, column=5, columnspan=2)

    #Nested functions below are for the functionality of the program


    def rollDice(diceValue):
        total = 0
        space = ' '
        crit = ''

        total = random.randint(1, diceValue)

        if diceValue == 20:
            if total == 20:
                crit = 'NATURAL 20!'
                rollDisplay.insert(0, space + crit + space)

            if total == 1:
                crit == 'NATURAL 1 :('
                rollDisplay.insert(0, space + crit + space)

        rollDisplay.insert(0, str(total) + space)

if __name__ == '__main__':
    main()