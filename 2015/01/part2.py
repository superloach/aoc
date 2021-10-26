import part1

if __name__ == '__main__':
	s = 0
	for i, c in enumerate(part1.inp):
		if s < 0:
			print(i)
			break

		s += part1.val(c)
