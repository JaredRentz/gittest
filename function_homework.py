def vol(rad):
	return 4/3 *3.14*rad**3

#print(vol(7))


def ran_check(num,low,high):
	if num in range(low,high):
		print("is in range")
	else:
		print("not in range")

			
ran_check(9,1,10)

def up_low(s):
	d = {"upper":0, "lower":0}
	for c in s:
		if c.isupper:
			d["upper"]+=1
		elif c.islower:
			d["lower"]+=1
		else:
			pass
	print(d["upper"])
	print(d["lower"])


up_low("Hello Mr. Roger, would you like to Come out and play?")