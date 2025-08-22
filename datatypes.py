# dict in  python 
#1. concate the two dict
'''
# concate the two  dict
d1 ={'name':'Dhananjay','age':20}
d2 ={'name':'pratap','age':20}
res = d1 | d2
print(res)
'''
#2. dict comprehension
n = int(input("Enter the value if n"))
result  = {x:x*x for x in range(1,n+1)}
print(result)

#3. find the freq of each char in string 

sample_string ="Dhananjay"
# convert into lovercase
sample_string = sample_string.lower()

# dict to store  res
char_count = {}
# iterate over all string
for char in sample_string:
# char present in dict increment it count 
 if char in char_count:
     char_count[char]+=1
 else :
 # otherwise set count = 1
    char_count[char] = 1
print(char_count)


#4. list with 5 elements

li = [1,2,3,4]
print(li)


#5. string palindrome 
def isPalindrome(str):
  start = 0
  end = len(str)-1
  while start < end:
   if str[start] != str[end]:
    return False
   start +=1
   end -=1
  return True
# call the function 
str = "121"
print(isPalindrome(str))


#6. number occurrence in arr
from array import*
arr = array('i',[1,2,3,4,6,4,7])

#print(arr.count(4))

#7 reverse the arr
from array import*
def reverseArray(arr):
    arr.reverse()
    return arr
   
arr1 = array('i',[1,2,3,4])
#print(reverseArray(arr1))
resp  = reverseArray(arr1)
print("reverse array elements")
for i in resp:
  print(i)
 
 
#8. rotate array by k

def rotateArray(arr,k):
  n = len(arr)-1
  k = k%n
  arr3 = [0]*n  
  for i in range(n):
    arr3[(i+k)%n] = arr[i];
  return arr3
  
# call function 
arr1 = array('i',[1,2,3,4])
resp  = rotateArray(arr1, 1)
print("rotated array elements")
for i in resp:
  print(i)
 
