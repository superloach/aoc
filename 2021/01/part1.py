import sys, itertools

inp = [*map(int, sys.stdin.read().strip().split('\n'))]

def inccount(i):
	return len([*
		filter(
			(0).__gt__,
			itertools.starmap(
				int.__sub__,
				itertools.pairwise(i),
			)
		)
	])

if __name__ == '__main__':
	print(inccount(inp))
