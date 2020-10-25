#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import cProfile
with cProfile.Profile() as pr:
   
# read the files 
df = pd.read_csv('detail.csv') 

   
# run the profile report 
profile = df.profile_report(title='CProfiling Report') 

df = pd.read_csv('detailVol.csv') 
profile = df.profile_report(title='CProfiling Report') 


df = pd.read_csv('detailTemp.csv') 
profile = df.profile_report(title='CProfiling Report') 

pr.print_stats()

