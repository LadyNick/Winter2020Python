#I don't really think date and time is that important here

'''FUNCTIONS'''
SYNTAX 

def functionname( parameters ):
    "function_docstring"
    function_suite
    return [expression]        #<--- nothing in here means return nothing

EXAMPLE

def printme( str ):
    "This prints a passed string into this function"
    print(str)
    return


ALL PARAMETERS IN PYTHON ARE PASSED BY REFERENCE 
#you can define parameters by doing printme( str = "My string" ) in this case

#order of parameters does not matter if its something like this
# def printinfo( name, age )
#and u call it with printinfo( age = 50, name = "miki" )

#when defining a function you can have default parameters def printinfo(name, age=35)
#whateer is entered will call will overwrite it

'''Variable Length Arguments'''
#This makes it so that if there are additional arguments they can be added as parameters
#to a function which can be useful so that you don't have to call a function for every single
#argument for functions where the same thing happens over and over

Ex:

def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print var
    return

printinfo(10) outputs: 10
printinfo(70, 60, 50) outputs: 70 60 50    #all with newlines between because thats the way it prints


'''LAMDA FOR SMALL FUNCTIONS, VERY FEW LINES '''
Syntax

lamda [arg1 [,arg2,...argn]]:expression

sum = lamda arg1, arg2: arg1 + arg2;

#calling sum(10, 20) returns 30, calling sum(20, 20) returns 40

local and global variables
#if u define a variable outside functions and then within a function define a variable with the
#same name, it will be a local variable, not the global variable

'''MODULES'''
#A module allows you to logically organize your pyhton code. 
#**its a file of python code(basically with outside .hpp and .cpp when u wanna include them)

ie. support.py holds:

def print_func(par):
    print("Hello : ", par)
    return

to use the function from this file you import the module by:
    
    import support 
    #and now you can use the function print_func(par)
    
You can also import specific functions from a certain module 
syntax 
    #from modulename import name1[, name2[, ... nameN]]
ie.  from support import print_func, function2, function3

#to import all items you use : from modname import *, but you shouldnt use this a whole lot

USE dir() FUNCTION to get all the variables and functions from a ModuleNotFoundError
ie. 
    import math
    content = dir(math)
    print(content)
    
    #^^ this will print a large list of all the names and the first 3 will be the doc, filename
    #from where it was loaded, and the name of the ModuleNotFoundError
    
globals() and locals()

#calling these functions will return all the names that can be accessed lobally and globally
#the return type is dictionary, so names can be extracted using the keys() function
#YOU WOULD USE PRINT(globals()) or same for locals()

'''FILES IO'''
#str = raw_input("Enter your input: "), will print the quote and then take in input
#str = input(blah blah), same thing except itll take the input as python info,
#   meaning you can input [x*5 for x in range(2,10,2)] and it will return [10,20,30,40]

'''OPEN CLOSE WRITE READ RENAME REMOVE FILE THINGS'''
#open file function creates a file object syntax:
#file object = open(file_name [, access_model][, buffering])

#access_model refers to the mode of when the file is opened, ie read, write, append
#buffering is some weird thing doesnt seem that important, if u set to 0, no buffering happens

#attributes you can print that will return info about the file, w file being filename
#   file.closed     true or false,    file.mode returns mode,   file.name returns name,
#   file.softspace  returns false if explicitly required with print, true otherwise

#filename.close() to close
#fileobject.write( "quote" ) will write to the file
#fileobject.read([count])   if count is missing it tries to read as much as possible
#   count is bytes which is basically characters including spaces

#tell() will tell you the current position within the file, where the enxt read or write will occur
# seek(offset[,from]) method changes from the current file position
#       offset indicates number of bytes to be moved, from is the reference position, 0 is the 
#       beginning as default

#rename files you do os.rename(current_file_name, new_file_name), which includes the .txt or whatever
#remove you do os.remove(file_name)   ***IN QUOTES BY THE WAY AS IN THE FILENAME


#os.mkdir("newdir") makes a new directory called newdir
#os.chdir("newdir") changes directory to newdir directory
#os.getcwd() gets current directory
#os.rmdir('dirname') removes directory

'''CLASSES AND OBJECTS'''

#a class is a user defined protoype for an object  w attributes and functions

class ClassName:
    'Optional class documentation string'
    class_suite
    
#doc string can be accessed via ClassName._doc_
#class_suite has all the component statements defining class members, data attributed and functions

#example python class

class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
        
    def displayEmployee(self):
        print "Name: ", self.name, "Salary: ", self.salary

#empCount is a class variable shared among all instances of the class
# the _init_ is the equivalent to constructor functions, in python theyre called methods
#you can declare other normal functions
#the self is saying like to itself object

#example of calling would be, emp1 = Employee("Zara", 2000)
#emp1.displayEmployee() 

#getattr(obj,name[,default]) - to access the attribute of the object
#hasattr(obj,name) - to check if an attribute exists or not
#setattr(obj,name,value) - to set an attribute. If attribue does not exist, then it would be created
#delattr(obj,name) - to delete an attribute 

#build in class attributes
#   _dict_ dictionary w class's namespace
#   _doc_ class doc string or none if undefined
#   _name_ class name
#   _module_ module name in which the class is defined,  "_main_" if in interactive mode
#   _base_ a possibly empty tuple containing the base classes 
# del to delete objects

#DEFINE CLASSES IN A SEPARATE FILE AND IMPORT THEM VIA import

#class inheritance:
#class SubClassName (ParentClass1[,ParentClass2,...]):
    'optional doc string'
    #class_suite

#issubclass(sub,superior) boolean function returns true if subclass sub is a subclass of the super class
#isinstance(obj,class) returns true if obj is an instance of class class
#ofc you can override parent functions

VVV TWO UNDERSCORES 

#_init_(self[,args...]) constructor
#_del_(self) destructor
#_cmp_(self,x) object comparison

#TO MAKE PRIVATE VARIABLES, you do a double underscore before the variable
#       __secretCount = 0
#it can become accessible if you do objectname._classname__secretCount, but otherwise it cant
