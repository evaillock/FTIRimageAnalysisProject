#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:29:26 2023

@author: ijvaillant
"""

import requests
from bs4 import BeautifulSoup

def getInchi(cas):
    '''
    This function accepts a chemical CAS number and returns the inchi key from the NIST webbook

    Parameters
    ----------
    cas : String
        String version of the chemical CAS registry number.

    Returns
    -------
    inchi_key : String
        The INCHI key for the chemical.

    '''
    # Construct the URL for the NIST website search page
    url = f"https://webbook.nist.gov/cgi/cbook.cgi?Name={cas}&Units=SI&Mask=20"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the span tag with the class "inchi-text"
    inchi_span = soup.find("span", class_="inchi-text")

    # Extract the InChI key from the span tag
    inchi_key = inchi_span.text.strip()

    # Return the InChI key
    return inchi_key