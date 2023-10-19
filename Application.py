import re
from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen
import validators
import requests
from bs4 import BeautifulSoup
import time
import random

#Main Function, Defines and Loops the GUI
def main():
#Define window
    window = Tk()
    window.title("WikipediaMaps")
    window.geometry("600x600")

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
    output = Label(window, text="Welcome to WikipediaMaps! Enter the link you want to start at\nin the first box, and the destination in the second. The path will be given to you here!")
    output.grid(column=1, row=4)

    #Define capture input function. Captures Start and Destination Text. Will be called when pressing start! button.
    def captureInput():
        start = startTextInput.get()
        destination = destinationTextInput.get()
        if not validators.url(start) and not validators.url(destination):
            output.config(text="Enter a valid Start and Destination Link")
        elif not validators.url(start):
            output.config(text="Enter a valid Start Link")
        elif not validators.url(destination):
            output.config(text="Enter a valid Destination link")
        else:
            output.config(text="Searching...")
            time.sleep(2)
            output.config(text=findPath(start, destination))


    #Add the search button
    B = Button(text="Start!", command=captureInput)
    B.grid(column=1, row=3)

    #Loop the GUI
    window.mainloop()


#Takes the start and end websites and will find the path using BFS with the links on each page.
def findPath(start, end):
    queue = [start]
    previous = {}
    previous[start]: None
    while queue is not None:
        current_page = queue.pop(0)
        if current_page is end:
            return reconstructPath(previous, current_page)
        neighbors = getNeighbors(start)
        for n in neighbors:
                queue.append(n)
                previous[n] = current_page
    return "No path was found!"


#Function takes a dictionary of a path, and traces it all the way back to the start
def reconstructPath(previous, current_page):
    print("building path")
    path = []
    key = current_page
    while previous[key] is not None:
        path.append(previous[key])
        key = previous[key]
    return path


#Takes the start website link and returns a list of all the URLs on the page
def getNeighbors(start):
    neighbors = []
    filteredNeighbors = []
    request = requests.get(start)
    soup = BeautifulSoup(request.content, 'html.parser')
    neighbors = soup.find(id='bodyContent').select('a')
    for link in neighbors:
        if link.get('href') is not None:
            if link.get('href').startswith("/wiki/"):
                filteredNeighbors.append("https://en.wikipedia.org" + link.get('href'))
    print("searched site: " + start + "\nFound: " + ",".join(str(l) for l in filteredNeighbors))
    return filteredNeighbors


#invocation of main function
main()
