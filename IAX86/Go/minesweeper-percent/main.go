package main

import "fmt"

n := 36
b := 5
i := n - b
d := i / n
c := 0
e := 0
nc := 0
ic := 0

func main() {
	for c != i {
		c = c++
		nc = n - c
		ic = i - c
		e = ic / nc
		d = d * e
	}
	println(d)
}