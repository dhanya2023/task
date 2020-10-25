#!/usr/bin/env python
# coding: utf-8

import pandas as pd
def down_sample(files,column,rule):
    index = 0
    for file in files:
        df = pd.read_csv(file+'.csv').iloc[:,1:]
        df[column[index]] = pd.to_datetime(df[column[index]])
        df.set_index(column[index]).resample(rule).mean().to_csv(file+'Downsampled.csv')
        index = index + 1
down_sample(['detail','detailVol','detailTemp'],['Absolute Time','Realtime','Realtime'],'1T')

