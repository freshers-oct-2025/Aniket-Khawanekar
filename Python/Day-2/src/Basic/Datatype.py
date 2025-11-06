
print("=== Lists Demo ===")
my_list = [1, 2, 3, 4, 2]
new_list = ["anvs", 42, 3.14, True]

print("New list:", new_list)
print("Original list:", my_list)

# List methods
my_list.append(5)                   
print("After append:", my_list)

my_list.insert(1, 10)           
print("After insert:", my_list)

my_list.remove(2)               
print("After remove:", my_list)

popped = my_list.pop()          
print("Popped:", popped)
print("After pop:", my_list)

my_list.sort()                  
print("After sort:", my_list)


print("\n=== Tuples Demo ===")
my_tuple = (1, 2, 3, 2, 4)
print("Tuple:", my_tuple)
print("Count of 2:", my_tuple.count(2))
print("Index of 3:", my_tuple.index(3))


print("\n=== Sets Demo ===")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Set1:", set1)
print("Set2:", set2)

set1.add(5)                     
print("After add:", set1)

set1.remove(2)                  
print("After remove:", set1)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))


print("\n=== Dictionary Demo ===")
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
new_dict = dict(name='Alice', age=25, city='Los Angeles')
print("New dict:", new_dict)
print("Original dict:", my_dict)

my_dict['email'] = 'john@example.com'  
print("After adding email:", my_dict)

del my_dict['age']              
print("After deleting age:", my_dict)

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

print("Get value:", my_dict.get('name'))
print("Get with default:", my_dict.get('age', 'Not found'))

data=dict(zip(my_dict,new_dict))
data.update(my_dict)
print("Updated data:", data)
print("Length of dict:", len(my_dict))
data1=dict.fromkeys(['a','b','c'],1)
print("From keys:",data1)

data2=dict(zip(['x','y','z'],[9,8,7]))
print("Zipped dict:",data2)