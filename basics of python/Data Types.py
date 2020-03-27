# Python Numbers(int, float,complex)
a = 5
type(a)

a = 2.0
type(a)

a = 1+2j
type(a)

a = "Vinod"
type(a)
print(id(a))
a = 15
print(id(a))
type(a)
###############################   List   ################################

list1 = ['Python', 'Python', 2013, 2018,[1,2,3,4]]
list1[2]

list2 = [1, 2, 3, 4, 5 ]
print(id(list2))
list2[3] = 257
print(list2)
print(id(list2))

list3 = ["a", "b", "c", "d"]



python_class = ["Basics", "of", "Python"]


list1 = ['of', 'Basics', 2014, 2018]

print(list1[0])


list2 = [1, 2, 3, 4, 5, 6, 7 ]
list2[3] = "Python"
print(list2)

list1 =[ "VInod" ]
print(id(list1))

list2 = [1,2,3,4,5,6]
print(id(list1))

list3 = ['Python', 'Basics', 2013, 2018]
list1+ list2 +list3
print(id(list1))


print(list1[2])


list1[2] = 8055
print(list1)

list1[0] = "Basics"

list1 = ['Python', 'Basics', 2013, 2018]
print(list1)
del(list1)

print(list1)

# Append

aList = [123, 'xyz', 'zara', 'abc']
aList.append( 1234 )
print(aList)



#Pop

print (aList.pop())
print(aList)
aList
print (aList.pop(2))
aList

#Insert

aList.insert( 1, 2009)
print (aList)

aList.insert(2,"vinod")
print (aList)

#Extend

aList = [123, 'xyz', 'tommy', 'abc', 123]
bList = [2009, 'beneli']

aList.extend(bList)
print(aList)


#Reverse

aList.reverse()
print(aList)


#Sort


blist = [8,99,45,33]
blist.sort(reverse = False)
print(blist)

#count

aList = [123, 'xyz', 'zara', 'abc', 123, "zara"];
print(aList.count("zara"))


##################################### Tuples ####################################


## Create a tuple dataset
tup1 = ('Street triple','Detona','Beneli', 8055)
tup2 = (1, 2, 3, 4, 5 )
tup3 = ("a", "b", "c", "d")

### Create a empty tuple
tup1 = ()
#Create a single tuple
tup1 = (50,)
#Accessing Values in Tuples
tup1 = ('Street triple','Detona','Beneli', 8055)
print(tup1[0])

tup2 = (1, 2, 3, 4, 5, 6, 7 )
tup2[2] = 14
print(tup2[1:5])

#Updating Tuples
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# So,create a new tuple as follows
tup1 = tup1 + tup2
print(tup1)

#Delete Tuple Elements
tup = ('Street triple','Detona','Beneli', 8055)
print (tup)
del(tup)
print(tup)
print ("After deleting tup : ")
print(tup)

#Basic Tuples Operations

#To know length of the tuple
tup = (1,2,3,'Basics','Python')
len(tup)


#To add two elements
tup2 =(4,5,6)

tup3 = tup+tup2
tup3*3

tup4 = ('Hi!',)
tup4*3





# Max and min in tuple
tuple1 = (456, 700, 200)
print(max(tuple1))

print(min(tuple1))



############################## Dictionary #################################


#Accessing Values in Dictionary
dict1 = {'Name': 'Vinod', 'Age': 25, 'bike': 'Apache'}
print(dict1)
print(dict1['Name'])
print(dict1['Age'])
print(dict1['bike'])


##Updating Dictionary
dict1 = {'Name': 'Vinod', 'Age': 25, 'bike': 'Beneli'}
dict1['Age'] = 8; # update existing entry

print(dict1)
dict1['Name'] = "Sri Vinod" # Add new entry
dict1['bike'] = "Honda"
dict1["Area"] = "Bangalore"

dict1
print(dict1['Age'])
print(dict1['Bike'])


#Delete Dictionary Elements
dict1 = {'Name': 'Vinod', 'Age': 25, 'bike': 'Apache'}
del(dict1['Name']); # remove entry with key 'Name'
dict1
dict1.clear()    # remove all entries in dict
del(dict1)        # delete entire dictionary

############################## Dictionary #################################



