# -*- coding: utf-8 -*-
"""
This is a script file for getting the inputs for the
project management metrics.

"""

# general class

class Inputs:
    """
    Inputs class for getting the measures for the main project management
    functions.
    
    Attributes:
        ppc (float) = planned percent completed 
        budget (int) = the budget of the project
        apc (float) = actual percent completed of the project
        ac (int)= actual cost of the project 
    
    """
    
    def __init__(self, ppc, budget, apc, ac):
        self.ppc = ppc
        self.budget = budget
        self.apc = apc
        self.ac = ac