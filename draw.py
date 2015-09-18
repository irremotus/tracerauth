from tkinter import *
import json

root = Tk()
root.title("Simple Graph")
root.resizable(0,0)
points = []
c = Canvas(root, bg="white", width=1000, height=1000)
c.configure(cursor="crosshair")
c.pack()

filebase = input("Enter file base name: ")
filecounter = 1

def point(event):
	c.create_oval(event.x, event.y, event.x+1, event.y+1, fill="black")
	points.append((event.x, event.y))

def release(event):
	global filebase
	global filecounter
	global points
	f = open(filebase + str(filecounter) + ".txt", "w")
	filecounter = filecounter + 1
	json.dump(points, f)
	f.close()
	points = []

c.bind("<B1-Motion>", point)
c.bind("<ButtonRelease-1>", release)

c.create_line(250, 250, 250, 750)
c.create_line(250, 750, 750, 750)
c.create_line(750, 750, 750, 250)
c.create_line(750, 250, 250, 250)

root.mainloop()
