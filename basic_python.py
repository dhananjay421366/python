
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

            
           


