import sys
import os
from math import floor

inname = sys.argv[1]
f = open(inname)
# f2 = open('data2', 'w')

lines = f.readlines()

folders = [] # (foldername, [(filename, path)])

# collect the data
i = 1
maxlen = 0
for line in lines:
	paths = line.replace('><', "\n").splitlines()
	if len(paths) > 1:
		# f2.write(line + "\n")
		dirname = (inname.split("."))[0] + "subject" + str(i)
		i += 1
		os.makedirs(dirname)
		folders.append((dirname,[]))
		j = 1
		for path in paths:
			path = path.replace('<', ' ').replace('>', ' ')
			path = path.strip()
			if len(path) > 0:
				points = path.split(';')
				points = points[:-1]
				if len(points) > maxlen:
					maxlen = len(points)
				folders[-1][1].append((str(j) + '.txt', points))
			j += 1
# f2.close()

# repeat data to pad to approximately maxlen
for fol in folders:
	for fil in fol[1]:
		l = len(fil[1])
		n = int(floor((maxlen - l) / l))
		path = ""
		for p in fil[1]:
			path += (p + ';') * (n + 1)
		path = path[:-1]
		nl = len(path.split(";"))
		npad = maxlen - nl
		if npad < 0:
			npad = 0
		path += ";"
		path += "0,0,0;" * npad
		path = path[:-1]
		nnl = len(path.split(";"))
		path += ";"
		fo = open(fol[0] + "/" + fil[0], 'w')
		fo.write(path + "\n")
		fo.close()
		print("Done with", fol[0] + "/" + fil[0], " : ", nl, "/", maxlen, " npad:", npad, nnl)
