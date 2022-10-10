def string_reverse(reverse_this: str) -> str:	
	return reverse_this[::-1]
	
string1 = "Cheeseburgers"
string2 = "dad"
string3 = "Coding is fun yo!"

print("The original string is " + string1)
print("The reverse string is " + string_reverse(string1))

print("The original string is " + string2)
print("The reverse string is " + string_reverse(string2))

print("The original string is " + string3)
print("The reverse string is " + string_reverse(string3))
