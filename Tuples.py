''' 
Similar to list but they can be immutable
'''
l = (1,2,3,4)
# Get the count of the tuples. Similar to a List!
#print(len(l))

# Grab the last number in the Tuple
#print(l[:-1])

# See how many times something appears in a Tuple

t = (1,2,4,3,2,2,1,2,3,2,1)

print(t.count(1))
num = 2

print(" 2 appears %s times in the Tuple"%(t.count(2)))
