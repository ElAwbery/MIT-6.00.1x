#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 14:24:19 2018

@author: Charlie
"""

def search(L, e):
    for i in range(len(L)):
        print(i)
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False




def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print(i, size-i-1)
        if L[size-i-1] == e:
            print ("L[size-i-1=", L[size-i-1])
            return True
        if L[i] < e:
            return False
    return False





def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    ops = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
                ops +=1
    print("Final L: ", L, "ops =", ops)
    
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    ops = 0
    for i in range(len(L)):
        print("starting next outer loop now. L=", L)
        ops += 1
        for j in range(len(L)):
            print ("i=", L[i], "j=", L[j])
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
                ops+=1
    print("Final L: ", L, "ops =", ops)
    
    
    

L = [102, 65, 4, 6, 7, 2, 85, 762, 0, 3, 57, 12, 97, 2, 5, 7982, 1, 12, 46, 654, 5, 4, 3, 2, 1, 0]

P = [102, 65]

Q = [102, 3, 56]

R=[3, 8, 65, 15]





