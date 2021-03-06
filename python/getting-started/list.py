# create list
a = ['a', 'b', 10, 1000]

# Sublists, Indexes of List
# Slice range notation generates shallow copy of list

simple_list = ['first', 'second', "third"]
print 'simple list: ' + str(simple_list)

# list index
print 'simple index: ' + simple_list[0] 

# negative index
print 'negative index: ' + simple_list[-1]

# sublist
print 'range 0:1 : ' + str(simple_list[0:1])

# sublist with negative
print 'range -2:-1 : ' + str(simple_list[-2: -1])

# default zero as first argument
print 'range :1 : ' + str(simple_list[:1])

# default max index value as a second argument
print 'range 1: : ' + str(simple_list[1:])

# default min and max:
print 'range : : ' + str(simple_list[:])

# list length
print 'length of the list: ' + str(simple_list) + ' is: ' + str(len(simple_list))

# substitution of elements in list
simple_list[0] = 'substitute'
print 'list after substitution: ' + str(simple_list)

# remove from list
simple_list[1:2] = []
print 'list with removed second element ' + str(simple_list)

# nested lists

# create nested list
nested_list = ['first', ['first_nested', 'second nested'], 'third']
print nested_list

# list as a stack (lifo)
stack = []
stack.append(1)
stack.append(2)
print stack.pop()
print stack.pop()

# filter function example
def even_num(x):
	return x % 2

print filter(even_num, range(1,10))
print filter(lambda x: x%2, range(1,10))

# range function example
def cube(x):
	return x*x*x

print map(cube, range(1,10))
print map(lambda x:x*x*x, range(1,10))

def sum_numbers(a,b):
	return a+b

# reduce function example
print reduce(sum_numbers, range(1,10))
print reduce(lambda a,b: a+b, range(1,10))

# remove item from list
list_with_item_to_remove = [1,2,3,4]
print str(list_with_item_to_remove)
del list_with_item_to_remove[0]
print str(list_with_item_to_remove)