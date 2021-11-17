import pandas as pd

def dataframe(file):
    """ creates dataframe.
    Args: 
        file(file): name of file
    Side effects:
        prints the dataframe
        
    source:
        https://www.easytweaks.com/pandas-read-text-files/  
    """
    df = pd.read_csv(file, delimiter =' ', names =['name', 'age', 'immunocompromised', 'job'], index_col = False)
    final = df.head()
    print(final)

data = dataframe("fariba.txt")
print(data)   
