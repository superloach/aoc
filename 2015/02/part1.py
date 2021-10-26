import sys
import functools
import operator

inp = [
	[int(d) for d in line.split('x')]
	for line in
	sys.stdin.read().strip().split()
]

sm = lambda ss: sorted(ss)[:2]
sa = lambda ss: 2*ss[0]*ss[1] + 2*ss[1]*ss[2] + 2*ss[2]*ss[0]
mul = lambda xs: functools.reduce(operator.mul, xs, 1)

if __name__ == '__main__':
	print(sum([
		sa(p) + mul(sm(p))
		for p in inp
	]))
