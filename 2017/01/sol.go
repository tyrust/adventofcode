// Advent of Code 2017
// Day 1 (http://adventofcode.com/2017/day/1)
// by Tyrus Tenneson
// 2017-12-03

package main

import (
	"bufio"
	"fmt"
	"os"
)

func partOne(s string) int {
	sum := 0
	for i := 0; i < len(s); i++ {
		m := int(s[i] - '0')
		n := int(s[(i+1)%len(s)] - '0')
		if m == n {
			sum += m
		}
	}
	return sum
}

func partTwo(s string) int {
	sum := 0
	for i := 0; i < len(s); i++ {
		m := int(s[i] - '0')
		n := int(s[(i+len(s)/2)%len(s)] - '0')
		if m == n {
			sum += m
		}
	}
	return sum
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		//fmt.Printf("%v", partOne(scanner.Text()))
		fmt.Printf("%v", partTwo(scanner.Text()))
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}
}
