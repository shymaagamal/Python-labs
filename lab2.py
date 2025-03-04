# 1. Reverse a String 

# Write a Python program to reverse a string. 

string="shaimaa gamal saeed"
 
s = string[::-1]
print(s)


# 2. Check if a String is a Palindrome 

# Write a Python program to check if a string is a palindrome 
# (reads the same backward as forward). 
string="NOON"
second=string[::-1]
if second == string:
    print("is palindrome")
else :
    print("is not a plindrome");    



# Remove Duplicates from a String 

# Write a Python program to remove duplicate characters
#  from a string.
# 
string ='shaimaa gamal'
nonDulicate=''.join(set(string))
print(nonDulicate) 



# 4.Find the Longest Word in a String 
# Write a Python program to find the longest word in a given string. 
# text = "Python is a great programming language" 
#Output=programming 

text = "Python is a great programming language" 
words = max(text.split(' '));
print(max(text.split(' '),key=len));


# 5.Find Common Elements Between Two Tuples 
# Write a Python program to find common elements between two tuples. 
# ``` python 
# tuple1 = (1, 2, 3) 
# tuple2 = (2, 3, 4) 
# # Output: (2, 3) 
tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)

common= list(x for x in tuple1 if x in tuple2 )
print(common)



# 6.Find the Maximum and Minimum Value in a Dictionary 
# Write a Python program to find the maximum and minimum value in a dictionary. 
# ``` Python 
# my_dict = {"a": 10, "b": 20, "c": 5}  
# Min= 5  , max=20 

my_dict = {"a": 10, "b": 20, "c": 5}  

max,min= max(list(my_dict.values())),min(list(my_dict.values()))
print(min)



# 7- Merge Two Dictionaries 
# Write a Python program to merge two dictionaries. 
# dict1 = {"a": 1, "b": 2} 
# dict2 = {"c": 3, "d": 4} 
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

 
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4} 
dict1.update(dict2)

print(dict1)




# 8- Find Common Keys in Two Dictionaries 
# Write a Python program to find common keys in two dictionaries. 
# dict1 = {"a": 1, "b": 2, "c": 3} 
# dict2 = {"b": 2, "c": 4, "d": 5} 
#Output: {'b', 'c'} 

dict1 = {"a": 1, "b": 2, "c": 3} 
dict2 = {"b": 2, "c": 4, "d": 5} 
print(set(dict1.keys() & dict2.keys()))



# 9-
# 
#longest sunstring in string

import copy
string = "abdullahabcdefghig"
lenOfLongestSubString=0
count =0
longestSubString=string[0]
buffer=string[0]
for  index in range(1,len(string)):
    if(ord(string[index])>ord(string[index-1])):
        count+=1
        buffer+=string[index]
    else:
        if(lenOfLongestSubString >count):
            count=0
            buffer=string[index]    
        else:    
            lenOfLongestSubString=count
            count=0
            longestSubString=copy.deepcopy(buffer)
            buffer=string[index]

 
print(longestSubString)