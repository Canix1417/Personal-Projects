def fizz_buzz(num: int) -> str:
	if num % 3 == 0:
		if num % 5 == 0:
			return "FizzBuzz!"
		else:
			return "Fizz!"
	if num % 5 == 0:
		return "Buzz!"
		
	else:
		return "Eh..."

for i in range(1,101):
	print(str(i) + " should is a " + fizz_buzz(i))