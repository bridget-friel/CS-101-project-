# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:33:29 2021

@author: Aksh
"""


def hamming_distance(dna1, dna2):
    dna1 = dna1.upper
    dna2 = dna2.upper
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
            continue
        else:
            distance = distance + 1
    return distance