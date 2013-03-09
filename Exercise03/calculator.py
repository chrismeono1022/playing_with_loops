
from arithmetic import *	

while True:
	user_input = raw_input("Use the prefix calculator by entering an arithmetic operator and a sequence of 2 numbers: >> ")
	new_list = user_input.split(" ")
	a = new_list[0]
	try:
		b = int(new_list[1])
		c = int(new_list[2])
	except ValueError:
		print "I don't understand. Try again!"
	if new_list[0] == "+" or new_list[0] == "add":
		answer = add(b,c)
		print answer
	elif new_list[0] == "-" or new_list[0] == "subtract":
		answer = subtract(b,c)
		print answer
	elif new_list[0] == "*" or new_list[0] == "multiply":
		answer = multiply(b,c)
		print answer 
	elif new_list[0] == "/" or new_list[0] == "divide":
		answer = divide(b,c)  
		print answer 
	elif new_list[0] == new_list[0] == "square":
		answer = square(b)
		print answer 
	elif new_list[0] == new_list[0] == "cube":
		answer =cube(b)
		print answer 
	elif new_list[0] == "power" or new_list[0] == "^":
		answer = power(b,c)
		print answer 
	elif new_list[0] == "mod" or new_list[0] == "%":
		answer = mod(b,c)
		print answer 
	else:
		print "I don't understand."