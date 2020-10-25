#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest

class TestSuites(unittest.TestCase):
 
    def completeTest(self):
        pathCSV = r'detail.csv'
 
        with open(pathCSV, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for item in row:
                    try:
                        getattr(MyFile.myClass, item)()
                    except AttributeError:
                        print("Unknown attribute", item, "ignored")
                        
    def completeTest(self):
        pathCSV = r'detailVol.csv'
 
        with open(pathCSV, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for item in row:
                    try:
                        getattr(MyFile.myClass, item)()
                    except AttributeError:
                        print("Unknown attribute", item, "ignored")
                        
    def completeTest(self):
        pathCSV = r'detailTemp.csv'
 
        with open(pathCSV, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for item in row:
                    try:
                        getattr(MyFile.myClass, item)()
                    except AttributeError:
                        print("Unknown attribute", item, "ignored")      
 
    @staticmethod
    def myTests():
        suite = unittest.TestSuite()
        suite.addTest(TestSuites('completeTest'))
        return suite
 
if __name__== "__main__":
    runner.run(MyFile.TestSuites.myTests())


# In[ ]:




