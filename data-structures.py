#taking input from users for adding two numbers

a=int(input("Enter the first number"))
b=int(input("Enter the second numebr"))
sum=a+b
print(sum)

#taking a single character from user as input
ch=input("Enter a character")[0]
print(ch)

#taking user input while executing file from command prompt
import sys
a=int(sys.argv[1])  #taking index number as 1 and not 0 because 0 is the index number for file name (example: python file_name.py 2 3). 
b=int(sys.argv[2]) 
print(a+b)


#using 'eval' function (evaluates the expression given as input)
res=eval(input("Enter a mathematical expression"))
print(res)

                                                          
  
                                                        #LISTS
#list of int type
li_num=[1,5,7,9,13,15] 

#retrieving the number 13 from the list
li_num[4] or li_num[-2]

#retrieving all the elements from the list
lin_num[:]  

#retrieving all the elements in reverse order from the list
li_num[::-1]

#list of string type
li_str=['abc','pqr','xyz']

#retrieving 'pqr' from li_str
li_str[1]

#creating nested list
data=[li_num, li_str]

#list can contain element of multiple data types
li_data=['python',2.5,3]  #list containing a string, integer, and a float element

#list is mutable i.e it can be changed using following methods
li_data.append('Java')        #Java will be added as the last element of the list; ['python', 2.5, 3, 'Java']

li_data.insert(1, 'IDLE')     #'IDLE' will be added at index number 1; ['python', 'IDLE', 2.5, 3, 'Java']

li_data.remove(3)             #element 3 will be removed from the list, remove() takes the element to be removed as the argument and not the index number, to remove element using index number use pop() method; ['python', 'IDLE', 2.5, 'Java']

li_data.pop(0)                #pop() removes the elemenet using index number, element at index number 0 is removed; ['IDLE', 2.5, 'Java']

li_data.pop()                 #removes the last element from the list; ['IDLE', 2.5]

li_data.reverse()             #reverses the list; [2.5, 'IDLE']

li_data.index('IDLE')         #returns the index number of the element passed as argument; if the element occurs twice in the list, first index number of the element is returned

li_data.count(2.5)            #returns the count of occurence of the element in the list

li_data.copy()                #returns a copy of the list(li_data); [2.5, 'IDLE']

li_data.clear()               #removes all element from the list; []

del li_data[1:]               #deletes all element from index number 1

li_data.extend(['xyz', 34, 56, 'mno'])   #adding multiple elements to the list

min(li_data)   #returns the minimum value in the list having only integers

max(li_data)   #returns the maximum value in the list having only integers

sum(li_data)   #returns the sum of all integer values in the list

li_data.sort()  #sorts the list in ascending order

                                             
  
                                              #Tuples
#tuples are immutable, unlike list, used when the elements are fixed and will not be changed. Since they are immutable the speed of execution is faster than the list
tu_data=(1,2,3,4,4,'abc')

tu_data.count(4)    #count the occurence of number 4 in the tuple, in this case the answer is '2'

tu_data.index(2)    #returns the index value of number 2 in the tuple, the answer in this case is '1'

                                              
                                              #Set
 #set is an unordered collection of unique elements. 
** set does not support indexing as the elements are unordered

set_data={1,2,3,4,5,'abc'}

set_data.add(8)     #adds 8 to the list
set_data.remove(2)  #removes 2 from the list

                                              #Variables
#Strings are  immuatble and iterable over the set of characters
a='pyhton' #assigning string to a variable
b=5        #assigning int to a variable
id(a)      #returning address of variable a
id(b)      #returning address of variable b
type(a)    #returning data type of value stored in variable a
type(b)    #returning data type of value stored in variable b
