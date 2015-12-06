import os
from math import floor

f = open('data')
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
		dirname = "subject" + str(i)
		i += 1
		os.makedirs(dirname)
		folders.append((dirname,[]))
		j = 1
		for path in paths:
			path = path.replace('<', ' ').replace('>', ' ')
			path = path.strip()
			if len(path) > 0:
				points = path.split(';')
				if len(points) > maxlen:
					maxlen = len(points)
				folders[-1][1].append((str(j) + '.txt', points))
			j += 1
# f2.close()

# repeat data to pad to approximately maxlen
for fol in folders:
	for fil in fol[1]:
		l = len(fil[1])
		n = floor(maxlen/l)
		path = ""
		for p in points:
			path += (p + ';') * n
		fo = open(fol[0] + "/" + fil[0], 'w')
		fo.write(path + "\n")
		fo.close()
		print("Done with", fol[0] + "/" + fil[0], " : ", n*l, "/", maxlen)
