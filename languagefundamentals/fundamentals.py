
# this is a python comment

# identifiers
# simply a name is callled identifier
# function_name
# variable_name
# class_name

# variables=> are used to represent a memory location

# coding standard
# company_name="luminar"==>snake_case(used in python),pep standard
# companyName="luminar"==>camel_case

bank_name="sbi"
ac_no=12345
amount=300
# hello sbi user your account 12345 is credited with amount 300
print(f"hello {bank_name} user your account {ac_no} is credited with amount {amount}")# f string for formatting
print("______________")
# operators

# 1. arithmetic operators -> +,-,*,/,%,**,//(fllor division)
#         10/2=5.0    10//2=5
#         floor(10.31)=10    round(10.31)=10    ceil(10.31)=11 (basic maths)

# 2. relational operators -> <,>,<=,>=,==,!=
#       can be used with int to int,char to char, boolean to boolean

# *,+ can also be used in strings

#3. logical operator -> and,or,not

# 4. bitwise operator -> &(bitwise and),|(bitwise or),^(xor)
#   x   y   x^y
#   0   0    0
#   0   1    1
#   1   0    1
#   1   1    0

# assignment
# num1+=10 ==> num1=num1+10
# num1-=20 ==> num1=num1-20
# num1*=2 ==> num1=num1*2


# flow controls -> if..else,looping

# looping
# 1. while -> use only when exact length of iteration is not known
# 2. for -> use only when exact length of iteration is known

# print(value,end="\n",sep="") end="\n" is by default newline

#String class

# string => sequence of characters
print("""valid string""")
# python string is designed in class 
# method => defined inside a class
#           object_name.method() 
# function => defined outside a class
# object => real world entity constructed by class
#   eg:- class str:
#           casefold() #method
#       strobj="HELLO"
#       strobj.casefold()

# functions => print(), input(), sorted()

# def function_name(parameter1,parameter2):
#   function definition
#   return value
# function_name(p1,p2)   #function call


# lambda function => used to simplify program
#                    does not have function name

print("-------------------------------------")


add=lambda n1,n2:n1+n2
print(add(100,200))

print("-------------------------------------")


# round =>
num=123.456783
out=round(num,2)
print(out)

print("-------------------------------------")

# map
numbers=[1,2,3,5,6,7]
cubes=list(map(lambda num:num**3,numbers))
print(cubes)

add_five=list(map(lambda num:num+5,numbers))
print(add_five)

print("-------------------------------------")


# filter()
numbers=[1,2,3,5,6,7]
odds=list(filter(lambda num:num%2!=0,numbers))
print(odds)

names=["python","pytz","django","rest","angular","pytorch"]
name_filter=list(filter(lambda w:w.startswith("py"),names))
print(name_filter)



# builtin.py  -> print()
#                input()
#                type()
#                sorted(iterable,key,reverse)
#                sum(iterable)
#                max(iterable,key)
#                min(iterable,key)
#                range()
#                round()
#                len()
#                map(function,iterable)
#                filter()



# python collections-> used to organize data


# list 
# tuple
# set
# dictionary

# collection_name        define             insertion order preserved or not     duplicate_allowed   update / mutable           methods
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# list                     []                       preserved                        allowed              yes              append(), count(), index(), pop(),
#                 empty_list=list() or []                                                                                  insert(), remove(), copy(), reverse()
#                                                                                                                          sort()
# 
# tuple                    ()                       preserved                        allowed              no               count(), index()
#                empty_tuple=tuple() or ()
# 
# set                  {10,20,30}                  not preserved                    not allowed           yes               add(), intersection(), union(), difference(),
#                    empty_set=set()               indexing not supported                              (by using another    pop(), remove(obj), discard(obj), update(),
#                                                                                                         set)              symmetric_difference()
# 
# dictionary                {}                     preserved                   duplicate key not allowed    yes             keys(), values(), items(), get(key), pop(key),
#                      {"key":value,}              indexing not supported      but values allowed                           update({key:value}), 
# 
# 



# list methodds
#       - append()->add a new element at the end of the list
#       - count()->occurence of an element in list
#       - index() ->position of an element in list
#       - pop() ->remove last element from list ,pop(index=-1)
#       - insert(index,object) ->add a new element to specified position
#       - remove(obj) ->remove the element by giving object
#       - copy() ->copy the list
#       - reverse() ->reverse the list
#       - sort()


# list comprehension
# nested list

# for .... else


# tuple methods
#       - count()->occurence of an element in list
#       - index() ->position of an element in list


