
# coding: utf-8

# In[30]:

numbers = list(range(2000, 3201))
for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        print (i, end=", ")

