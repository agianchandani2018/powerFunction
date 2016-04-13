def to_power(base, exponent):

	"""This program asks the user for an exponent and base and returns the result"""

	if exponent > 0:
	 	return base * to_power(base, exponent -1)
	elif base == 0:
		return 0 
	elif exponent < 0:
		return("This program can't handle negative exponents")		

	else:
	 	return 1
	 	
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
	
	
	 	
def float_input(question):
	"""Offers try again"""	
	
	number = input(question)
	
	x = 1
	while x == 1:
		
		try:
			number = float(number)
			x = 0
		except ValueError:
			print("Sorry, that's not a number.")
			print("Try again")
			number = input(question)
	return number			


#--------------------------------------Main Program---------------------------------------
		
base = float_input("Enter a base: ")
exponent = float_input("Enter an exponent: ")

print("{} to the power of {} is {}".format(base, exponent, to_power(base, exponent)))



