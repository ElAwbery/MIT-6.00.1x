#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:15:17 2018

@author: ElAwbery
"""

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        print("1minIndx:", minIndx,"minVal:", minVal, "j:", j)
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
        print("2minIndx:", minIndx,"minVal:", minVal, "j:", j)
        
    print(L)
            
            
ListTest = [7, 4, 3, 6, 8, 8, 0, 1, 3]

