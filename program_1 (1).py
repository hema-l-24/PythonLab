#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m1 = int(input("Enter marks of internal 1: "))
m2 = int(input("Enter marks of internal 2: "))
m3 = int(input("Enter marks of internal 3: "))

if m1<=m2 and m1<=m3:
    avg = (m2+m3)/2
elif m2<=m1 and m2<=m3:
    avg = (m1+m3)/2
elif m3<=m1 and m3<=m2:
    avg = (m1+m2)/2
    
print("Average of best 2 marks out of the 3 internal tests is ", avg)


# In[ ]:


val = int(input("Enter a value "))

str_val = str(val)
if str_val == str_val[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    
for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i)," appears ", str_val.count(str(i)), " times ")


# In[ ]:




