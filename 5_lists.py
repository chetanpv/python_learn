a = [1,2,3,4,5]
print a 		# [1,2,3,4,5]

dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append',
'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print a[2] 		# 3
print len(a)		# 5
print a[-2]		# 4

a[2] = 5
print a

# ------------------------------------------------------------------------------------
# Append : Adds the object at the end of the list
# ------------------------------------------------------------------------------------
a.append("Chetan")
print a 		# [1, 2, 5, 4, 5, 'Chetan']

# ------------------------------------------------------------------------------------
# Count : Says how many times the object is repeated in list
# ------------------------------------------------------------------------------------
a.append(3)
print a.count(3)	# 2 

# ------------------------------------------------------------------------------------
# Extend : Joins two lists. Adds at the end
	# Extending tuple      	-> everything in tuple is separated and added at the end
	# Extending dictionary 	-> only the keys are appended at the end as string
	# Extending set 	-> same as tuple, added at the end
	# Extending lists	-> same as tuple, added at the end
# ------------------------------------------------------------------------------------
b = [12, 44, 67]
a.extend(b)
print a			# [1, 2, 5, 4, 5, 'Chetan', 3, 12, 44, 67]

# ------------------------------------------------------------------------------------
# Index : Returns the first index match occurance of the object
# ------------------------------------------------------------------------------------
a.index(5)
print a			# 2

# ------------------------------------------------------------------------------------
# Insert : (Pos, object) : At given position, inserts given object
	# Position is mandatory
	# We can insert any object here.
		# Another list
		# Another dictionary
# ------------------------------------------------------------------------------------
a.insert(2,77)
print a			# [1, 2, 77, 5, 4, 5, 'Chetan', 3, 12, 44, 67]

# ------------------------------------------------------------------------------------
# Pop : Removes the element via index
	# By default last element
	# if index given, then that element
# ------------------------------------------------------------------------------------
a.pop(6)
print a			# [1, 2, 77, 5, 4, 5, 3, 12, 44, 67]

# ------------------------------------------------------------------------------------
# Remove : Removes element via value, first value from starting index
# ------------------------------------------------------------------------------------
a.remove(5)
print a			# [1, 2, 77, 4, 5, 3, 12, 44, 67]

# ------------------------------------------------------------------------------------
# Revserse : Reverses the list
# ------------------------------------------------------------------------------------
a.reverse()
print a			# [67, 44, 12, 3, 5, 4, 77, 2, 1]

# Sort : Sorts the list
# b = a.sort() # Cannot be done. b will be None
# print b			
a.sort()
print a			# [1, 2, 3, 4, 5, 12, 44, 67, 77]

a.sort(reverse=True)
print a			# [77, 67, 44, 12, 5, 4, 3, 2, 1]
# -------------------------------------------------------------------------
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)	# ('Sorted list:', [(4, 1), (2, 2), (1, 3), (3, 4)])
# -------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Copy:
# ------------------------------------------------------------------------------------
c = [1,2,3,4,5]
d = c
d.append(6)
print c		# [1, 2, 3, 4, 5, 6]
print d		# [1, 2, 3, 4, 5, 6]

import copy
c_new = [1,2,3]
d_new = copy.copy(c_new)
d_new.append(4)
print c_new

# ------------------------------------------------------------------------------------
# Clear : Clearing a list
del c_new[:] # [] # We can take slicing as a separate concept
# ------------------------------------------------------------------------------------


	

