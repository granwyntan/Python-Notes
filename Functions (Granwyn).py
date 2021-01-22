############################################################################################################################################################
# © 2021 by Granwyn Tan
# Functions

## Declaring
# Without Arguments:
def function1():
    pass

# With Arguments:
def function2(arg1, arg2):
    print(arg1+" "+arg2)

# With Arbitrary Arguments: 
# Don’t know how many arguments
def function3(*list_thingy):
    print("The first item in the list is not", list_thingy[1], "but", list_thingy[0])

# With Keyword Arguments:
# Order when calling does not matter
def function4(key1, key2, key3):
    print("The last key is", key3)

# With Arbitrary Keyword Arguments:
def function5(**list_thingy):
    print("My Last Name is", list_thingy["last_name"])

# Default Parameter Value:
def function6(country = "Singapore"):
    print("We are in", country)

# Lists as Arguments:
def function7(list_as_argument):
    print(list_as_argument)

# Return Values:
def function8(our_class):
    return our_class


## Calling
# Without Arguments:
function1()

# With Arguments:
function2("Granwyn", "Tan")

# With Arbitrary Arguments: 
function3("Granwyn", "Joe", "Ethan", "Abdullah")

# With Keyword Arguments:
function4(key1="Mr Seth Tan", key2="Mr Alvin Tan", key3="Mr Stanley Tan")

# With Arbitrary Keyword Arguments:
function5(first_name="Granwyn", last_name="Tan")

# Default Parameter Value:
function6(country = "USA")

# Lists as Arguments:
my_list = ["Granwyn", "Joe"]
function7(my_list)

# Return Values:
our_class_name = function8("S3-01")
print("Our Class: "+our_class_name)
################################################################################################################################
