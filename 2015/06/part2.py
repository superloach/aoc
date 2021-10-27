import part1

if __name__ == '__main__':
	cmds = {
		'on': lambda l: l + 1,
		'off': lambda l: max(0, l - 1),
		'toggle': lambda l: l + 2,
	}

	lights = part1.process(part1.inp, cmds)

	print(sum(lights))
