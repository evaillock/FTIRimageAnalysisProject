#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:36:50 2023

@author: ijvaillant
"""
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
def download_IR_spectrum(cas_number):
    '''
    This function scrapes the NIST chemistry webbook for a specific chemical by CAS number
    The function writes the IR spectrum jcamp file to a directory called scrapedFTIR making the directory
    if it does not already exist
    
    Parameters:
        --------------
        cas_number: the CAS identification number of the chemical you are looking for as a string
    
    Examples:
        ---------------
        #Get the water FTIR graph cas number 7732185
        download_IR_spectrum('7732185')
    '''

    # Create the directory if it doesn't exist
    directory = 'scrapedFTIR'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the URL for the NIST Chemistry WebBook page for the given CAS number
    url = f'https://webbook.nist.gov/cgi/cbook.cgi?ID={cas_number}&Type=IR-SPEC&Index=1'
    
    # Send a request to the URL and get the page content
    page = requests.get(url)
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract the chemical name from the page title
    title = soup.title.string
    name = title.split(' - ')[0]

    # Find all the jcamp-dx links in the page
    jcamp_links = []
    for link in soup.find_all('a'):
        if 'jcamp-dx' in link.get('href'):
            jcamp_links.append(link.get('href'))

    # Download the jcamp-dx files
    for i, link in enumerate(jcamp_links):
        if not link.startswith("http"):
            link = "https://webbook.nist.gov" + link
        filename = f'{name}_IR_spectrum_{i+1}.jdx'
        filepath = os.path.join(directory, filename)
        try:
            urllib.request.urlretrieve(link, filepath)
            print(f'{filename} downloaded.')
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
