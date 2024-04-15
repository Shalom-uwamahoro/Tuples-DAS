my_tuple = (12, 25, 7, 43, 9, 18)

print(my_tuple[0:3]) 

print(my_tuple[-6:-2])

tuple_to_list = list(my_tuple)
print(tuple_to_list)

tuple_to_list.insert(3, 10)
tuple_to_list.remove(25)
print(tuple_to_list)

my_tuple = tuple(tuple_to_list)
print(my_tuple)

print(len(my_tuple))

new_items = (4,5,6)

final_tuple = my_tuple + new_items
print(final_tuple)
print(len(final_tuple))

del(my_tuple)
print(my_tuple)

