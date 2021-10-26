import sys

inp = sys.stdin.read().strip().split()

vowels = lambda s: sum(1 for _ in filter('aeiou'.__contains__, s)) >= 3
double = lambda s: sum(s[x]==s[x+1] for x in range(len(s)-1)) > 0
badstr = lambda s: not ('ab' in s or 'cd' in s or 'xy' in s or 'pq' in s)

if __name__ == '__main__':
	print(sum(
		vowels(s) * double(s) * badstr(s)
		for s in inp
	))
