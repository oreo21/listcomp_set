import string

a = [1,2,3] #sets must not contain duplicate elements
b = [2,3,4]
c = [1,3,5,8,11,'a','b','x','y']
d = [2,3,4,8,11,'a','c','x','z','t']

def union(a, b):
	return a + [
		x 
		for x in b 
		if not x in a
	]
	

def intersection(a, b):
	return [
		x
		for x in a
		if x in b
	]

def setDifference(a, b):
	return [
		x
		for x in a
		if x not in b
	]

def symmetricDifference(a, b):
	return setDifference(union(a, b), intersection(a, b))

def cartesianProduct(a, b):
	return [
		[x, y]
		for x in a
		for y in b
	]

print "union:\t" + str(union(a, b)) + "\n"
print "intersection:\t" + str(intersection(a, b)) + "\n"
print "setDifference:\t" +str(setDifference(a, b)) +"\n"
print "symmetricDifference:\t" + str(symmetricDifference(a, b)) +"\n"
print "cartesianProduct:\t" + str(cartesianProduct(a, b)) + "\n"
