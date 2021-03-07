# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:23:07 2021

@author: Aksh
"""

def dna_count(dna):
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    dna = dna_upper
    for letter in dna:
        if letter == "A":
            count_A = count_A + 1
        elif letter == "C":
            count_C = count_C + 1
        elif letter == "G":
            count_G = count_G + 1
        elif letter == "T":
            count_T == count_T + 1
        else:
            print("Invalid input")
    return (count_A, count_C, count_G, count_T)