#Author: Ami
#Date: March 10


def int_input(question):
	"""Offers try again"""	
	
	number = input(question)
	
	x = 1
	while x == 1:
		
		try:
			number = int(number)
			x = 0
		except ValueError:
			print("Sorry, that's not a number.")
			print("Try again")
			number = input(question)
	return number	


#the function
def to_power(base, superScript):

	tally = 0 #will count how many times the base is multiplied by itself
	next = 1
	
		
#main part that multiplies the base by itself equal to the value of the exponent
	while tally < superScript:
		next = base * next
		tally += 1	
	
	return next


# --------------------------------- Main program below -----------------------------------	


#user inputs base and exponent
base = int_input("Enter a base: ")
superScript = int_input("Enter an exponent: ")



answer = to_power(base, superScript)

print("The answer is {}".format(answer))