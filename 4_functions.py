# ----------------------------------------------------------------------------------------
# Function call without return value
# ----------------------------------------------------------------------------------------

def a(name):
    print "hello", name # hello Chetan # when you use , operator a default space is given
a("Chetan")

# ----------------------------------------------------------------------------------------
# Function call with return value
# ----------------------------------------------------------------------------------------
def b(number):
    return number + 1
print b(4)		# 5

print "="*20
# ----------------------------------------------------------------------------------------
# Scope of a variable
	# i cannot be changed inside a function
	# Parameter passed value can be changed. But within the scope and sent back
# ----------------------------------------------------------------------------------------
i = 4
def c(number):
    print "Inside c: i:", i
    # i += 1		# i cannot be changed. i here is referred as out of scope variable
    print "Inside c: number:", number
    number += 1
    print "Inside c: number:", number
    return number
output = c(i)
print "Output of the function", output
print "Outside c: i:", i

# Inside c: i: 4
# Inside c: number: 4
# Inside c: number: 5
# Output of the function 5
# Outside c: i: 4

print "="*20
# ----------------------------------------------------------------------------------------
# Function call with arguments
	# keyword args must always be at the end
	# Empty string OR 0 are also values. They will oeverride default parameter
# ----------------------------------------------------------------------------------------
def d(name, age, work="hp"):
    print name
    print age
    print work
d("Chetan","27","")	# Chetan 27 None
d("Chetan","27")	# Chetan 27 hp
d("Chetan","27","hpe")	# Chetan 27 hpe

print "="*20
# ----------------------------------------------------------------------------------------
# Arbitrary arguments
# ----------------------------------------------------------------------------------------
def e(*name):
    print name
d("Chetan", "Vivek", "Naveen")		# Chetan Vivek Naveen

def f(**generally_called_kwargs):
  print generally_called_kwargs

keywords = {'keyword1': 'foo', 'keyword2': 'bar'}
f(keyword1='foo', keyword2='bar')	# {'keyword2': 'bar', 'keyword1': 'foo'}
f(**keywords)				# {'keyword2': 'bar', 'keyword1': 'foo'}

print "="*20

def g(*name, **generally_called_kwargs):
    print name, generally_called_kwargs
    print type(name)				# <type 'tuple'>

keywords = {'keyword1': 'foo', 'keyword2': 'bar'}
g("Chetan",keyword1='foo', keyword2='bar')	# ('Chetan',) {'keyword2': 'bar', 'keyword1': 'foo'}
g("Chetan",**keywords)				# ('Chetan',) {'keyword2': 'bar', 'keyword1': 'foo'}

# ----------------------------------------------------------------------------------------
# Recursion
# ----------------------------------------------------------------------------------------
def fact(n):
    if n == 1:
	return 1
    else:
	return (n * fact(n-1))
output = fact(4)
print output			# 24

# ----------------------------------------------------------------------------------------
# Anonymous Function/Lamda function
# ----------------------------------------------------------------------------------------
double = lambda x: x * 2
print double(5) 		# 10

# ----------------------------------------------------------------------------------------
# Filter()
	# The function is called with all the items in the list and a new list is returned
	# which contains items for which the function evaluats to True.
# ----------------------------------------------------------------------------------------
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)			# [4, 6, 8, 12]














