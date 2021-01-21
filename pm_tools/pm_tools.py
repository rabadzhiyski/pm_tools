# -*- coding: utf-8 -*-
"""
This is a script file for calculating the most
popular project management metrics.
"""
import math

# Add general Class

class Metrics:
    """
    Metrics class for calculating the main project management
    functions.
    
    Attributes:
        ppc (float) = planned percent completed 
        budget (int) = the budget of the project in int
        apc (float) = actual percent completed of the project
        ac (int)= actual cost of the project 
    
    """
    
    def __init__(self, ppc, budget, apc, ac):
        self.ppc = ppc
        self.budget = budget
        self.apc = apc
        self.ac = ac
        
# planned_value = planned % complete * budget
    def planned_value(self, ppc, budget):
        
        return ppc * budget
    
# earned_value = actual % complete * budget
    def earned_value(self, ac, budget):
       
        return ac * budget
       
# schedule_variance = earned_value - planned_value
    def schedule_variance(self):
       
        ev = self.ac * self.budget
        pv = self.ppc * self.budget
       
        return ev * pv
           
# cost_variance = earned_value - actual cost
    def cost_variance(self):
        
        ev = self.ac * self.budget
        
        return ev - self.ac
        
# schedule_perf_index = earned_value / planned_value
    def schedule_perf_index(self):
        
        ev = self.ac * self.budget
        pv = self.ppc * self.budget
        
        return ev / pv
    
# cost_perf_index = earned_value / actual cost
    def cost_perf_index(self):
        
        ev = self.ac * self.budget
        
        return ev / self.ac
    
# create one example object per milestone

# calculate the respective function