import part1

# copied and simplified from https://mail.python.org/pipermail/python-list/2003-April/236940.html
qrepr = lambda s: (
	'"%s"' % repr(
		s.replace('@', '@@').
		replace('"', '+@+').
		replace("'", '-@-')
	)[1:-1].
	replace('-@-', "'").
	replace('+@+', r'\"').
	replace('@@', '@')
)

diff2 = lambda i: sum(len(qrepr(l)) - len(l) for l in i)

if __name__ == '__main__':
	print(diff2(part1.inp))
