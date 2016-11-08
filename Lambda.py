'''
Lambda - Expressions
'''

# written as a full function:

def square(num):
	print(num**2)

# A 1 line def function
def squares(num): print(num**2)

#square(2)
#squares(4)

# Using it as a lambda expression
sq = lambda num: print(num**2)
#sq(5)

# Test - Check if a number is even

isEven = lambda num: num%2 == 0

# reverse words using lambda
reverese = lambda rev: rev[::-1]

print(reverese("REDRUM"))