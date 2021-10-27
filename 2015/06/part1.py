import sys

inp = sys.stdin.read().strip().split('\n')

coord = lambda s: [*map(int, s.split(','))]

width = 1000
height = 1000

def process(inp, cmds):
	lights = [0]*1000*1000

	for line in inp:
		words = line.split()
		if words[0] == 'turn':
			words = words[1:]

		cmd = words[0]
		start = coord(words[1])
		end = coord(words[3])

		for x in range(start[0], end[0]+1):
			for y in range(start[1], end[1]+1):
				c = x*width + y
				lights[c] = cmds[cmd](lights[c])

	return lights

if __name__ == '__main__':
	cmds = {
		'off': lambda l: 0,
		'on': lambda l: 1,
		'toggle': lambda l: 1 - l,
	}

	lights = process(inp, cmds)

	print(sum(lights))
