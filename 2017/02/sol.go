// Advent of Code 2017
// Day 2 (http://adventofcode.com/2017/day/2)
// by Tyrus Tenneson
// 2017-12-03

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func partOne(sheet [][]int) int {
	sum := 0
	for _, row := range sheet {
		min := row[0]
		max := min
		for _, val := range row {
			if val < min {
				min = val
			}
			if val > max {
				max = val
			}
		}
		sum += max - min
	}
	return sum
}

func partTwo(sheet [][]int) int {
	sum := 0
	for _, row := range sheet {
	ColLoop:
		for i, m := range row[:len(row)-1] {
			for _, n := range row[i+1:] {
				var s, t int
				if m > n {
					s = n
					t = m
				} else {
					s = m
					t = n
				}
				if t%s == 0 {
					sum += t / s
					break ColLoop
				}
			}
		}

	}
	return sum
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var sheet [][]int
	for scanner.Scan() {
		var row []int
		for _, f := range strings.Fields(scanner.Text()) {
			v, err := strconv.Atoi(f)
			if err != nil {
				fmt.Errorf("parsing int: %v", err)
			}
			row = append(row, v)
		}
		sheet = append(sheet, row)
	}
	//fmt.Printf("%v", partOne(sheet))
	fmt.Printf("%v", partTwo(sheet))
	if err := scanner.Err(); err != nil {
		fmt.Errorf("reading standard input: %v", err)
	}
}
