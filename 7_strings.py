name = "Chetan"
print name			# Chetan
name = 'Chetan'
print name			# Chetan
name = "'Chetan'"
print name			# 'Chetan'
some_string = """this is in 
    a new
   line"""
print some_string		# Prints with spaces and new lines as it is

# String is like an array of characters
print name[2]			# h
print name[0:3]			# 'Ch

# Strings are immutable
# name[1] = "V"			# Throws error
# print name

# -------------------------------------------------------------------------------------
# Concatenate
# -------------------------------------------------------------------------------------
lastname = "Patige"
print name + lastname		# 'Chetan'Patige

# -------------------------------------------------------------------------------------
# Substring
# -------------------------------------------------------------------------------------
substring = "chet"
if substring in name:
    print "Present"		# Case sensitive

'''
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

# -------------------------------------------------------------------------------------
# Capitalize
	# Only the first letter is capitalized
# -------------------------------------------------------------------------------------

output = substring.capitalize()
print output			# Chet

# -------------------------------------------------------------------------------------
# Count
	# Number of times char is repeated, words too(chars form a word)
# -------------------------------------------------------------------------------------
new_string = "My name is Chetan"
output = new_string.count("a")
print output			# 2 

# -------------------------------------------------------------------------------------
# Endswith
# -------------------------------------------------------------------------------------
if new_string.endswith("name"):
    print "Works"		# Not working :)

# -------------------------------------------------------------------------------------
# Find
	# Position of the word from where it began
# -------------------------------------------------------------------------------------
output = new_string.find("name")
print output		# 3

# -------------------------------------------------------------------------------------
# Index
# -------------------------------------------------------------------------------------
print new_string.format()



























