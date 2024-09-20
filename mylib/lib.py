"""
 library file
"""
import pandas as pd
import matplotlib.pyplot as plt

# Data Loading
def load_dataset(csv):
    df = pd.read_csv(csv)
    return df

# Data Stats
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
    plt.savefig("plot_from_data.png")
    


