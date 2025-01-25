"""
Question: How to store multiple pices of info with what we know?
"""
"""
Dictionaries fix this by assigning every element to "look-upable" address

"""
"""
Dictionaries are just lists but rather than having indicies 0,....,len(list) -1,
assign each individual value to a key that we can look up 
"""

my_Dict = {}
my_dict2 = dict()
# make a empty dictionary 

my_dict3 = {"key":1, "key2": 2, "key3": 3}

"""
All things in Dictionaries follow the template of {key: value,}

"""

"""
How to access things from Dictionaries
"""
print(my_dict3["key"])
print(my_dict3[key2])

"""
What can be a key? Values can be anything dosent really matter what you store in a vlue 
but keys have to be immutable  

cannot changed: strings, ints, floats 
"""


num = 1
num2 = 3
sum = 0
print(sum)
sum = num + num2 
print(sum)

"""
in this example sum was immutable because to change the value you had to do a variable assignment to change 

non immutable: lists, 

"""

def changelist():
    mylist = [1,2,3]
    print(mylist)
    mylist.append(4)
    print(mylist)

"""
    lists are mutable we didnt have to do another var resignment to add 4 to our list 

    why do keys need to be immutable
    keys for dicts have to immutable if they wernt your values would move around in mem everytime you updated the key

"""
def key_test():
    my_dict4 = {"af": 313, 14:"hello", 3.14: "pi"}

    print(my_dict4["af"])
    print(my_dict4[3.14])

"""
how to solve the searching porblem 
"""

def searchdict():
    my_dict4()
    if "af" in my dict4:
        print("This is in the dict ")
    else:
        print("that is not in the dict ")

searchdict()

"""
the in keyword searches for keys and not values. anything can be a vlaue inclidng lists 
"""

users = {"hello":["password",12,"hello@hello.com"], "word":["iloveschool",9,"word@world.com"]}
print("password", "gradelevel", "email")
print(users["hello"])

print("password is" + users["hello"][0])

"""
dict that comprising of keys (usernames) and values (account info)
values were lists of objects
acces obj in a list at a certain way 

    loops over dicts 
    for-each or for-i (index) loops 

    dicts work the same way but we weant to make the disction that for-each iterates over keys 
"""

def looptest(dict):
    for key in dict:
        print(key)
        print(dict[x])

looptest(my_dict3)



"""
for each loops iterate over keys, get the values make sure you square brackets operator 
the current key your looking at 

how do we add stuff to dicts. Conventional widsom is  .append() 

var assignment with []

ex. my_Dict[newkey] = newvalue
"""

my_dict3["key4"] = key4
print(my_dict3["key4"])

"""
also means that you update dict values the same way 

"""

my_dict3["key3"] = 1 
print(my_dict3["key3"])

"""
when we were working with lists, and try to access a list at an index that dosent exist index error\:

"""
