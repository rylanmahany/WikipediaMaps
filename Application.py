from tkinter import *
from PIL import ImageTk, Image
#Define window
window = Tk()
window.title("WikipediaMaps")
window.geometry("500x500")

#Add photo to the top of window
img = ImageTk.PhotoImage(Image.open("wikimaps.png").resize((100, 100)))
titlePhoto = Label(window, image = img)
titlePhoto.image = img
titlePhoto.grid(column = 1, row = 0)

#Add the Start Link text block
startText = Label(window, text="Start Link: ")
startText.grid(column = 0, row = 1)

startTextInput = Entry(window, width = 60)
startTextInput.grid(column = 1, row = 1)

#Add the Destination Link Block
DestinationText = Label(window, text="Destination Link: ")
DestinationText.grid(column = 0, row = 2)

startTextInput = Entry(window, width = 60)
startTextInput.grid(column = 1, row = 2)

#Add the search button
B = Button(text = "Start!")
B.grid(column = 1, row = 3)

window.mainloop()