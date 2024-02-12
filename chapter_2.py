#      chapter 2   Strings & Conditional Statements 

str1= "this  is  method 1 for creating string"
str2= 'this method 2 for creating string'
str3= """"this is third method of creating string"""

#  escape sequence character

#  for breaking line /n
# for tab /t
#  for concatination +

# len() is used for finding length of string

print(len(str1))
print(len(str2))
print(len(str3))

num1=str(123455667788990)
print(type(num1))
print(len(num1))

#  indexing

#  indexing is start at zero
string1="my name is mirza ahmer baig"
print(string1[4])
# string1[0]="d" this is not possible onle access data not changeed in string

#    slicing

name1="my name is mirza ahmer baig"
print(name1[1:])
print(name1[1:5])
print(name1[3:7])

#  backword counting is also worked

print(name1.replace("my","your"))

print(name1)

name1=name1.replace("my","your")

print(name1)
#  PRACTICE QUESTION

firstname=input("ENTER YOUR FIRST NAME: ")
fl=len(firstname)
print("THE LENGTH OF YOUR FIRSTNAME IS : " , fl)

#         CONDITIONAL STATMENT
# if elif else

marks=int(input("ENTER YOUR MARKS OUT OF 100: "))
if(marks>=90):
    print("YOU GOT A GRADE")
elif(marks>=80):
    print("YOU GOT B GRADE")
elif(marks>=70):
    print("YOU GOT B GRADE")
else:
    print("fail")


    










