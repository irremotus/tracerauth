from tkinter import *
import json
import numpy as np
import scipy as sp
import math
import sys

fname1 = sys.argv[1]
fname2 = sys.argv[2]

f1 = open(fname1, "r")
f2 = open(fname2, "r")

p1 = json.load(f1)
p2 = json.load(f2)

f1.close()
f2.close()

sides1 = []
sides2 = []

numSides = 4

def getSquareSide(p):
	"Left, Bottom, Right, Top: 0, 1, 2, 3"

	h = 1000
	w = 1000

	dLeft = abs(0 - p[0])
	dBottom = abs(h - p[1])
	dRight = abs(w - p[0])
	dTop = abs(0 - p[1])

	m = min(dTop, dBottom, dLeft, dRight)
	if m == dLeft:
		return 0
	elif m == dBottom:
		return 1
	elif m == dRight:
		return 2
	else:
		return 3

for i in range(numSides):
	sides1.append([])
	sides2.append([])

for p in p1:
	side = getSquareSide(p)
	sides1[side].append(p)

for p in p2:
	side = getSquareSide(p)
	sides2[side].append(p)


root = Tk()
root.title("Sides")
root.resizable(0,0)
points = []
c = Canvas(root, bg="white", width=1000, height=1000)
#c.configure(cursor="crosshair")
c.pack()

# draw square
c.create_line(250, 250, 250, 750)
c.create_line(250, 750, 750, 750)
c.create_line(750, 750, 750, 250)
c.create_line(750, 250, 250, 250)

colors = ["red", "green", "blue", "orange"]
for s in range(len(sides1)):
	side = sides1[s]
	for i in range(len(side)):
		c.create_oval(side[i][0], side[i][1], side[i][0]+1, side[i][1]+1, fill=colors[s], outline=colors[s])

colors = ["blue", "orange", "red", "green"]
for s in range(len(sides2)):
	side = sides2[s]
	for i in range(len(side)):
		c.create_oval(side[i][0], side[i][1], side[i][0]+1, side[i][1]+1, fill=colors[s], outline=colors[s])



# collect differences

def getNearestTwo(p, side, vertical):
	for i in range(len(side)-1):
		p1 = side[i]
		p2 = side[i+1]
		if vertical:
			cond = abs((p1[1] - p[1])) <= abs((p2[1] - p[1]))
		else:
			cond = abs((p1[0] - p[0])) <= abs((p2[0] - p[0]))

		if cond:
			return (i, i+1)
	if vertical:
		if p[1] < min(side[0][1], side[-1][1]):
			return (0, 0)
		elif p[1] > max(side[0][1], side[-1][1]):
			return (len(side), len(side))
	else:
		if p[0] < min(side[0][0], side[-1][0]):
			return (0, 0)
		elif p[0] > max(side[0][0], side[-1][0]):
			return (len(side), len(side))



nearest = []
nearest2 = []
spoints = []
for i in range(500):
	spoints.append((250, 250 + i))

for p in spoints:
	nearest.append(getNearestTwo(p, sides1[0], True))
	nearest2.append(getNearestTwo(p, sides2[0], True))

sd = []
sd2 = []
for i in range(numSides):
	sd.append([])
	sd2.append([])





for i in range(len(spoints)):
	p = spoints[i]
	if not nearest[i] is None:
		if (nearest[i][0] < len(sides1[0])) and (nearest[i][1] < len(sides1[0])):
			n1 = sides1[0][nearest[i][0]]
			n2 = sides1[0][nearest[i][1]]
			n = ((p[0]-n1[0], p[1]-n1[1]), (p[0]-n2[0], p[1]-n2[1]))
		else:
			n = ((0, 0), (0, 0))
	else:
		n = ((0, 0), (0, 0))
	sd[0].append(n)

	print("a" + str(nearest2[i]))
	if not nearest2[i] is None:
		if (nearest2[i][0] < len(sides2[0])) and (nearest2[i][1] < len(sides2[0])):
			n1 = sides2[0][nearest2[i][0]]
			n2 = sides2[0][nearest2[i][1]]
			n = ((p[0]-n1[0], p[1]-n1[1]), (p[0]-n2[0], p[1]-n2[1]))
		else:
			n = ((0, 0), (0, 0))
	else:
		n = ((0, 0), (0, 0))
	sd2[0].append(n)

td = 0
for i in range(len(spoints)):
	p = spoints[i]

	# first set of points
	n = sd[0][i]
	n1 = n[0]
	n2 = n[1]
	d = n1[0] + n2[0]
	d1 = d
	d = abs(d)
	c.create_oval(p[0]-40, p[1], p[0]-40-d, p[1], fill="red", outline="red")

	# second set of points
	n = sd2[0][i]
	n1 = n[0]
	n2 = n[1]
	d = n1[0] + n2[0]
	d2 = d
	d = abs(d)
	c.create_oval(p[0]-40, p[1], p[0]-40+d, p[1], fill="blue", outline="blue")

	# compare the two differences
	d = d2 - d1
	d = abs(d)
	c.create_oval(p[0]-60-d/2, p[1], p[0]-60+d/2, p[1], fill="yellow", outline="yellow")

	print(d)
	td = td + d

print(td)









root.mainloop()
