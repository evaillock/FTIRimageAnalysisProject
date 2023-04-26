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

    #loop through every CAS in the passed list to get each IR spectrum
    for cas_id in cas_ls:
        #utilizing try and except to catch errors with specific CAS numbers for future troubleshooting
        try:
            params['JCAMP'] = 'C' + cas_id
            response = requests.get(nist_url, params=params)
            #check to see if spectrum exists for CAS, move to next item in loop if does not
            if response.text == '##TITLE=Spectrum not found.\n##END=\n':
                continue
            #if spectrum exists write to file in spectra folder
            with open(spectra_path +cas_id +'.jdx', 'wb') as data:
                data.write(response.content)
            #visual note of download
            print(cas_id,' jdx downloaded')
        except:
            #visual note of error
            print('error with cas: ',cas_id)
    #print confirmation that loop is finished        
    print('done')


