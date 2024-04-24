package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	var text string
	scanner.Scan()
	text = scanner.Text()
	println(len(text))
	scanner.Scan()
	n := parse(scanner.Text())

	prime := (1 << 19) - 1
	a := 26
	dict := make(map[string]int)
	println(n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		line := scanner.Text()
		var L, R int
		fmt.Sscanf(line, "%d %d", &L, &R)
		substring := text[L:R]
		hashVal := 0

		if dict[substring] == 0 {
			for _, ch := range substring {
				hashVal = (hashVal*a + int(ch)) % prime
			}
			dict[substring] = hashVal
		} else {
			hashVal = dict[substring]
		}

		fmt.Println(hashVal)

	}
}

func parse(s string) int {
	var n int
	fmt.Sscanf(s, "%d", &n)
	return n
}
