#  list and tuples
# it is a builtin data types

#  types of data types

# mutable data types
# 1)list
# 2)dictionary
# 3)sets

# immutable data types
# 1)numbers
# 2)Strings
# 3)tuples

#                                LIST
marks=[89,99,00,767,779,45,]

print(marks)

# list method does not return any thing

# directly apply

#     TUPLES 
# tuples are immutable
tup=(6,7,8,8,7)
tup=(1,)
print(tup)
print(type(tup))


# PRACTICE QUESTION
# WAP ask use to enter your three movies and stored in list

moves1=input("ENTER YOUR 1 FAVOURITE MOVIES: ")
moves2=input("ENTER YOUR 2 FAVOURITE MOVIES: ")
moves3=input("ENTER YOUR 3 FAVOURITE MOVIES: ")

movielist=[]
movielist.append(moves1)
movielist.append(moves2)
movielist.append(moves3)



print(movielist)
print(type(movielist))

#  check the list is a palindarone 

plist=[]
pelement=input("ENTER THE FIRST ELEMENT OF YOUR LIST: ")
plist.append(pelement)
pelement=input("ENTER THE SECOND ELEMENT OF YOUR LIST: ")
plist.append(pelement)
pelement=input("ENTER THE THIRD ELEMENT OF YOUR LIST: ")
plist.append(pelement)
pelement=input("ENTER THE FOURTH ELEMENT OF YOUR LIST: ")
plist.append(pelement)
pelement=input("ENTER THE FIFTH ELEMENT OF YOUR LIST: ")
plist.append(pelement)

clist=plist.copy()
clist.reverse()

if(plist==clist):
    print("THE LIST IS PALINDRONE")
else:
    print("YOUR LIST IS NOT PLINDRONE")

    


