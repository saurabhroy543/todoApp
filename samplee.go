package main

import "fmt"

func main() {
	avgWeight()
	/*fmt.Println("Enter your first name")
	var first string
	fmt.Scanln(&first)
	fmt.Println("Enter your second name")
	var second string
	fmt.Scanln(&second)
	fmt.Println("your full name is " + first + " " + second)*/

}
func check(n int) string {
	if n == 0 {
		fmt.Println("NOT in range num is zero")
	} else if n < 10 {
		fmt.Println("number is In range")
	} else {
		fmt.Println("not in range")
	}
	return "done"

}
func year() {
	fmt.Println("Enter your birth year")
	var date int
	fmt.Scanln(&date)
	fmt.Println("enter your age")
	var age int
	fmt.Scanln(&age)

	fmt.Println("year:=", age+date)
	return

}
func avgWeight() {
	sun := 0
	for i := 0; i < 5; i++ {
		fmt.Println("Enter the weight")
		var weight int
		fmt.Scanln(&weight)
		sun = sun + weight

	}
	avg := sun / 5
	fmt.Println("Avg weight is:=", avg)
	return
}
