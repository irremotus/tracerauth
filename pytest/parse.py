import os

f = open('data')
f2 = open('data2', 'w')

lines = f.readlines()

i = 1
for line in lines:
	paths = line.replace('><', "\n").splitlines()
	if len(paths) > 1:
		f2.write(line + "\n")
		dirname = "subject" + str(i)
		i += 1
		os.makedirs(dirname)
		j = 1
		for path in paths:
			path = path.replace('<', ' ').replace('>', ' ')
			path = path.strip()
			if len(path) > 0:
				fo = open(dirname + "/" + str(j) + '.txt', 'w')
				fo.write(path + "\n")
				fo.close()
			j += 1
f2.close()
