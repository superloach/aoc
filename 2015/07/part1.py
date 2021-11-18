import sys

def split(line):
	l, target = line.split(' -> ')
	return l.split(' '), target

inp = [*map(split, sys.stdin.read().strip().split('\n'))]

ops = {
	'NOT': lambda x: ~x,
	'AND': lambda x, y: x & y,
	'OR': lambda x, y: x | y,
	'LSHIFT': lambda x, y: x << y,
	'RSHIFT': lambda x, y: x >> y,
}

def process(line, target, env):
	try:
		op = next(filter(line.__contains__, ops.keys()))
		line.remove(op)
		f = ops[op]
	except StopIteration:
		op = '!!!'
		f = lambda v: v

	nline = [[env.get, int][v.isdigit()](v) for v in line]
	if None not in nline:
		env[target] = (f(*nline) + (1<<16)) % (1<<16)
		return True

	return False

def run(inp, env):
	while inp:
		remove = []
		for index, (line, target) in enumerate(inp):
			if process([*line], target, env):
				remove.append(index)

		for r in sorted(remove)[::-1]:
			inp.pop(r)

	return env

if __name__ == '__main__':
	env = run(inp, {})
	print(env['a'])
