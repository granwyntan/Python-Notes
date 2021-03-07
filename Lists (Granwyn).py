############################################################################################################################################################
# © 2021 by Granwyn Tan
# Lists

mylist = ["S3-01", "S3-01", "S3-03", "S3-04", "S3-05", "S3-06", "S3-07"]


### Removing Elements/Items from Array/List

## Remove an element from index/position
# mylist.pop(1)

## U can do a for loop
# for i in range(0, len(mylist)-1):
#     if mylist[i] == "S3-01":
#         mylist.pop(i)

## or the last method i love doing is
mylist[1] = "S3-02"


### Adding Elements/Items to Array/List
## Add to end of array
# mylist.append("S3-08")

## Insert at index/position
mylist.insert(7, "S3-08") # It won't error even if its above the index but u should ideally use the correct position


### Get element
## With Index
print(mylist[1]) # Gets second element
print(mylist[1:4]) # Gets second to fifth element

## With Name/Value for loop
for item in mylist:
    if i == "S3-01":
        print(i)

## After that u should print to check if its right b4 submitting code, etc.
print(mylist)

# String and List
# String
## Functions


# List
## Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2

## Repetition
mylist = [0] * 10
## or
anotherlist = list1 * 3

## Index [i]
a = ["hehe", "haha", "lmao", "hall", "classroom", "lab", "field", "library"]
i = 0
print(a[i])

## Slice [a:b]
print(a[1:5])

## Slice with steps [a:b:c]
address = "1 Technology Drive"
new_addr = address[2::2]

## Membership check (in)
text = "The red fox is quick"
print("brown" in text) # False

############################################################################################################################################################
