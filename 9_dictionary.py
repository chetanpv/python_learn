a = {"name": "Chetan", "age": 27}
print a				# {"name": "Chetan", "age": 27}
b = dict({"name": "Vivek"})
print b				# {"name":"Vivek"}
b = dict([("name","Vivek"), ("age",27)])
print b				# {'age': 27, 'name': 'Vivek'}

# Accessable by key
print b['name']			# Vivek

# Update the value
	# dict.update() does the same
	# Updating key directly is 3 times faster
b["name"] = "Naveen"
print b				# {'age': 27, 'name': 'Naveen'}

# -------------------------------------------------------------------------------------
# Dictionary key cannot be updated(immutable)
	# They are stored in hash
# A key can only be an int or string. No iterable object like list or set
	# Value can be anything
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Removing items from dictionary
# -------------------------------------------------------------------------------------
# Pop
	# Removes one element reading the key
b.pop("name")
print b				# {'age': 27}

# clear
	# Clears all the elements
b.clear()
print b				# {}

'''
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
'''
# -------------------------------------------------------------------------------------
# Copy
# -------------------------------------------------------------------------------------
c = a.copy()
print c			# {'age': 27, 'name': 'Chetan'}

# -------------------------------------------------------------------------------------
# Fromkeys
		# Default value is set to None
# -------------------------------------------------------------------------------------
keys = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(keys,"vowel")
print(vowels)		# {'i': 'vowel', 'u': 'vowel', 'e': 'vowel', 'a': 'vowel', 'o': 'vowel'}

# -------------------------------------------------------------------------------------
# Get
	# Gets a value by passing the name
	# if no key then None
	# Can return default value if None using comma separator
# -------------------------------------------------------------------------------------
print c.get("name")			# Chetan
print c.get("lastname")			# None
print c.get("lastname", "Patige")	# Patige

# -------------------------------------------------------------------------------------
# Haskey
# -------------------------------------------------------------------------------------
if c.has_key("name"):
	print "Exists"			# Exists
# -------------------------------------------------------------------------------------
# Items
	# Converts to a list
# -------------------------------------------------------------------------------------
i = c.items()
print i					# List # [('age', 27), ('name', 'Chetan')]
print i[0][1]				# 27

# -------------------------------------------------------------------------------------
# Iteritems
# -------------------------------------------------------------------------------------
for x,y in c.iteritems():		# name Chetan
    print x,y				# age 27

for item in c.iteritems():		# This is not the ideal way to do
    print item				# (name, Chetan)
    print type(item)			# Tuple

# -------------------------------------------------------------------------------------
# Iterkeys
	# Same with itervalues()
# -------------------------------------------------------------------------------------
for item in c.iterkeys():
    print item				# age
    print type(item)			# string

# -------------------------------------------------------------------------------------
# Keys
	# Same with values()
# -------------------------------------------------------------------------------------
print c.keys()				# ['age', 'name']
print type(c.keys())			# List

# -------------------------------------------------------------------------------------
# Pop
	# Delete element via key
	# if element not there, raises error
	# default value can be given 
# -------------------------------------------------------------------------------------
c.pop("name")
print c					# {'age': 27}
print c.pop("name", "No keys")		# No keys

# -------------------------------------------------------------------------------------
# Setdefault
	# returns value if key found
	# else if sets the key with a default value or None
# -------------------------------------------------------------------------------------
output = c.setdefault("age")
print output				# 27
output = c.setdefault("phno", "123")
print output				# 123
print c					# {'phno': '123', 'age': 27}









































