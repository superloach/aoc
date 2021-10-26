import part1

if __name__ == '__main__':
	print(sum([
		sum(2*part1.sm(p)) + part1.mul(p)
		for p in part1.inp
	]))
