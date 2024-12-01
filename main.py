import pandas as pd 
import numpy as np

data = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18],
    'Address': ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai'],

}

df = pd.DataFrame(data)
print(df)
