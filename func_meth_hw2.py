# function that calculates the volume of a sphere (radius)
# V = 3/4 3.14 x^3

def vol(rad):
	return(4/3*3.141*(rad**3))

#print(vol(9))

# Function that checks if a number is withing a given range

def ran_check(low,high,num):
	if num in range(low,high):
		return "true"
	else:
		return "false"

#print(ran_check(1,10,11))

# Function that returns how many upper and how many lower characters

sample_string = "Hello Mr. Rogers, how are you this fine Tuesday?"

def up_low(str):
	count = {"lower":0, "upper":0}
	for c in str:
		if c.isupper():
			count["upper"]+=1
		elif c.islower():
			count["lower"]+=1
		else:
			pass
	upper = count["upper"]
	lower = count["lower"]
	return "There are %s upper case letters \nThere were %s lower case letters"%(upper,lower)

#print(up_low(sample_string))

# Function that returns a list of only unique elements in an array
l1 = [1,2,3,4,4,4,2,3,6,5,5,6,4,2,4,6,3,2,1,34,32]

def unique_list(l):
	list=[]
	for item in l:
		if item in list:
			pass
		else:
			list.append(item)
	return list

#print(unique_list(l1))

# Write a function that multiplies numbers in a list
mul = [2,5,4,5,67,8,89,]

def multiply_list(l):
	result = 1
	for num in l:
		result= result * num
	return result

print(multiply_list(mul))














