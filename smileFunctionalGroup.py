#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:49:43 2023

@author: ijvaillant
"""

import rdkit
from rdkit import Chem

def functional_group_exists(smiles, functional_group):
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