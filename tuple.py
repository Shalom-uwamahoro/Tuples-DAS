my_tuple = (12, 25, 7, 43, 9, 18)

print(my_tuple[0:3]) 

print(my_tuple[-6:-2])

my_tuple += (10,)
print(my_tuple)


remove_item = 25
my_tuple = tuple(item for item in my_tuple if item != remove_item )
print(my_tuple)

print(len(my_tuple))
