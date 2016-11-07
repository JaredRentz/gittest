'''
range - Function
range(start,stop[, step])-> list of integers
range(stop) -> list of integers
'''
start = 0
stop = 20

r =list(range(start,stop))
#result = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

even = list(range(start,stop,2))
#print(even)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

'''
List Comprehensions
'''
# a Traditional 4 loop:
l = []
for letter in "word":
	l.append(letter)

#print(l) = ['w', 'o', 'r', 'd']

# Now using List Comprehesion
lst = [apple for apple in "word"]
#print(lst) = ['w', 'o', 'r', 'd']

# Say we wanted to find the sq of numbers in a range 0 - 10
square = [square**2 for square in range(0,11)]
#print(square) = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Find the Even numbers in a range 0 - 10
enum = [x for x in range(0,11) if x%2 == 0]
#print(enum) = [0, 2, 4, 6, 8, 10]

my_list = [n*n for n in range(1,11)]
#print(my_list) [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
Celsius to Fahrenheit coversion
'''
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [(temp*(9/5)+32) for temp in celsius]

#print(fahrenheit) = [32.0, 50.0, 68.18, 94.1]

'''
Nested List Comprehesion
1. Take 1 - 10 and square it.
2. Take the square of that number and square it again!
'''

nes = [x**2 for x in[x**2 for x in range(11)]]
#print(nes) = [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

























