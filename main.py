import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


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

df = pd.read_csv('data.csv')

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


#----- PART two ------

#?df.describe()  #it will return the statistical information about the dataframe

#?df.hist()  #it will return the histogram of the dataframe
#*btw : hostogram is the graphical representation of the frequency of the data
#the y-axis represents the frequency of the data ( rows of the dataframe)
#the x-axis represents the data points (columns of the dataframe)



#histogram for one column
#?df['Age'].hist(bins=2)  #it will return the histogram of the Age column
#?bins=2 means the number of bins you want to see in the histogram


# addresses_count = df['Address'].value_counts()
# #todoREADING : it will return the addresses and the number of times they are repeated in the dataframe
# age_count = df['Age'].value_counts()
# #todoREADING : it will return the ages and the number of times they are repeated in the dataframe

# print(df['Address'].value_counts()[-1:])
# print(df['Address'].value_counts()['Gaza'])


# plt.bar(age_count.index , age_count.values , color='red' , alpha=0.5) 
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.title('Age Distribution')

# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the dataset
# df = pd.read_excel('zsalam.xls')

# # Ensure 'VoucherDate' is in datetime format
# df['VoucherDate'] = pd.to_datetime(df['VoucherDate'])

# # Extract Hour, Month, and Day from 'VoucherDate'
# df['Hour'] = df['VoucherDate'].dt.hour
# df['Month'] = df['VoucherDate'].dt.month
# df['Day'] = df['VoucherDate'].dt.day

# # Define time periods for categorization
# conditions = [
#     (df['Hour'] >= 2) & (df['Hour'] < 8),      # 2AM to 8AM
#     (df['Hour'] >= 8) & (df['Hour'] < 14),     # 8AM to 2PM
#     (df['Hour'] >= 14) & (df['Hour'] < 20),    # 2PM to 8PM
#     (df['Hour'] >= 20) & (df['Hour'] < 24)     # 8PM to 12AM
# ]

# choices = ['2AM-8AM', '8AM-2PM', '2PM-8PM', '8PM-12AM']

# # Apply the conditions to create a 'Period' column
# df['Period'] = np.select(conditions, choices, default='Unknown')

# # Columns to exclude (drop them for analysis)
# columns_to_exclude = ['CustomerNumber', 'Frst_Name', 'S_Name', 'ItemName', 'EItemName', 'ItemCategoryName', 'VoucherDate']
# df_filtered = df.drop(columns=columns_to_exclude)

# # Iterate through each unique month and plot separate histograms
# for month in df['Month'].unique():
#     # Filter data for the specific month
#     month_data = df_filtered[df['Month'] == month]
    
#     # Ensure there's data for the month
#     if month_data.empty:
#         print(f"No data for Month {month}. Skipping...")
#         continue
    
#     # Split data into time periods
#     morning_data = month_data[month_data['Period'] == '2AM-8AM']
#     afternoon_data = month_data[month_data['Period'] == '8AM-2PM']
#     evening_data = month_data[month_data['Period'] == '2PM-8PM']
#     night_data = month_data[month_data['Period'] == '8PM-12AM']
    
#     # Print basic statistics to inspect data distribution
#     print(f"Month {month}:")
#     print(f"Morning data count: {morning_data['Hour'].count()}")
#     print(f"Afternoon data count: {afternoon_data['Hour'].count()}")
#     print(f"Evening data count: {evening_data['Hour'].count()}")
#     print(f"Night data count: {night_data['Hour'].count()}")
    
#     # Plot histograms for each time period
#     plt.figure(figsize=(10, 8))
#     plt.hist(morning_data['Hour'], bins=np.arange(2, 9, 1), alpha=0.7, label='2AM-8AM', edgecolor='black')
#     plt.hist(afternoon_data['Hour'], bins=np.arange(8, 15, 1), alpha=0.7, label='8AM-2PM', edgecolor='black')
#     plt.hist(evening_data['Hour'], bins=np.arange(14, 21, 1), alpha=0.7, label='2PM-8PM', edgecolor='black')
#     plt.hist(night_data['Hour'], bins=np.arange(20, 25, 1), alpha=0.7, label='8PM-12AM', edgecolor='black')

#     # Set plot titles and labels
#     plt.title(f'Voucher Amounts by Time Period for Month {month}')
#     plt.xlabel('Hour of the Day')
#     plt.ylabel('Frequency')
#     plt.legend()

#     # Rotate x-axis labels for clarity
#     plt.xticks(rotation=45)

#     # Show the plot for this month
#     plt.tight_layout()  # Ensures the layout is adjusted properly
#     plt.show()





