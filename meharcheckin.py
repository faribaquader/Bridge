import matplotlib.pyplot as plt
import numpy as np


AGES = ["18-25", "25-35", "45-55", "55-65", "65-80"]
YES = [200, 100, 20, 15, 50]
NO = [12, 10, 100, 75, 45]

def graph(x, y, z):
    """Creates a graph which compared individual's vaccine consent and 
    their ages.
    
    Args: 
        x (list of str): the age ranges on the x-axis
        
        y (list of int/float): the number of individuals who said they would
        get the COVID-19 vaccine.
        
        z (list of int/float): the number of individuals who said they would 
        not get the COVID-19 vaccine. 
    
    Side effects:
        Production of a bar graph that shows the ages and their consent. 
        
    Sources: 
    https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib
    -in-python/ : lines 34-38, allowed me to develop the code for 
    production of two bars for each x-axis label, using two sets of data. 
    
    https://datatofish.com/bar-chart-python-matplotlib/ : lines 39-43, allowed
    me to learn about the different methods you can use from the plt class to 
    edit the bar graph. """
        
    n = 5
    xaxis = np.arange(n)
    plt.bar(xaxis - 0.2, y, 0.4, label = "Yes")
    plt.bar(xaxis + 0.2, z, 0.4, label = "No")
    plt.xticks(xaxis, AGES)
    plt.title("Ages vs. Vaccine Consent")
    plt.xlabel("Ages")
    plt.ylabel("Vaccine Consent")
    plt.legend()
    plt.show()
    
final = graph(AGES, YES, NO)
print(final)