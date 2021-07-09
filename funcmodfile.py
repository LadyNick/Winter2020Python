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