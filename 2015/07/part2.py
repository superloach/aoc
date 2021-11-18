import part1

if __name__ == '__main__':
	print(part1.run(
		[l for l in part1.inp if l[1] != 'b'],
		{'b': part1.run([*part1.inp], {})['a']},
	)['a'])
