# if, elif, else Statements
'''
if case1:
	perform action 1
elif case2:
	perform action 2
else: 
	perform action 3
'''
x = [2,3,4,5,7,8]
y = 6
z = 3
'''
if x>y:
	print(x)
elif y>z:
	print(y)
else:
	print(z)
'''
# FOR LOOPS IN PYTHON

#for item in x:
	#print(item)

badge_numbers = [1,3,432,43242,432]
'''
for x in badge_numbers:
	if x % 3 == 0:
		print(x)
'''

list_sum = 0
'''
for num in badge_numbers:
	list_sum += num
print(list_sum)
'''

# Iterating through a Dictionary
d = {"k1":1, "k2":2, "k3":3}

#for k,v in d.items():
#	print(v)

'''
While Loops
'''
x = 0

while x <= 10:
	print("x is equal to: ",x)
	x += 1
	if x == 4:
		break
else:
	print("Done!")

