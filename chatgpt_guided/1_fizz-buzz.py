"""
FizzBuzz-Print numbers 1 to 100, but:
	•	“Fizz” for multiples of 3
	•	“Buzz” for multiples of 5
	•	“FizzBuzz” for both
"""

for i in range(1, 101):
	to_print = i
	if i % 3 == 0:
		to_print = "fizz"
	if i % 5 == 0:
		to_print = "buzz"
	if i % 3 == 0 and i % 5 == 0:
		to_print = "fizzbuzz"
	
	print(to_print)


"""
As a comparison, I asked ChatGPT for fizzbuzz code. The result it gave is: 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

It reduces the code by 1 line, by not assigning a variable that gets changed, but prints based on the condition met using an "elif". 
"""

