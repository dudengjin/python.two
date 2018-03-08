
names = {'liuqian','du','li','huo'}
def show_magicians():
	for mag_names in names:
		print(mag_names)

show_magicians()

print("---------------------------------------")

names = {'liuqian','du','li','huo'}
mag_names = []
def make_great(names,mag_names):
	while names:
		mag = names.pop()
		mag = 'the great ' + mag
		mag_names.append(mag)	

def show_magicians(mag_names):
	for name in mag_names:
		print(name)

make_great(names,mag_names)
show_magicians(mag_names)

print("---------------------------------------")

names = {'liuqian','du','li','huo'}
mag_names = []
def make_great(names,mag_names):
	while names:
		mag = names.pop()
		mag = 'the great ' + mag
		mag_names.append(mag)	

def show_magicians(mag_names):
	for name in mag_names:
		print(name)

make_great(names,mag_names)
show_magicians(names)
show_magicians(mag_names)


