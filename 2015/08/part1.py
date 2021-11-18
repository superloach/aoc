import sys

inp = sys.stdin.read().strip().split('\n')

diff = lambda i: sum(len(l) - len(eval(l)) for l in i)

if __name__ == '__main__':
	print(diff(inp))
