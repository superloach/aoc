package main

import (
	"bytes"
	"fmt"
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
	locs := map[[2]int]struct{}{}

	x, y := 0, 0
	dir := 0
big:
	for _, step := range input {
		switch step[0] {
		case 'R':
			dir = (dir + 1) % 4
		case 'L':
			dir -= 1
		}

		fmt.Println(x, y, string(step))

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

		for i := 0; i < n; i++ {
			x += dx

			_, ok := locs[[2]int{x, y}]
			if ok {
				break big
			}

			locs[[2]int{x, y}] = struct{}{}
		}

		for i := 0; i < n; i++ {
			y += dy

			_, ok := locs[[2]int{x, y}]
			if ok {
				break big
			}

			locs[[2]int{x, y}] = struct{}{}
		}

		fmt.Println(x, y)
	}

	if x < 0 {
		x *= -1
	}
	if y < 0 {
		y *= -1
	}

	println(x+y)
}
