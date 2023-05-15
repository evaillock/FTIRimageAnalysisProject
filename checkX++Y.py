#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:45:38 2023

@author: ijvaillant

This runs to check that all of the xy data in the jcamp files are in '(X++(Y..Y))' format
"""

import jcamp
import os
import glob

#path that contains the IR files
path = os.path.join(os.getcwd(), 'scrapedFTIR', 'ir','goodUnits')
    
extension = 'jdx' #extension for jcamp files
all_files = glob.glob(os.path.join(path, "*.jdx")) #container for all of the files

dtype = '(x++(y..y))' #need our jcamps to be in this format for further analysis
numNot = 0 #number not in proper format counter
for file in all_files:
    data = jcamp.jcamp_readfile(file)
    xydata = data.get('xydata', r'N\A').lower() != dtype
    if xydata == True:
        numNot += 1

print(numNot) #gives a count of how many files were not usable
