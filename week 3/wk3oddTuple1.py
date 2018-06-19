# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''

    count = 0
    newTup = ()

    for element in aTup:
        
        if count%2 == 0:
            newTup += (element,)
            count += 1
        else:
            count += 1
            
    return newTup
    
