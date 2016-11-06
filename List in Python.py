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
print(sort_list)

#Printing a  reverse list- must use original variable
a = [1,2,3,4,5]
num = a.reverse()
#print(a)