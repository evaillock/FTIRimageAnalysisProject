#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:49:18 2023

@author: ijvaillant
"""

import jcamp
import os
import shutil
import glob

#this script checks the files scraped and moves them to a good units or bad units folder
#in this case good units are files already in wavenumber and absorbance

#path that contains the IR files
path = os.path.join(os.getcwd(), 'scrapedFTIR', 'ir')

#where we want to store files in ABS and Wavenumber
goodPath = os.path.join(path, 'goodUnits')
#where to store items not in ABS and Wavenumber
badPath = os.path.join(path, 'badUnits')


#create the folders at the good and bad path if they don't exist already
if not os.path.exists(goodPath):
    os.makedirs(goodPath)
    
if not os.path.exists(badPath):
    os.makedirs(badPath)
    
extension = 'jdx'
all_files = glob.glob(os.path.join(path, "*.jdx"))


for file in all_files:
    data = jcamp.jcamp_readfile(file)
    wavenumbers = data.get('x_units', r'N\A').lower() != 'micrometers'
    absorbance = data.get('yunits', r'N\A').lower() == 'absorbance'
    # move file if wavenumbers is in micrometers
    
    if wavenumbers == False:
        print('bad apple')
        shutil.move(file, badPath)
    
    # move file if not in absorbance
    if absorbance == False:
        shutil.move(file,badPath)
    else:
        shutil.move(file,goodPath)
