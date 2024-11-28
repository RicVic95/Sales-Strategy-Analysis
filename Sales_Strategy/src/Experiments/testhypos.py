import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns   
import numpy as np
import pingouin 

# Read in the data 
sales = pd.read_csv('../../data/interim/sales_data_HT.csv')
sales.head()
sales.drop(columns=['Unnamed: 0'], inplace=True)
sales.set_index('customer_id', inplace=True)
sales['sales_method'] = sales['sales_method'].astype('category') # Convert to category type

# ---------------------------------------- #
#       Hypothesis Testing                 #
# ---------------------------------------- #

# Hypothesis: There is a significan difference in revenue between sales methods 
# Null Hypothesis: There is no significant difference in revenue between sales methods

# Kruskal-Wallis Test 
pingouin.kruskal(data=sales, dv='revenue', between='sales_method')
pingouin.kruskal(data=sales, dv='revenue_per_sale', between='sales_method')

# Both p-values are less than 0.05, so we reject the null hypothesis. 
# There's strong evidence to suggest that there is a significant difference in revenue
# and revenue per sale between sales methods.

# Post-hoc pairwise comparisons
# Dunn's test

dunn_revenue = pingouin.pairwise_tests(data=sales, dv='revenue', 
                                       between='sales_method', padjust='bonf')

dunn_rev_per_sale = pingouin.pairwise_tests(data=sales, dv='revenue_per_sale', 
                                            between='sales_method', padjust='bonf')

# all pairwise comparisons show statistically significant differences 
# in revenue and revenue per sale between sales methods since p-values 
# are less than 0.05 after Bonferroni correction.

# ---------------------------------------- #
# Which sales method is the best?          #
# ---------------------------------------- #

# Average revenue per transaction 


# Calculate average transactions per week by sales method
sales_by_week = sales.groupby(['week', 'sales_method']).agg(total_transactions=('revenue', 'count'),
                                                            total_revenue=('revenue', 'sum')).round(2).reset_index()

sales_by_week['avg_revenue_per_transaction'] = sales_by_week['total_revenue'] / sales_by_week['total_transactions']

sns.barplot(data=sales_by_week, x='week', y='revenue', hue='sales_method')
sns.lineplot(data=sales_by_week, x='week', y='revenue', hue='sales_method')

sns.lineplot(data=sales_by_week, x='week', y='total_revenue', hue='sales_method')
sns.lineplot(data=sales_by_week, x='week', y='avg_revenue_per_transaction', hue='sales_method')
sns.lineplot(data=sales_by_week, x='week', y='total_transactions', hue='sales_method')

sales_by_week.groupby('sales_method').agg(avg_weekly_transactions=('total_transactions', 'mean'),
                                            avg_weekly_revenue=('total_revenue', 'mean')).round(2
                                                                                                
table = sales.groupby('sales_method').agg(total_transactions=('revenue', 'count'), 
                                  total_revenue=('revenue', 'sum')).round(2)    
table['avg_revenue_per_transaction'] = table['total_revenue'] / table['total_transactions']                                                                                            