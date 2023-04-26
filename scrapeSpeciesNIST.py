# -*- coding: utf-8 -*-
"""
This file scrapes NIST for all of the IR spectrums available in jcamp format for every item in the species list

"""

import pandas as pd
import os
from scrapeIR import scrape_ir

#open the species csv 
df = pd.read_csv('species.csv',sep='\t')
#drop all items without a CAS
df_dropnan = df.dropna()
#reindex dropnan df
df2 = df_dropnan.reset_index(drop=True)

#convert cas numbers to list format
cas_list = list(df2.CAS)

#paramaters to pass to scrape function
params={'JCAMP': '', 'Type': 'IR', 'Index': 0}

#create directory needed to store IR files if it does not already exist
dir_path = 'scrapedFTIR'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

#call my scrape IR function 
scrape_ir(cas_list, params)


