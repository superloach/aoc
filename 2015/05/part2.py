import part1

groups = lambda s, n: (s[x:x+n] for x in range(len(s)-n+1))

haspairs = lambda s: any(s.count(p)>1 for p in groups(s, 2))
hastrio = lambda s: any(t==t[::-1] for t in groups(s, 3))

if __name__ == '__main__':
	print(sum(
		haspairs(s) * hastrio(s)
		for s in part1.inp
	))
