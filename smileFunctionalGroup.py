#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:49:43 2023

@author: ijvaillant
"""

import rdkit
from rdkit import Chem

def functional_group_exists(smiles, functional_group):
    '''
    This function accepts a chemical from is canonical smiles and a functional group in SMARTS format
    and returns a 1 if the functional group is in the molecule and a 0 if it is not

    Parameters
    ----------
    smiles : String
        The smiles string of the chemical you are checking.
    functional_group : String
        SMARTS string for the functional group of interest.

    Returns
    -------
    int
        1 means the functional group does exist within the molecule
        0 indicates the functional group does not exist within the molecule.

    '''
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return 0
    else:
        fg_mol = Chem.MolFromSmarts(functional_group)
        if fg_mol is None:
            return 0
        else:
            matches = mol.GetSubstructMatches(fg_mol)
            if len(matches) > 0:
                return 1
            else:
                return 0