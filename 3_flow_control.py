# ------------------------------------------------------------------------------------
# If Condition
# ------------------------------------------------------------------------------------

# string comparison here is case sensitive
# IF matches returns a boolean. Boolean decides the condition flow
a = "Chetan"
temp = []
if a == "chetan":
    print "It is not case sensitive"
elif a == "Chetan":
    print "It is case sensitive"
else:
    print "Its not me!"

# ------------------------------------------------------------------------------------
# Nested Ifs
# ------------------------------------------------------------------------------------
if "Che" in a:
    if "tan" in a:
	print a		# Chetan

# ------------------------------------------------------------------------------------
# For loop
# ------------------------------------------------------------------------------------
for i in a:
    temp.append(i)	# ['C', 'h', 'e', 't', 'a', 'n']
print temp

#for(i=0;i<5;i++):	# This cannot be done
#    print i

del temp[:]
for i in range(1,5):
    temp.append(i)	# [1, 2, 3, 4]
print temp

for i in range(len(a) - 5):
    print "Hello"

del temp[:]
for i in temp:
    print i
else:
    print "No items"

print "=" * 20
# ------------------------------------------------------------------------------------
# While loop
# ------------------------------------------------------------------------------------
sum = 0
i = 0
while i < 5:
    sum += i
    i+=1
print sum		# 10

while i==100:
    print i
else:
    print "i is not 100"

print "=" * 20
# ------------------------------------------------------------------------------------
# Break, Continue and Pass
# ------------------------------------------------------------------------------------

i = 0
while i < 10:
    i += 1
    if i == 2:
        continue	# Skip this condition
    elif i == 3:
	pass 		# Do nothing
    elif i == 6:
        break		# Exit Condition
    print i		# 1 3 4 5

print "=" * 20

i = 0
while i < 10:
    while i < 7:
        print "Innerloop:", i
	if i == 4:
	    break	# break exits only the inner condition
        i += 1
    print "Outerloop:", i
    i += 1
# Innerloop: 0
# Innerloop: 1
# Innerloop: 2
# Innerloop: 3
# Innerloop: 4
	# Outerloop: 4
# Innerloop: 5
# Innerloop: 6
	# Outerloop: 7
	# Outerloop: 8
	# Outerloop: 9

 
















