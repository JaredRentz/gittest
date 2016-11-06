'''
Working with List in Python: 
we do no use var in Python
'''
my_list = ["welcome", 23, 1.4]
her_list = ["Love", "Honor", "Passion"]
#print(my_list)

my_list = my_list + her_list
my_list.append("HERRRR")

my_list.pop(3)

#print(my_list)

sort_list = ["BJ's","Fresh Market","IOS","FEDEX","ABC"]

# Reveresing the order of the list. So last thing first!
sort_list.reverse()
#print(sort_list)

#Printing a  reverse list- must use original variable
a = [1,2,3,4,5]
num = a.reverse()
#print(a)

'''
Working with Dictionaries in Python
'''

# start an empty dictionary:
d = {}

# To add items in a dictionary
d["name"] = "Jared"

#print(d) =  Prints {'name': 'Jared'}

# Nested Dictionaries
demo = {'k1':{'nestkey':{'value': 30}}}
#print(demo["k1"]["nestkey"]["value"])

vip_List = {"people":{"name":["Jordan", "Peter"]}}

name = (vip_List["people"]["name"][1].upper())

# Dictionary methods
#print(vip_List.keys())

lala = {}

lala["k1"] = "value 1"
lala["k2"] = "value 2"
lala["k3"] = "value 3"

print(lala.values())
print(lala.keys())
print(lala.items())




















