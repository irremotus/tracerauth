import os

f = open('data')

lines = f.readlines()

i = 1
for line in lines:
	paths = line.replace('><', "\n").splitlines()
	if len(paths) > 1:
		dirname = "subject" + str(i)
		i += 1
		os.makedirs(dirname)
		j = 1
		for path in paths:
			fo = open(dirname + "/" + str(j) + '.txt', 'w')
			j += 1
			path = path.replace('<', ' ').replace('>', ' ')
			path = path.strip()
			fo.write(path + "\n")
			fo.close()
