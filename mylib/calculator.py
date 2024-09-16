"""
 library file
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset="https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"

def load_dataset():
    df = pd.read_csv(dataset)
    return df

def grab_mean(df, col):
    return df[col].mean()

def grab_median(df, col):
    return df[col].median()

def grab_max(df, col):
    return df[col].max()

def grab_std(df, col):
    return df[col].std()

def generate_descriptive_statistics(data):
    des_stat = data.describe()
    return des_stat

def create_histogram(df, col):
    plt.hist(df[col], bins=30, edgecolor='black')  # Create histogram with 30 bins
    plt.title(f'Histogram of {col}') 
    plt.xlabel(col)
    plt.ylabel('Frequency') 
    plt.grid(True)  #Add grid lines
    plt.show() 
    


