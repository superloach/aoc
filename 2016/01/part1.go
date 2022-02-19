package main

import (
	"bytes"
	"io"
	"os"
	"strconv"
)

var input = func() [][]byte {
	bs, err := io.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}

	return bytes.Split(bytes.TrimSpace(bs), []byte(`, `))
}()

func main() {
	x, y := 0, 0
	dir := 0
	for _, step := range input {
		switch step[0] {
		case 'R':
			dir += 1
		case 'L':
			dir += 3
		}

		n, err := strconv.Atoi(string(step[1:]))
		if err != nil {
			panic(err)
		}

		dir %= 4

		dx := [...]int{
			0, 1, 0, -1,
		}[dir]
		dy := [...]int{
			1, 0, -1, 0,
		}[dir]

		x += dx * n
		y += dy * n
	}

	if x < 0 {
		x *= -1
	}
	if y < 0 {
		y *= -1
	}

	println(x+y)
}
