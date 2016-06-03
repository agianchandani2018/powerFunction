import recursivePowerFunction

		
base = recursivePowerFunction.float_input("Enter a base: ")
exponent = recursivePowerFunction.int_input("Enter an exponent: ")

print("{} to the power of {} is {}".format(base, exponent, recursivePowerFunction.to_power(base, exponent)))