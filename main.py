import pandas as pd 
import numpy as np

data = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18],
    'Address': ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai'],

}

# df = pd.DataFrame(data)
#as it return the indexes which i do not need to  of the dataframe 
# df.to_csv('data.csv' , index = False)
# df.to_excel('data.xlsx' , index = False



# df = pd.read_csv('data.csv')
# print(df)

# ---- --- --- ?Methods to use with df(dataframe)
#?df.head()  #it will return the first 5 rows of the dataframe (also we can pass the number of rows we want to see)
#?df.tail()  #it will return the last 5 rows of the dataframe (also we can pass the number of rows we want to see)
#?df.sample()  #it will return the random row from the dataframe (also you can use n= number of rows you want to see randomly)
#<#>
#?frac : Fraction means the percentage of the data you want to see randomly
#?frac = 0.1  #it will return the 10% of the data randomly
#to shuffle the data we can use the sample method
#?df.sample(frac=1)  #it will return the shuffled data , why 1 ? because 1 means 100% of the data
#<#>

#?df.columns  #it will return the columns of the dataframe
#?df.index  #it will return the indexes of the dataframe
#?df.shape  #it will return the shape of the dataframe (rows, columns) #it will return the tuple
#?df.info()  #it will return the information about the dataframe
#?df.describe()  #it will return the statistical information about the dataframe
#?df.dtypes  #it will return the data types of the columns of the dataframe

#use case of the sample method
#-> imagine that you have a dataset of 1000 rows and you want to see 10% of the data randomly
#-> you can use the sample method to see the 10% of the data randomly


#-> df.sample(frac=0.1)  #it will return the 10% of the data randomly


# You are referring to "franc" as a concept related to percentages or calculations with numbers, possibly related to returning a 
# percentage or a proportion from a sample of data, such as 10% of a dataset.

# df = pd.read_csv('data.csv')
# shuffled_data = df.sample(frac=1) #it will return the shuffled data


#cut_off = int(0.7 * len(shuffled_data))
#train_df = shuffled_data[:cut_off] #it will return the 70% of the data
#test_df = shuffled_data[cut_off:] #it will return the 30% of the data


#-----




