#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:36:50 2023

@author: ijvaillant
"""
import os
import requests


def scrape_ir(cas_ls, params):
    '''Collect data from NIST database and store them in jdx format.

    Args:
        cas_ls: (list) CAS ids to download data for
		params: (dict) queries to be added to url


    Returns:
        None
    '''	
    #nist url
    nist_url = "https://webbook.nist.gov/cgi/cbook.cgi"
	#Create directory for the relevant spetra 
    spectra_path = os.path.join('./scrapedFTIR', params['Type'].lower(), '')
    if not os.path.exists(spectra_path):
        os.makedirs(spectra_path)

    
    for cas_id in cas_ls:
        try:
            params['JCAMP'] = 'C' + cas_id
            response = requests.get(nist_url, params=params)
    
            if response.text == '##TITLE=Spectrum not found.\n##END=\n':
                continue
            
            with open(spectra_path +cas_id +'.jdx', 'wb') as data:
                data.write(response.content)
            print(cas_id,' jdx downloaded')
        except:
            print('error with cas: ',cas_id)
    print('done')


