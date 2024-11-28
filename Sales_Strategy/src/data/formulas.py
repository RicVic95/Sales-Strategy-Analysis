import pandas as pd 
import numpy as np 

def number_of_outliers(df, column):
    '''Function to find number of outliers in a column based on IQR.'''
    # Calculate the first (Q1) and third (Q3) quartiles and the IQR
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)  
    IQR = Q3 - Q1
    
    # Calculate the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Find and count the outliers
    n_outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)].shape[0]
    
    return n_outliers


def remove_outliers(df, column): 
    '''Function to remove outliers in a column based on IQR.
    
    Parameters:
    df (pandas.DataFrame): DataFrame to process.
    column (str): The column name to detect and remove outliers from.

    Returns:
    pandas.DataFrame: Cleaned DataFrame without outliers.
    '''
    # Calculate the first (Q1) and third (Q3) quartiles and the IQR
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    # Calculate the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR  
    
    # Filter out rows with outliers in the specified column
    df_clean = df[(df[column] >= lower_bound) & (df[column] <= upper_bound) | df[column].isnull()]
    
    # Optionally, return the number of rows removed
    rows_removed = len(df) - len(df_clean)
    print(f"Rows removed: {rows_removed}")
    
    return df_clean

