# Sets can be of different data types

myset = ()			# Initialization
myset = {1,2,3,"Chetan"}
print myset			# set([1, 2, 3])
myset = set([1,2,3,4,5])
print myset 			# set([1,2,3,4,5])
# mynewset = set(1,2,3)		# Not Possible


'''
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''

# -------------------------------------------------------------------------------------
# Add
	# Adds a single entity
	# use set.update() to add another set to it
		# Does union of two sets and combines them
# -------------------------------------------------------------------------------------
myset = {1,2,3,4,5,6}
myset.add(7)
# output = myset.add(7)		# Not possible
print myset			# set([1,2,3,4,5,6,7])

# -------------------------------------------------------------------------------------
# Clear
	# Clears the whole set
# -------------------------------------------------------------------------------------
myset.clear()
print myset			# set([])

# -------------------------------------------------------------------------------------
# Copy
# -------------------------------------------------------------------------------------
mynewset = {1,2,3}
output =  mynewset.copy()
print output			# set([1,2,3])

# -------------------------------------------------------------------------------------
# Difference
	# First set - Second set
# -------------------------------------------------------------------------------------
a = {1,2,3,4,5}
b = {1,2,3}
print a.difference(b)
# print output			# set([4,5]) # a - b

# -------------------------------------------------------------------------------------
# discard
	# Delete an entity
	# Raises a key error if not present
		# set.remove() does not raise an error
# -------------------------------------------------------------------------------------
a.discard(5)
print a				# set([1,2,3,4])


