# set methods
#       - add()-> add new element in set
#       - intersection()-> common elements from two sets
#       - union()-> return all unique elements from two sets 
#       - difference()-> remove set2 elements from set1 (diff=st1.difference(st2))
#       - pop()-> remove element from set
#       - remove(obj)-> remove the specified element from set, if element is not in set it will display an error
#       - discard(obj)-> remove the specified element from set, if element is not in set it will not display any error but return None
#       - symmetric_difference()-> (A U B) – (A ∩ B)
#       - update()-> a set can update by using another set



# dictionary methods
#               - keys()-> return all keys in a dictionary
#               - values()-> return all values in a dictionary
#               - items()-> return both keys and values in a dictionary
#               - get(key)-> return a specific value using a key from dictionary, it returns None when the given key is not in dictionary
#               - update({key:value})-> update the value in a dictionary
#               - pop(key)-> remove element from a dictionary








# File I/O -> text,json

# File processing
# Step 1:- File open -> 
#           f=open(the_path,mode)  #mode=w,r,a


# File operations =>
#               - read = r
#               - write = w
#               - append = a




# Json -> Javascript object notation

# Json is a format that used to transfer data.

# Xml,Yaml,Gson are also the format that used to transfer data.


# data.json - filename
# json.py =>  def load(file_object)   ,it should import to pgm.py 
# re.py   =>  def fullmatch()
# bultins.py=> def print()
#              def input()
#              def max()

# pgm.py
# from json import load
# f=open("data.json","r")
# result=load(f)

# from re import fullmatch
# from bulltins import print,input,max



# Regular Expressions=> used for pattern matching

# re.py   functions=>

#                   -def finditer(pattern,text)-> used to return the position of pattern in given string
#                   -def fullmatch(rule,text) -> used to check the entire pattern match with rule
#                   -def search()
#                   -def start()-> used to print position of search pattern in text
#                   -def group() -> used to print search pattern


# Data Structures -> organizing and storing data in a particular manner
#           - Array
#           - Stack ->LIFO order , stores in continuous memory location
#           - Queue -> FIFO order , stores in continuous memory location
#           - Linked list
#           - Tree
#           - Graph

# Queue operations -> insertion,deletion
# insertion -> front is fixed and rear is incrementing while adding new element in queue
#           -> inserting in rear position and deleting from front

# Stack operations -> Push for insertion and Pop for deletion
# top is incremented by adding new element to stack and
# top get decremented while removing an element from stack
# stack underflow -> happens when we try to pop(remove) an item from stack, when nothing is actually there to remove
# stack overflow  -> happens when we try to add new item to stack, when stack is full

# Linked list -> contains  a node -> data which stores data and pointer to next address

#  Tree -> root node, child nodes, leaf nodes
# binary tree -> right node has largest element than root node and left node has smallest element than root node
# tree traversing -> inorder   (LEFT,ROOT,RIGHT)
#                 -> preorder  (ROOT,LEFT,RIGHT)
#                 -> postorder (LEFT,RIGHT,ROOT)





# front end -> creativity
# back end -> logical side 

# FRONT END - HTML, CSS, Bootstrap, Javascript, Angular




# OOPS => Object Oriented Programming

# class -> plan or design pattern or blueprint or template
#          list,set,tuple,dict
# class contain attributes and methods

# example

# class Student:    # class
#       name:str
#       rollnumber:int
#       course:str

# def set_student(self,name,rollno,course):  # method
#     self.name=name
#     self.rollnumber=rollno
#     self.course=course

# def display_student(self):
#     print(self.name,self.rollnumber,self.course)

# self=> used to point current instance 

# object -> the thing that construct using class


# constructor
# constructor -> initializing instance variables
# in java,c++ constructor name is same as class name 
# in javascript constructor()
# in python __init__()
# constructor automatically invokes while object creation

# __str__ => string representation of object


# function overloading => same function name but different number of parameters
#                         python does not support function overloading


# *args => take any number of parameters in a function in the form of tuple
# **kwargs => take any number of parameters in key-value format in a function in the form of dictionary


# decorator =>
# def swap_num(fn):       # fn takes function as parameter value
#     def wrapper(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return wrapper

# @swap_num
# def sub(n1,n2):
#     return n1-n2

# @swap_num
# def div(n1,n2):
#     return n1/n2

# print(sub(2,10))
# print(div(2,10))


# inheritance -> methods and properties of parent class is acquired by child class

# polymorphism - method overloading, method overriding
# method overloading -> within a class
# method overriding ->requires minimum 2 class

# super()

# abstraction -> used to hide the implementation details of methods in a class
# abstract methods -> methods that do not have definition