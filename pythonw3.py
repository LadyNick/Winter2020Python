#inside of a function, you can define a variaable to be global ie.
#global x

#objname.strip() will return the string without any whitespace at the beginning or end
#example of replace   -->   txt.replace("H","J")

#age = 36
#txt = "My name is John, and I am {}"    <<-- brackets are a placeholder
#print(txt.format(age))

#you can use or & and

#to insert in list you do list.insert(placementbefore, "lemon"),
#if placementbefore is 1, then lemon will be 2nd
#list[-1] refers to the last item, its reverse

#to add multiple things to a list, say add one list into another list
#list1.update(list to be added)
#for removing you use .remove or .discard

#for dictionaries, to get the value of a certain key you do
#dictname.get("keyname")
#to change a dict value you do dictname["keyname"] = newthing

#to add to dict you do dictname["keyname"] = "value"
#to remove from dictionary u can do dictname.pop("keyname")

#you can put if else in one line
#print("Yes") if 5 > 2 else print("No")

#to stop loop in while loop you use break
#to jump to next iteration in a loop use continue
#once the condition of a while is false, you put else:

#for x in range(6) loops through a code set 6 times

#def myfunction(): and then define 0on the next lines
#if u dont know # of arguments passed into function, add *at the front of the para
#if u dont know # of keyword arguments passed u used ** prefix in para def in function
#x = lambda a : a 
#^^^ lambda function that takes on parameter a and returns it

#FOR INIT AND ALL THE CLASS STUFF WITH THE UNDERSCORES YOU DEFINE IT WITH 2 UNDERSCORES NOT 1

#you can import a model with an alias doing import mymodule as mx
#print(dir(mymodule)) to print all variables and function names of mymodule module