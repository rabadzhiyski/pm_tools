from .General import Inputs

"""
This is a script file for calculating the most
popular project management metrics.

"""

class Metrics(Inputs):
    
    """
    Metrics class for calculating the measures for the main project management
    functions.
    
    Attributes:
        ppc (float) = planned percent completed 
        budget (int) = the budget of the project in int
        apc (float) = actual percent completed of the project
        ac (int)= actual cost of the project 
    
    """
    
    def __init__(self, ppc, budget, apc, ac):
        
        Inputs.__init__(self, ppc, budget, apc, ac)

# planned_value = planned % complete * budget
    def planned_value(self):
        
        """
        Function to calculate planned value.
                
        Args:
            None
        
        Returns:
            int: planned_value = planned % complete * budget
            
        """
        
        return self.ppc * self.budget
    
# earned_value = actual % complete * budget
    def earned_value(self):
        
        """
        Function to calculate earned value.
                
        Args:
            None
        
        Returns:
            int: earned_value = actual % complete * budget
            
        """ 
       
        return self.apc * self.budget
       
# schedule_variance = earned_value - planned_value
    def schedule_variance(self):
        
        """
        Function to calculate schedule variance.
                
        Args:
            None
        
        Returns:
            int: earned value - planned value
            
        """
       
        ev = self.apc * self.budget
        pv = self.ppc * self.budget
       
        return ev - pv
           
# cost_variance = earned_value - actual cost
    def cost_variance(self):
        
        """
        Function to calculate cost variance.
                
        Args:
            None
        
        Returns:
            int: earned value - actual cost
            
        """
        
        ev = self.apc * self.budget
        
        return ev - self.ac
        
# schedule_perf_index = earned_value / planned_value
    def schedule_perf_index(self):
        
        """
        Function to calculate schedule performance index.
                
        Args:
            None
        
        Returns:
            int: earned value / planned value
            
        """
        
        ev = self.apc * self.budget
        pv = self.ppc * self.budget
        
        return ev / pv
    
# cost_perf_index = earned_value / actual cost
    def cost_perf_index(self):
        
        """
        Function to calculate cost performance index.
                
        Args:
            None
        
        Returns:
            int: earned value / actual cost
            
        """
        
        ev = self.apc * self.budget
        
        return ev / self.ac
