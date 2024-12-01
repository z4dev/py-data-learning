import pandas as pd 
import numpy as np

data = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18],
    'Address': ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai'],

}

df = pd.DataFrame(data)
#as it return the indexes which i do not need to  of the dataframe 
# df.to_csv('data.csv' , index = False)
# df.to_excel('data.xlsx' , index = False)
print(df)
