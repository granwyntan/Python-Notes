############################################################################################################################################################
# © 2021 by Granwyn Tan
# Dictionaries
thisdict = {
    1 : True,
    2 : False,
    3 : True,
    4 : True,
    5 : False,
    6 : True
}
# Access Items

## Entire Dictionary
print(thisdict)

## Length of Dictionary
print(len(thisdict))

## Get All Keys
print(thisdict.keys())

## Get All Values
print(thisdict.values())

## Get Value by Key
### Method 1
print(thisdict.get(1))
### Method 2
print(thisdict[1])


# Changing Items

## Method 1
thisdict.update({1: False})

## Method 2
thisdict[1] = False


# Adding Items

## Method 1
thisdict[7] = True

## Method 2
thisdict.update({8: True})


# Removing Items

## Remove Last Item from Dictionary
print(thisdict.popitem())

## Remove Item by Key Name
### Method 1
print(thisdict.pop(1))
### Method 2
del thisdict[2]

## Delete Entire Dictionary
del thisdict
### print(thisdict) # This will cause an error because "thisdict" no longer exists.

## Empty/Clear Dictionary
thisdict.clear()

'''
We are Going to reinstate values in this case but the next step is redundant if the deletion/clearing functions do not get carried out
'''
thisdict = {
    1 : True,
    2 : False,
    3 : True,
    4 : True,
    5 : False,
    6 : True
}

# Loop Dictionaries

## Print all values in the dictionary, one by one
### Method 1
for x in thisdict:
    print(thisdict[x])
### Method 2
for x in thisdict.values():
    print(x)

## Print all keys in the dictionary
for x in thisdict.keys():
    print(x)

## Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
    print(x, y)


# Copy Dictionaries

## Method 1
mydict = thisdict.copy()

## Method 2
mydict = dict(thisdict)


# Nested Dictionaries

## Method 1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

## Method 2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# Dictionary Methods
'''
Method		Description
clear()		Removes all the elements from the dictionary
copy()	     	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()		Returns the value of the specified key
items()		Returns a list containing a tuple for each key value pair
keys()		Returns a list containing the dictionary's keys
pop()		Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()		Updates the dictionary with the specified key-value pairs
values()		Returns a list of all the values in the dictionary
'''
    
############################################################################################################################################################
