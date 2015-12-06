from tkinter import *
import json

root = Tk()
root.title("Simple Graph")
root.resizable(0,0)
points = []
c = Canvas(root, bg="white", width=600, height=600)
c.configure(cursor="crosshair")
c.pack()

def draw_point(p, color):
	c.create_oval(p[0], p[1], p[0]+1, p[1]+1, fill=color, outline=color)

#c.create_line(250, 250, 250, 750)
#c.create_line(250, 750, 750, 750)
#c.create_line(750, 750, 750, 250)
#c.create_line(750, 250, 250, 250)

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

for i in range(1, 7):
	f = open(str(i) + '.txt', 'r')
	line = f.readline()
	points = line.split(";")
	for point in points:
		point = point.strip()
		if len(point) < 1:
			continue
		ps = point.split(",")
		p = []
		for pi in ps:
			p.append(float(pi))
		draw_point(p, colors[i-1])
	print(colors[i-1])
	f.close()


root.mainloop()
