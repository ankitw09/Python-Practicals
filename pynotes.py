# List is ordered and changeable allows duplicate

# Tuple is ordered and unchangeable allows duplicate

# Set is unordered unchangeable and unindexed duplicate no allowed
# can remove and add items 

# Dictionary is ordered changeable but not duplicate



 

thislist.append("orange") # append at  last / also add list2 

thislist.insert(1, "orange")  # position , value insert at position

thislist.extend(list2) # second list added at last can add tuple set dict

thislist.remove("value") # remove the value

thislist.pop(1)  # remove the item at position 1

thislist.pop() # remove the last element

del thislist[0] # remove at index 

del thislist # remove the  list completely

thislist.clear()    # complete clear the list

for x in thislist # all element will come in x

#Loop through the index no 
for i in range(len(thislist))

thislist.sort()

thislist.sort(reversed=True) # sort in reverse order

thislist.reverse()

thislist.copy()

thislist.count("value")  # returns the no of elements  with specified value
# join 2 list by concatination 






# Tuple
# cant not add element after tuple is created
# tuple allow duplicates values

len(thistuple)
# one item tuple remember the comma

# access tuple by index thistuple[1]

# tuple can't be changed so convert to list then change element
 # and again convert to tuple

 x=("apple", "cherry")
 y=list(x)
 y[1]="kiwi"
 x=tuple(y)
 print(x)

 # append convert to list then again convert to tuple

thistuple = ()
y = ()
thistuple += y 
# y tuple will be added at the end of thistuple

# removing convert to list remove then again make it to tuple

del thistuple # del the thistuple completely

# unpacking in python (green , yellow , red)= thistuple
# if var are less then add * at last var rest values assign as list
# can add * at middle also 


# join to tuple through 
tuple3= tuple1 + tuple2

# want to multiply content of the tuple 
# multiply by 2
mytuple = tuple*2

thistuple.count(5) # this will count how much time 5 occur in tuple




# Exception handling in python

# try:
#     if error occured 

# except will execute

# if no error else will execute
# finally always execute


# raise valueerror ("this is error")

#  catching value error 
# except valueError as ve:
#     print (ve)

# we will get output as this is error 

# filter function filter out value less than 30 
# in func if x< 30 filter(func, list)

def func(x):
    if x<=30:
        return x
#using filter function which will filter out less than 30 value
y = filter(func, list2)

print(list(y))



def add(x, y):
    return x + y
from functools import reduce
#reduce function will do addition of all values
print(reduce(add, list2))


def fun2(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
#map function will map true or false accordingly
map_object = map(fun2, fruit)

print(list(map_object))

#reloading module using importlib module
importlib.reload(mymodule)

img = cv2.imread(r'C:\Users\DEVANSH SHARMA\cat.jpeg', 1)
cv2.imshow('image',img)  
pixel = img[100,100]  
print(pixel)  


height = img.shape[0]  
width = img.shape[1]  
channels = img.shape[2]  
size1 = img.size  

b,g,r = cv2.split(img)  
img = cv2.merge((b,g,r))  

# String

print("free" in txt)
print(b[2:5]) # called as slicing 5 not included

a="string"
a.upper()
a.lower()
a.strip # remove whitespaces
a.replace("h","j") # h ki jagah j aayega
a.split(",") # if it found , it will split the stirng
a+b # string concatination

# string format
a="My name is John, and my age {}"
print(a.format(39)) # printed as My name is John, and my age 39
# specify index in {} wo value print ho jayegi

# string methods
# use as string.casefold()
capitalize() # make first ch capital
casefold() # lower case coverts
center() # centered string return 
count()  # count the no of times specified value occur in list

encode() # returns an encoded version of the string




# Sets 

# sets are unordered unmutable and unindexed 

len(thisset)
print("banana" in thisset)
thisset.add("orange")

to add item from another set use update()
thisset.update(anotherset)  # we can also add any iterable like list

# remove item user remove or discard method
thisset.remove("banana") 
thisset.pop() # remove the last item 
thisset.clear() # emptyfires the set
del thisset # delete completely

# join the set use union
set3=set1.union(set2)
set1.update(set2)

set1.intersection_update(y) # only keep the duplicates
z=x.intersection(y)  # present in both add in z

x.symmetric_difference_update(y) # only keep not present in both
z=x.symmetric_difference(y) # only keep element not present in both in z
copy() # copy of set returns

# global keyword belongs to the global 


# Dictionary  

# we can add change and remove items in dict
# duplicates not allowed
len(thisdict)
thisdict["model"] # accessing dict items
also use get method # thisdict.get("model")
thisdict.keys() # list of keys in dict
thisdict.values() # returns values in dict
car["color"] = "red"  # add new item or change
thisdict.items() # returns each item as tuple in the list
thisdict.update({"year": 2020}) # also use for add new
thisdict.pop("model") # remove key 
thisdict.popitem() # remove the last inserted item
del thisdict["model"] # delete key model
del thisdict # completely delete
thisdict.clear() # clear the dict completely
thisdict.copy() # copies the dict = sign create only reference



# some other things

#`add *kids in parameter so dont need to specify _Parameters
# add **kids for args like dict means key value pair



# OOPs
# init will called every time object is created

del p1.age # delete object properties like this
delete p1 # dellete object like this 



# Inheristance:
class student(parentclass):
    pass

# new object created constructor function is called
# the child init function override the inheristance of the parent init func
# to keep call to parent init func parent.init(para)
# super().__init__(para)


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # start with end with search return true or false
# ^.*$,stringname