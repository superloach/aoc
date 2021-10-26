import sys

inp = sys.stdin.read()

dirs = {
	'<': [-1, 0],
	'>': [1, 0],
	'^': [0, 1],
	'v': [0, -1],
}

def walk(locs, inp):
	x, y = 0, 0

	l = len(inp)

	locs[x*l+y] = locs.get(x*l+y, 0) + 1

	for c in inp:
		if c not in dirs:
			continue

		dx, dy = dirs[c]
		x += dx
		y += dy

		locs[x*l+y] = locs.get(x*l+y, 0) + 1

if __name__ == '__main__':
	locs = {}
	walk(locs, inp)
	print(len(locs))
