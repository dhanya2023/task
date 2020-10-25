#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

reader = csv.reader(open(r"detailVolDownsampled.csv"),delimiter=' ')
filtered = filter(lambda p: 'Central' == p[2], reader
csv.writer(open(r"detailVolDownsampled.csv",'w'),delimiter=' ').writerows(filtered)


# In[ ]:




