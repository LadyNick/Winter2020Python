'''Use 3 single quotes
To make a multiline comment'''

# this is a single line comment
'''
Use python filename.py to run a python file
If you do python, it takes the next lines as python code,
so use exit() to exit if you do that 
'''

'''Variable Types'''
#In python the variable types are automatically decided, you can't combine string and ints though
#semicolons aren't used in python, which is why indexing is so important

fruit = "strawberry"    #string
bears = 3               #int
money = 13.65           #floating point
a,b,c = "Hi","Hello","Hey"  #assigning with commas

#Delete items with del
#To print things you use print(variablename) or you do print(quote or number or whatever)

print(fruit)
print(fruit,bears,money)
#python practice.py returns this:
#strawberry
#strawberry 3 13.65
#if the first line was print(fruit,end="") it removes the newline 
#if the first line was print(fruit,bears,money,sep='') it removes the spaces in between

'''There are Numbers, Strings, Lists, Tuples, & Dictionary'''

#strings and lists are pretty similar
#**lists can be a combination of different types
'''
print(str)                  prints the entire string or entire list
print(str[0])               prints first character or first element in list
print(str[2:5])             start and end values, the first refers to index, second refers to nth placement
print(str[2:])              prints from the first values index to the end of the string or list
print(str*2)                prints the string or list twice
***print(str + "blah")      STRINGS prints the var string + the added string
***print(list + list2)      LISTS prints the list + list2 elements
'''

#TUPLES ARE LIKE LISTS BUT THEY ARE CONSTANT AND CAN'T UPDATE THEM, so the prints are the same
#you can update a list by doing list[index] = update

#DICTIONARY
#A dictionary is a word with a definition, in this case the word can be any type and the 
#definition can be any type
'''
dict = {}                    this starts a dict
dict['one'] = "number 1"       in this case, its a new entry, or for the entry 'one', we assign some def'''
dictex = {'name': 'Nikki', 'bday': 1013}  #this sets up a dict, with the words and defs 
'''
the commands for printing are basically the same
print(dict['one'])            prints value for 'one' key
print(dictex)                 prints the dict dictex
print(dictex.keys())          prints the words
print(dictex.values())        prints the definitions
'''

print(dictex)               #{'name': 'Nikki', 'bday': 1013}
print(dictex['name'])       #Nikki, ** still does automatic newline
print(dictex,dictex['name'],dictex['bday'])  #this prints the above w spaces, and the 1013 at the end

'''
int(x[,base])           converts x to integer, base specifies the base if x is string
long(x[,base])          to long int
float(x)                to floating point num
complex(real [,imag])   creates a complex number
str(x)                  converts to string representation
repr(x)                 to expression string
eval(str)               evaluates a string and returns and object
tuple(s)                converts s to a tuple
list(s)                 to a list
set(s)                  to a set
dict(d)                 creates dictionary, d must be a sequence of (word,def) tuples
frozenset(s)
chr(x)
unichr(x)               int to unicode char
ord(x)                  single char to int val
hex(x)                  int to hex string
oct(x)                  int to octal string
'''

'''BASIC OPERATORS & DECISION MAKING'''

''' 
+ add, - sub, * mult, / div, % mod, ** expo, == equal, != not equal, <> not equal
> < >= <= = += add and assign, -= sub assign, *= assign, so on
| or, ^ XOR, & and, ~ ones complement, << binary left shift, >> right shift
'''

'''
if, else, elif (else if), you put a colon after every if and else and elif 
if blah blah:
else blah:
**you can also write it in the same line
if ( blah ) : do blah blah
'''

#I already know how loops work 
candies = ['lolipop', 'gum', 'choco'] #list 
num = 1;
for candy in candies:
    print(num,":",candy)
    num+=1
#prints... remember theres spaces
#1 : lolipop
#2 : gum
#3 : choco

'''
%d is a placeholder for a number, %s for string, %c for char
'''

#for num in range(10,20) iterates from 10 to 20
#for i in range(2,num)   iterates from 2 to whatever num is 
#print('%d equals %d * %d' % (num,i,j)) prints the vlaues in the vars at the locations
#breaks are used to move to the earliest for loop based on the least amount of indentation
#or it can go to the next for loops, it can cut time 
'''
for blah
    for i in blach
        if blah
            a
            b
            c
            break
    else
        blah
                break
'''