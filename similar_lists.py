# Made by Luboš Kulhan | alias: Adam Kaiser

import math as m
def similar_lists(x,y):
    try:
        if len(x) == 0 or len(y) == 0:
            return "ERROR - list is empty."
        if len(x) > len(y):
            list_lenght = len(y)
            print("WARNING - lists are not the same lenght; first list is longer.")
        elif len(x) < len(y):
            list_lenght = len(x)
            print("WARNING - lists are not the same lenght; second list is longer.")
        else:
            list_lenght = len(x)
        i = 0
        while i < list_lenght:
            podobnost = m.isclose(x[i],y[i],abs_tol=0.1)
            if not podobnost:
                podobnost = False
                break
            i += 1
        return podobnost
    except TypeError:
        return "ERROR - list must contain only int or float."

# Test - uncomment for testing
#list_1 = [1,-2.09]
#list_2 = [1.01000001,-1.9999994]
#print(similar_lists(list_1,list_2))