# An empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Check my_list so far:
print(my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
#chek my_list again after insert:
print(my_list)

# Extend with another list
my_list.extend([50, 60, 70])
#check my_list after extend:
print(my_list)

# Remove the last element
my_list.pop()
#check my_list after remove:
print(my_list)

# Sort in ascending order
my_list.sort()
#Check my_list after sorting:
print(my_list)

# Find index of 30
index_30 = my_list.index(30)

print("Final list:", my_list)
print("Index of 30:", index_30)

my_list.pop(0)
print(my_list)