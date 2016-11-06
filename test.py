#!/usr/bin/env phython

'''
created by Jared Rentz. He is awesome!

def main():
	print ("Get the Money")


if __name__ == '__main__':
	main()


'''
# Performing Powers
#print(2**3)

# Perform Sq Rt. using 0.5
#print(8**.5)

my_income = 32435
my_tax_rate = .075

my_taxes = my_income * my_tax_rate

x = "MONEY"

print("My taxes are: %1.3f"  %(my_taxes))

# Print Formating multiple methods

print("Welcome to {x} house where we {y} freely with income of %1.3f".format(x="Jared's", y="live") %my_taxes)