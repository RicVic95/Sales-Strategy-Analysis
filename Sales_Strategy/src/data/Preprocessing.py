import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

# Read in the data 
sales_df = pd.read_csv('../../data/raw/product_sales.csv')

# Explore Data
sales_df.head()

# Check column types 
sales_df.dtypes

# -----------------------------------------------------# 
#                  Data Preprocessing                  #
# -----------------------------------------------------# 


# Check for unique values in sales_method column
sales_df['sales_method'].unique()

# homogeneate strings to display only the three categories
sales_df['sales_method'] = sales_df['sales_method'].str.lower()
sales_df['sales_method'] = sales_df['sales_method'].replace('em + call', 'email + call')

# Adjust for appropriate data type
sales_df['sales_method'] = sales_df['sales_method'].astype('category')


# ----------------- Outliers -----------------#

# Check for outliers 
sns.boxplot(data=sales_df, y='revenue', x='sales_method', hue='sales_method')
plt.title('Revenue by Sales Method')
plt.savefig('../../reports/figures/revenue_by_sales_method.png')

# Find number of outliers per sales method 
from formulas import number_of_outliers

for method in sales_df['sales_method'].unique(): 
    df = sales_df[sales_df['sales_method'] == method]
    n_outliers = number_of_outliers(df,'revenue')
    print(f'\n Number of outliers for {method}: ', n_outliers)
  
# Remove outliers for the revenue column
from formulas import remove_outliers

sales_call_no_outliers = remove_outliers(sales_df[sales_df['sales_method'] == 'call'], 'revenue') 
sales_email_no_outliers = remove_outliers(sales_df[sales_df['sales_method'] == 'email'], 'revenue')
sales_email_call_no_outliers = remove_outliers(sales_df[sales_df['sales_method'] == 'email + call'], 'revenue')

# Concatenate the dataframes
sales_no_outliers = pd.concat([sales_call_no_outliers, sales_email_no_outliers, sales_email_call_no_outliers])

# Verify results 
len(sales_df) - len(sales_no_outliers) # Number of rows removed

# ----------------- Missing Values -----------------#

# Check for missing values 
sales_no_outliers.isnull().sum()

# Check missing values per category 
missing_df = sales_no_outliers.groupby('sales_method')[['customer_id','revenue']].count()
missing_df['missing_percent'] = 1 - (missing_df['revenue'] / missing_df['customer_id'])

# Separate missing values by sales method
missing_call = sales_no_outliers[sales_no_outliers['sales_method'] == 'call']
missing_email = sales_no_outliers[sales_no_outliers['sales_method'] == 'email']
missing_email_call = sales_no_outliers[sales_no_outliers['sales_method'] == 'email + call']

# Remove missing values for 'call' and 'email' sales methods
missing_call_clean = missing_call.dropna()
missing_email_clean = missing_email.dropna()

# Impute missing values for 'email + call' sales method 
n = missing_email_call.groupby('nb_sold').agg({'revenue':'mean'})

# Impute missing values based on the 'nb_sold' means 
for row in missing_email_call.iterrows(): 
    if np.isnan(row[1]['revenue']): 
        mean_revenue = missing_email_call_means.loc[row[1]['nb_sold']]['revenue']
        missing_email_call.loc[row[0], 'revenue'] = mean_revenue   

# Concatenate the dataframes with removals and imputations 
sales_final = pd.concat([missing_call_clean, missing_email_clean, missing_email_call])




# Save the cleaned data 
sales_final.to_csv('../../data/processed/sales_data_clean.csv', index=False)

sns.boxplot(data=sales_final, y='revenue', x='sales_method', hue='sales_method')
plt.title('Revenue by Sales Method (no outliers)')
plt.savefig('../../reports/figures/revenue_by_sales_method_no_outliers.png')


