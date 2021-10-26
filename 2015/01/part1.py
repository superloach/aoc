import sys

inp = sys.stdin.read()

val = lambda c: ')('.index(c)*2-1

if __name__ == '__main__':
	print(sum([val(c) for c in inp]))
