from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen


def main():
#Define window
    window = Tk()
    window.title("WikipediaMaps")
    window.geometry("500x500")

    #Add photo to the top of window
    img = ImageTk.PhotoImage(Image.open("wikimaps.png").resize((100, 100)))
    titlePhoto = Label(window, image = img)
    titlePhoto.image = img
    titlePhoto.grid(column=1, row=0)

    #Add the Start Link text block
    startText = Label(window, text="Start Link: ")
    startText.grid(column=0, row=1)

    startTextInput = Entry(window, width=60)
    startTextInput.grid(column=1, row=1)

    #Add the Destination Link Block
    destinationText = Label(window, text="Destination Link: ")
    destinationText.grid(column=0, row=2)

    destinationTextInput = Entry(window, width=60)
    destinationTextInput.grid(column=1, row=2)

    #Add output window
    output = Label(window, text="Welcome to WikipediaMaps! Enter the link you want to start at in the first box, and the destination in the second. The path will be given to you here!")
    output.grid(column=1, row=4)

    #Define capture input function for the button
    def captureInput():
        start = startTextInput.get()
        destination = destinationTextInput.get()
        if urlopen(start).getcode() == 404 and urlopen(destination).getcode() == 404:
            output.config(text="Enter a valid Start and Destination Link")
        elif urlopen(start).getcode() == 404:
            output.config(text="Enter a valid Start Link")
        elif urlopen(destination).getcode() == 404:
            output.config(text="Enter a valid Destination link")
        else:
            output.config(text=findPath(start, destination))


    #Add the search button
    B = Button(text="Start!", command=captureInput)
    B.grid(column=1, row=3)
    window.mainloop()



def findPath(start, end):
    return "Connection not found!"


main()
