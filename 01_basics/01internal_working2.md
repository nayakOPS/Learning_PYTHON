Numbers and string are differently treated in python as compared to tuple,dictionary and list

reference count is there for each memory allocation (ref_count)

score = 10
a_score = score

so the 10 ref_count is 2

>>> import sys
>>> sys.getrefcount(24601)
3

>>> score = 10
>>> a_score = score
>>> sys.getrefcount(10)
4294967295  this big numbers shows due to compiler optimization loops working

always that same big number is get if any param pass to getrefcount

DATA TYPE is always stored in memory not in variable

Numbers and strings are not immediately collected by Automatic garbage collector(gc),
for later usage it is kept
>>> b = 3
>>> b= "nepads"
>>> b = 3.14

>>> c = 5
>>> d = 2
>>> c
5
>>> d
2
>>> c = c + 2
>>> c
7

new value of c is 7 and the c will be pointing to 7 and previous value 5 being a number it is not immediately collected

>>> mylistone = [1,2,3]
>>> mylisttwo = mylistone
above list references will be like
    mylistone ---> [1,2,3]
    mylisttwo ---> [1,2,3]

>>> mylistone = [1,2,3]
>>> mylisttwo = mylistone
>>> mylistone = ['newlist']
>>> mylisttwo
[1, 2, 3]

understand this too refer to concept of memory reference
>>> mylistone = [1,2,3] 
//from here the reference is being changed caused previous another value is associated with it
>>> mylistone
[1, 2, 3]
>>> mylistone[0] = 33
>>> mylistone
[33, 2, 3]
>>> mylisttwo
[1, 2, 3]

remember that list is mutable i have changed the value of mylistone 

due to list being mutable this property is seen
[1, 2, 3]
>>> l1 =  [1, 2, 3]
>>> l2 = l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0] = 55
>>> l1
[55, 2, 3]
>>> l2
[55, 2, 3]

cause here l1 and l2 are pointing the same refernece and the same reference index is changed

list is mutable , p1 and p2  have to different 
>>> p1 = [1, 2, 3]
>>> p2 = p1
>>> p2 = [1, 2, 3]
>>> p1[0] = 66
>>> p1
[66, 2, 3]
>>> p2
[1, 2, 3]
>>>

In list , slicing makes another copy of the list
so the below result is seen
>>> h1 = [1, 2, 3]
>>> h2 = h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0] = 44
>>> h1
[44, 2, 3]
>>> h2
[1, 2, 3]

'is' operator checks the memory reference if both operand has same mem reference