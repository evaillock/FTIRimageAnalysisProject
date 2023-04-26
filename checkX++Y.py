#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:45:38 2023

@author: ijvaillant
"""

import jcamp
import os
import glob

#path that contains the IR files
path = os.path.join(os.getcwd(), 'scrapedFTIR', 'ir','goodUnits')
    
extension = 'jdx'
all_files = glob.glob(os.path.join(path, "*.jdx"))

dtype = '(x++(y..y))'
numNot = 0
for file in all_files:
    data = jcamp.jcamp_readfile(file)
    xydata = data.get('xydata', r'N\A').lower() != dtype
    if xydata == True:
        numNot += 1

print(numNot)