import part1

if __name__ == '__main__':
	locs = {}
	part1.walk(locs, part1.inp[::2])
	part1.walk(locs, part1.inp[1::2])
	print(len(locs))
