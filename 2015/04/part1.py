import itertools
import hashlib

inp = "yzbqklnj"

salt = lambda i, n: (str(i) + str(n)).encode('ascii')

find = lambda i, s: filter(
	lambda n: hashlib.md5(salt(i, n)).hexdigest().startswith(s),
	itertools.count(),
).__next__()

if __name__ == '__main__':
	print(find(inp, '0'*5))
