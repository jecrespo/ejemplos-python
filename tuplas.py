# -*- coding: utf-8 -*-

tup1 = ()
tup1 = (50,)
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print (tup1[0])
print (tup1[3])
print (tup2[1:3])

tup1 = (12, 34.56,True)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)
print (tup3[0])

tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup
print ("After deleting tup : ")
#print (tup)