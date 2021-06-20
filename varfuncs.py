'''NUMBERS STRINGS LISTS TUPLES DICTIONARY FUNCTIONS'''

'''NUMBERS'''
#int(x) convert to int
#long(x) convert to long int
#float(x) convert to float
#complex(x) convert to complex w real part x and imaginary 0
#complex(x,y) convert x and y to complex w real x imaginary y
#abs(x) positive distance between x and 0
#ceil(x) ceiling of x: smallest int not less than x
#cmp(x,y) compare x and y, -1 if x is less, 0 if equal, 1 if x greater
#fabs(x) abs val of x
#floor(x) floor of x: largest int not greater than x
#log(x) natural log of x for x>0
#log10(x) same but base 10
#max(x,y,z,..) returns max of x y and z
#min(x,y,z,..) same but min
#pow(x,y) val of x^y, in this ^ is ** 
#round(x[,n]) x rounded to n digits from the decimal point
#sqrt(x) sqrt of x for x > 0

#choice(seq) returns a random item from a list tuple or string
#radrange([start,]stop[,step]) a random selected element from range(start,stop,step)
#random() a random float r that less than or equal to 0 or less than 1
#seed([x]) sets the int starting val used in generating ran numbs
#shuffle(lst) randomizes the items of a list in place, returns nothing
#unform(x,y) a random float r such that x is less than or equal to r and r is less than y, x<r<y

#trig functions acos(x) asin(x) atan2(y,x) atan(x) cos(x) hypot(x,y) sin(x) tan(x) all radians
##degrees(x) convert to degrees, radians(x) convers to radians
#also has mathematical constants pi and e


'''STRINGS'''
#print(string[x:y]) this will print the string from index x to yth place of string
#^^[x] will give char at x index

#print(string[:x]) this will print the string from the beginnign to the xth character
# in        returns true if a char exists in given string
# not in    returns true if char doesnt exist in string
#%% is if you want one signle %
#printing \\ will print one single \
#doing print(r"string") will print the raw version of the string, as in it will take the special characters as is

#capitalize() capitalizes first letter of string
#center(width,fillchar) returns a space-padded string with the original strin centered to a total of width cols
#count(str,beg=0,end=len(string)) counts how many times str occurs in string or in substring if range chosen
#endswith(suffix,beg=0,end=len(string)) same as above but checks if end of string has suffix inputted or substr
#find(str,beg=0,end=len(string)) same but true or false if find a string in a string
#index(str,beg=0,end=len(string)) same as ^^ but raises exception is str not found
#isalnum() returns true if at least 1 char and all chars are alphanumeric
#isalpha() same but letters only
#isdigit() implied
#islower() implied
#isnumeric() implied
#isspace() implied
#istitle() if properly titlecased
#isupper()
#join(seq) merges string representations of elements in sequence sea into a string with separator string
#lower() implied
#lstrip() removed all leading whitespace in string
#max(str) returns max alpha char
#min(str) implied
#replace(old,new[,max]) replaces all occurences of old in string with new or at most max occurrences
#rfind(str,beg=0,end=len(string)) same as find bust search backwards??? why
#same for rindex
#rstrip() removes all trailing whitespace of string
#split(str="",num=string,count(str)) splits string according to delimiter str(space if not provided) and
#   and returns list of substrings; split into at most num substrings if given
#splitlines(num=string,count('\n')) splits string at all or num newlines and returns a list of each line with newlines removed
#startswith(str,beg=0,end=len(string)) same as suffix but the beginning
#strip([chars]) performs both lstrip and rstrip on string
#swapcase() inverts casing
#title() returns titlecased version of string


