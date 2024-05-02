my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

my_list.append(6)
print("List after adding element:", my_list)

my_list.remove(3)
print("List after removing element:", my_list)

my_list[2] = 10
print("List after modifying element:", my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)

my_dict['d'] = 4
print("Dictionary after adding element:", my_dict)

del my_dict['b']
print("Dictionary after removing element:", my_dict)

my_dict['a'] = 10
print("Dictionary after modifying element:", my_dict)

my_set = {1, 2, 3, 4, 5}
print("\nOriginal set:", my_set)

my_set.add(6)
print("Set after adding element:", my_set)

my_set.remove(3)
print("Set after removing element:", my_set)