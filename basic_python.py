
# Nimbalkar Dhananjay  // date 25/07/25


'''a = 10
b = 10
c = a+b
print(c)
print("Hello Dhananjay")'''

'''
!a1 = 1
1b =2 
c# =0 
d 1 = 1  '''

'''print(!a1)
print(1b)
print(c#)
print(d 1)'''

'''
var1 = 1
_a1 =2 
c_ =0 
_d_1 = 1

print(var1)
print(_a1)
print(c_)
print(_d_1)


# swap the values of variable without use third var
A = 25
B  = 40
A = A+B
B = A-B
A = A-B
print("\n", A)
print("\n", B)
'''

# operators in python 
#1. Arithmetic Operator    // +,-,*,/,%
#2. comparison operator // > ,< ,<=,>=
#3. Logical Operator       // and , or , not
#4. Bitwise operator    // & , | , ~  to complement , ,<< ,>>
#5. Assignment operator // = , -= ,+= , *= ,/= , <<= ,>>=
#6. Membership operator 



#1. Arithmetic Operator    // +,_,*,/,%
# get input through user 
'''
x  = int (input("Enter the first  number "))
y  = int (input("Enter the  second number "))  

print(x+y)
'''




#2. comparison operator // > ,< ,<=,>=
'''
x  = int (input("Enter the first  number "))
y  = int (input("Enter the  second number "))
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

'''
#3. Logical Operator       // & , | , !
'''
x  = int (input("Enter the first  number "))
y  = int (input("Enter the  second number "))

print(x & y)
print(x|y)
print(not x)
'''


#4. Bitwise operator    // & , | , ~, ,<< ,>>   // operation on binary 
'''
x  = int (input("Enter the first  number "))
y  = int (input("Enter the  second number "))
'''

'''
x = 10
y =4

print(x & y)   # false
print(x|y)      #  true +=
print(~x)    
print(x^y)
print(x<<2)
print(x>>3)

'''


# Assingment operator 

a = 10 
b = a
print(b)

b += a
print(b)

b -= a
print(b)

b *= a
print(b)

b <<= a
print(b)

b /= a
print(b)








# counting sort 
#1. find largest no 
#2. create count arr with size largest+1
#3. calculate frequency of each elements and store in count arr
#. build an sorted arr


#1. find largest no 
def counting_sort(arr, length):
  max = arr[0]
  
  for i in range(1,length):
         if arr[i] > max:
            max = arr[i]
            
  return max
arr = [2,3,3,7,9]
length = len(arr)
ans = counting_sort(arr,length)
#print(ans)

#2. create count arr with size largest+1



# Nimbalkar Dhananjay // date 01/08/25

# Built-in datatype in python 

#1. Integers
a =12 
print(type(a))

#2. Float

b = 99.99
print(type(b))

#3. Complex
i = 10
c = 2+3j
print(type(c))

#4. String

name ="Dhanu"
print(type(name))



# User Defined Data types in python 

#1. List // mutable || same and diff element allow || []

a = []
print(a)
a = [1,2,3 , "dhanu"]
print(a)

# accessing the element from list 
print(a[1], "first value in list")
 
# using loop
for i in a:
 print(i)
 
#2. Tuple // immutable  || same and diff element allow  || ()
tp1 = ();
print(tp1)

tp1 = (1,2,3,4,5)
print(tp1)

# accessing the element from tuple
print(tp1[0])  # access the first element 

# slicing element 
print(tp1[1:4])  

#working of slice function 

'''1 is the start index (inclusive) — it starts at index 1, which is the element 2.

4 is the stop index (exclusive) — it stops before index 4, so it goes up to index 3.'''


# repetition 
my_tuple = ("Dhanu")

# now i want repete this value in my tuple in 5 time 
final_tuple = my_tuple*5 
print(final_tuple)


# built-in  function in tuple 
#1. len 
#2. min 
#3. max
#4 sum

print(len(tp1))
print(min(tp1))
print(max(tp1))
print(sum(tp1))


#3 Set // unordered || mutable || unique || {}
#ex. 
set1 = {1,2,3}
print(set1)

# set operatios 
#1. union 
set1 = {1,2,3}
set2 = {2,4,5};
print(set1.union(set2))

#2. Intersection 
set1 = {1,2,3}
set2 = {2,4,5};
print(set1.intersection(set2))

#3. difference  // return unique element from set1
set1 = {1,2,3}
set2 = {2,4,5};
print(set1.difference(set2))

#4.symmetric_difference// return unique element from set1 + set2
set1 = {1,2,3}
set2 = {2,4,5};
print(set1.symmetric_difference(set2))


#4. dictionary || {key:value}||dict() method ||key always unique ||immutable 

#ex both are same || for dict(key = value ) || i simple {key:value}
dictionary = {1:"dhananjay" , 2:"pratap",(1,2):[1,2,3]}
#or 
dhanu = dict(a="dhananjay",b="pratap")
print(type(dhanu))

# operations on dict
#1. access 
 #i. using key 
  #ex. 
print(dictionary[(1,2)])

#or 

 #ii. using get() method || syntax dict.get(key , value ) // value optional
 
print(dictionary.get(1))


#Iteration 
for key in dhanu # for key 
for value in dhanu.values():  # for value 
for key , value in d.items():  # for key-value


##### remove element from dict 

#del dhanu["a"]  #delete element
print(dhanu)


dhanu.pop("a") # remove first element 
print(dhanu)

print(dhanu.popitem()) # remove last element




           


