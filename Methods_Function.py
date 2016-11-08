'''
Methods are objects built into functions.
object.method(args)
'''
l = [1,2,3,4,5]

l.append(6)
l.count(3)

'''
Functions
def = functions
'''
def name_of_function(Greeting, Name):
	print(Greeting +" " + Name)

#name_of_function("Good-Bye", "Jared")

def addition(x,y):
	return(x + y)

x = addition(1,4)
#print(x)

def is_prime(num1):
	for n in range(2,num1):
		if num1 % n == 0:
			print("Not prime")
			break
	else:
		print("The number is prime")

is_prime(3)