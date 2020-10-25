#!/usr/bin/env python
# coding: utf-8

# Library Import
import numpy as np
import pandas as pd


# directory

from os import listdir
directory = '../Data/'
files = listdir(directory)


# extract data from files
def extract_respective(files):
    details = []
    details_vol = []
    details_temp = []
    for file in files:
        file_df = pd.read_excel(directory+file, None)
        for sheet in file_df.keys():
            if 'Detail_67' in sheet:
                details.append(file_df[sheet])
            elif 'DetailVol_67' in sheet:
                details_vol.append(file_df[sheet])
            elif 'DetailTemp_67' in sheet:
                details_temp.append(file_df[sheet])
    return pd.concat(details, axis=0), pd.concat(details_vol, axis=0), pd.concat(details_temp, axis=0)


details_df, details_vol_df, details_temp_df = extract_respective(files)


# saving all files with respective names
details_df.to_csv('detail.csv')
details_vol_df.to_csv('detailVol.csv')
details_temp_df.to_csv('detailTemp.csv')
