"""
Module parses and formats data correctly before analysis. It uses Pandas and Pandas dataframes for this.
See https://pandas.pydata.org/ for more information.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pprint

def create_dataframe(csv_file):
    """
    Function for creating a panda dataframe from a csv file where the top row
    contains labels. Removes rows with errors (i.e. NaN-values)
    
    Args:
        csv_file (File): The filepath to the csv file you wish to base the dataframe on
    
    Returns:
        dataframe: The correctly formatted dataframe
    """
    
    labels = open(csv_file).read(0)

    dataframe = pd.read_csv(csv_file, na_values='NaN')
    dataframe = dataframe.dropna()

    return dataframe

def get_dataframes(csv_file, features=None):
    """
    Function splits the dataframe 80/20 training data/control data.
    
    Args:
        csv_file (File: The filepath to the csv file you wish to base the dataframe on
        features (List, optional): List of features that should be included in the dataframe. Defaults to None.
    
    Returns:
        dataframe: The dataframe with training data. Approx. 80% of the original dataset
                    The dataframe with control data. Applrox. 20% of the original dataset
    """

    dataframe = create_dataframe(csv_file)

    if features == None:
        pass
    else:
        for column_name in list(dataframe.columns.values):
            if column_name not in features:
                del dataframe[column_name]

    m = np.random.rand(len(dataframe)) < 0.8 #splits the dataset randomly 80/20

    training_data = dataframe[m]
    training_data = training_data.replace(['pos'], 1).replace(['neg'], 0)
    control_data = dataframe[~m]
    control_data = control_data.replace(['pos'], 1).replace(['neg'], 0)


    return training_data, control_data

def scatter_plot(x_axis_data, y_axis_data, colors="green"):
    """
    Function creates a dataframe and displays a scatter plot based on two values.
    
    Args:
        x_axis_data (dataframe): The dataframe or array with the x-axis values
        y_axis_data (dataframe): The dataframe or array with the y-axis values 
        colors (str, optional): Color of the dots in the graph. Defaults to "green".
    """
    
    area = np.pi*3

    #Plot data
    plt.scatter(x_axis_data, y_axis_data, s=area, c=colors, alpha=0.5)
    plt.title('Scatter plot of model')
    plt.show()

if __name__ == "__main__":
    training_data, control_data = get_dataframes(sys.argv[1])
    scatter_plot(training_data['age'], training_data['pregnant'])
