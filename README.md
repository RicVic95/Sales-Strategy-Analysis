# Hypothesis-Driven Sales Strategy Optimization
---
# Executive Summary

## Objective
The goal of this project was to evaluate and compare sales methods (Call, Email, and Email + Call) to identify the most effective strategies for maximizing revenue and profitability. By analyzing transactional data, the project aimed to recommend optimal sales approaches for scalable revenue growth and efficient resource allocation.

## Approach
The analysis followed a structured process, including data validation, exploratory data analysis (EDA), statistical testing, and efficiency evaluation. Key steps included:

- **Data Cleaning**: Addressing missing values, removing outliers, and ensuring dataset integrity.
- **Exploratory Analysis**: Identifying trends in sales performance over time, differences across customer groups, and revenue drivers by state.
- **Statistical Testing**: Using non-parametric tests (Kruskal-Wallis and pairwise comparisons) to determine significant differences in revenue distributions across sales methods.
- **Efficiency Metrics**: Estimating costs per transaction and profit margins to compare the scalability and efficiency of each method.

Key considerations included:
- Identifying the most scalable sales method for maximizing total revenue.
- Evaluating transaction efficiency by analyzing average revenue and profit margins.
- Highlighting opportunities for optimizing high-revenue but resource-intensive methods.
- Recommending data-driven strategies for sustained growth.

## Results
The analysis revealed significant differences between the three sales methods, with key findings summarized below:

- **Email**: The most scalable method, generating the highest total revenue ($660,475.80) and transactions (6,834). It had the lowest cost per transaction ($2.00) and a profit margin of 36%, making it the most cost-effective strategy for maximizing overall revenue.
- **Email + Call**: The most efficient per transaction, with the highest average revenue per sale ($184.23) and a 42% profit margin. However, its lower transaction volume (2,572) limits scalability.
- **Call**: The least favorable method, with the lowest total revenue ($226,668.99), average revenue per transaction ($47.54), and profit margin (18%).

Statistical tests confirmed that revenue distributions differed significantly across methods, emphasizing the importance of strategic prioritization. Additionally, states like California, Texas, and New York emerged as key revenue drivers, collectively accounting for **over one quarter of total revenue**.

### Recommendations
1. **Scale the Email Method**:
   - Focus on scaling email campaigns further to leverage its scalability and cost-effectiveness.
   - Sustain performance through strategies like A/B testing, customer segmentation, and retention campaigns to address declining transaction volumes over time.

2. **Optimize Email + Call for High-Value Opportunities**:
   - Use this method strategically for premium customers or high-value products, where maximizing revenue per transaction is critical.
   - Streamline operations to reduce resource demands and increase transaction volume.

3. **Reduce the Call Method to Specific Situations**:
   - Limit the use of the call method to scenarios where email or email + call campaigns are not viable, such as targeting specific customer demographics or regions with limited accessibility.
   - Focus on optimizing call campaigns for efficiency and profitability when deployed.

4. **Monitor Revenue Metrics**:
   - Track weekly revenue and transaction volumes for each sales method to identify performance trends.
   - Establish performance thresholds to ensure resource allocation aligns with business goals.

5. **Target Key States**:
   - Focus sales and marketing efforts on California, Texas, and New York to capitalize on their high revenue contributions.

6. **Explore Additional Sales Channels**:
   - Investigate emerging sales channels such as SMS marketing, social media outreach, or live chat support.
   - Evaluate their impacts on revenue to uncover new opportunities for growth and diversification.
   - Adopt an omnichannel approach by integrating multiple methods to maximize scalability and customer engagement, ensuring a balanced and comprehensive strategy.

## Key Impact
Implementing these recommendations has the potential to significantly enhance revenue and profitability while improving resource efficiency. Specifically:

- Scaling the Email method could sustain high transaction volumes and total revenue growth.
- Strategically deploying Email + Call could maximize returns from high-value customers.
- Reducing reliance on the Call method would free up resources for more efficient strategies.
- Targeting top-performing states could amplify overall revenue by focusing efforts where they yield the highest returns.
- Exploring additional sales channels and adopting an omnichannel approach will allow the business to stay agile, capture new opportunities, and maintain competitive advantage in evolving markets.

By adopting a data-driven approach to sales strategy, the business can align its operational efforts with its strategic goal of maximizing revenue growth and resource optimization.

--- 

# Introduction

Sales methods play a critical role in driving business growth and maximizing revenue. With evolving customer behaviors and emerging communication channels, it has become essential for businesses to evaluate the effectiveness of their sales strategies to ensure optimal resource allocation and sustained profitability.

This project aims to analyze and compare the performance of three primary sales methods—Call, Email, and Email + Call—using a structured data-driven approach. By understanding how these methods impact key metrics like revenue, transaction volume, and efficiency, the project provides actionable recommendations to refine the company’s sales strategy and adapt to changing market dynamics.

The findings presented in this report are intended to guide decision-making, identify areas of opportunity, and ensure the business remains competitive in an increasingly customer-centric landscape.

# Data Validation

The dataset contains 15,000 rows and 8 columns before cleaning and validation. I have validated all the columns against the criteria in the dataset table: 

| **Column Name**       | **Description**                                                                 | **Changes Performed**                                                                                                              |
|------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `week`                | Week of the sale, counted as weeks since product launch.                         | No changes required; data was already valid and within the expected range (1–6).                                                 |
| `sales_method`        | Sales method used for the customer (Call, Email, Email + Call).                  | Homogenized string cases, standardized categories to include only `call`, `email`, and `email + call`.                           |
| `customer_id`         | Unique identifier for the customer.                                              | Verified uniqueness; no duplicates detected.                                                                                     |
| `nb_sold`             | Number of products sold per transaction (7–16).                                  | No changes required; data was valid.                      |
| `revenue`             | Total revenue from the sale, rounded to 2 decimal places.                        | - Removed 99 outliers based on IQR method.<br> - Handled missing values:<br>   - Dropped for `call` (3.7%) and `email` (7.4%).<br>   - Imputed for `email + call` (13.6%) using average revenue grouped by `nb_sold`. |
| `years_as_customer`   | Number of years the customer has been buying from the company (founded in 1984). | Removed 2 customers with `years_as_customer` > 40 due to data errors exceeding the company's existence.                          |
| `nb_site_visits`      | Number of times the customer visited the website in the last 6 months.           | No changes required; data was valid and within expected ranges.                                                                  |
| `state`               | Customer's shipping location (e.g., California, Texas).                         | No changes required; verified 50 unique values, matching the 50 U.S. states.                                                     |

After data validation, the dataset contains 14,174 rows and 9 columns. The data cleaning process addressed key issues to ensure the reliability of the analysis. Notably, outliers were removed from the revenue column to minimize the risk of skewed results, and missing values in the email + call category were imputed to preserve data integrity for this high-value sales method. These steps were critical in preparing the dataset for meaningful comparisons and ensuring robust insights across the different sales methods.

# Exploratory Data Analysis
## What is the relationship between numerical variables? 

To explore relationships between key variables, a correlation heatmap was generated. Understanding these relationships is critical for identifying factors that drive revenue and sales volume. For instance, examining the strength of correlations can help determine whether increasing website visits might lead to higher sales or whether time-based trends suggest opportunities for optimizing marketing campaign timing.

The heatmap below visualises the correlation between key variables (revenue, nb_sold, week, etc): 

The positive correlation (r = 0.72) between revenue and nb_sold aligns with expectations, as higher sales volumes typically lead to greater revenue. The stronger correlation (r = 0.81) between nb_sold and week suggests a potential time-based trend, possibly driven by seasonal effects or the impact of marketing campaigns over time. This indicates that sales volume may be influenced by temporal factors, which could be leveraged to optimize future campaigns. Additionally, the mild correlation between nb_sold and nb_site_visits suggests that website engagement plays a role, albeit not a dominant one, in driving sales volume.

<div align='center'> 
    <img src= 'Sales_Strategy/reports/figures/correlation_heatmap.png' alt='Correlation' width=500> 
</div> 

## How have sales performed over the last 6 weeks? 

The graph below shows the cumulative revenue generated by each of the sales methods, indicating that 'email' has provided the highest revenue across all three. However, after the first 3 weeks, we can see a noticeable increase in revenue generated by the 'email + call' campaign. The worst performing method was 'call', which has the lowest revenue across all three categories. 

<div align='center'> 
    <img src= 'Sales_Strategy/reports/figures/cumulative_revenue_by_sales_method.png' width=600> 
</div>    

While these numbers may appear to indicate that 'email' is the best sales method when it comes to revenue, it's important to note that the dataset contains a vastly different number of transactions for each sales category. There are a total of 4,768 transactions for 'call', 6,834 for 'email' and 2572 for 'email + call'. While it is expected that the 'email' method has the highest cummulative revenue, it can be explained by the considerably higher number of transactions, and not necessarily suggest that it is the most profitable.

The boxplot below shows the distribution of revenue per sales method, indicating that, while there is a higher variability of revenue for the 'email + call' method, average values indicate that it holds higher returns per transactions, on average. 

<p align='center'> 
    <img src= 'Sales_Strategy/reports/figures/revenue_by_sales_method_no_outliers.png' width=600> 
</p>    
 

## Performance over time

The line plot on the left shows the average revenue generated by each transaction, over the last 6 weeks. We can see an overall increase for each sales method, this is in line with the figure presented before, which suggests that 'email + call' has the highest profitability per transaction. 

On the other hand, the right-side plot shows the number of transactions by sales method for each week. We can see a considerable decrease in the number of transactions for 'email' (from 2626 transactions on week 1 to 99 only on week 6), a minor decrease in number of transactions for the 'call' method (from 740 on week 1 to 415 on week 6) and a noticeable increase for the 'email + call' method (from 148 on week 1 to 583 on week 6)

<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin: auto;">
  <img src="Sales_Strategy/reports/figures/avg_revenue_by_week.png" alt="Revenue by week" width="49%" style="margin-right: 10px;">
  <img src="Sales_Strategy/reports/figures/transactions_by_week.png" alt="Transactions by week" width="49%">
</div>

## Is there a difference across customer groups? 
 
We'll focus on revenue as our metric for comparison. We segmented customers based on their tenure into four different categories: New (0-2 years), Growing (3-10 years), Established (11-20 years) and Loyal (21-39 years). The bar plot below shows the number of customers belonging to each of the categories. 

<div align='center'> 
    <img src= 'Sales_Strategy/reports/figures/n_customers_per_group.png' width=600> 
</div>    

It is evident that the most common customer group is 'Growing' and 'New'. In terms of average revenue generated from each of the groups, it is possible to see a negative correlation (albeit negligible) between average revenue and tenure. That is, the bigger the tenure, the lower the average revenue. Differences are minor, however, and further analysis would need to be made to determine if there is a statistically significant difference. 

### Can we notice a difference revenue between customer groups, when combined with sales methods?

The table below shows the average revenue for each of the sales methods, divided by their customer groups: 


| tenure_group       | sales_method   | average_revenue |
|--------------------|----------------|-----------------|
| 0-2 (New)         | call           | 48.254291       |
|                   | email          | 97.232362       |
|                   | email + call   | 186.996289      |
| 3-10 (Growing)    | call           | 47.147525       |
|                   | email          | 96.438521       |
|                   | email + call   | 183.190387      |
| 11-20 (Established) | call         | 46.313134       |
|                   | email          | 95.081310       |
|                   | email + call   | 178.714100      |
| 21-39 (Loyal)     | call           | 45.824048       |
|                   | email          | 94.909375       |
|                   | email + call   | 176.595322      |


These findings are in line with what we mentioned before. Differences across average revenue are very minor and, in fact, highest average revenue can be seen by the two most common customer groups. 

### Where are customers coming from? 

The barplot below shows the top 10 States by their sales revenue (left axis) and their sales count (right axis) . California, Texas and New York represent the top 3, together represent almost 27% of the total revenue of the business. 

<div align='center'> 
    <img src= 'Sales_Strategy/reports/figures/top_10_states_by_revenue_and_sales.png' width=600> 
</div>   

## Key findings from Exploratory Data Analysis

Overall Spread: 
- **Email + call** generates the highest average revenue per transaction but has the lowest transaction volume.
- **Email** generates the highest total revenue and transactions. Suggesting it might be the most scalable. 

Revenue Over Time: 
- Average revenue per transaction increases over time for all methods, while transaction volume declines for 'email' and 'call'. 

Differences across customers:
- There seems to be little to no difference between average revenue across tenure groups, even when separated by each of the sales methods. 
- California, Texas and New York represent the best performing states by sales count and revenue. Combined they can account for more than one quarter of the total revenue of the company.

# Statistical Analysis

The purpose of this section is to investigate if there is a statistically significant difference in average revenue generation for each of the sales methods. If so, we can later determine which of these is the best to use as we move forward. 

## Is there a difference in revenue between sales methods? 

### Tests for normality 

First, we need to understand if our data is normally distributed. The table below was calculated by performing Shapiro-Wilk tests for normality for each of the sales methods' 'revenue' column. 


| sales_method   | p_value         | statistic | result                    |
|----------------|-----------------|-----------|---------------------------|
| call           | 1.342326e-39    | 0.942515  | Not Normally Distributed  |
| email          | 1.077739e-40    | 0.957479  | Not Normally Distributed  |
| email + call   | 2.332966e-35    | 0.917418  | Not Normally Distributed  |


We can then confirm this results by performing Q-Q plots for each of the sales methods as an additional test for normality: 

<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin: auto;">
  <img src="Sales_Strategy/reports/figures/qq_plot_call_rps.png" width="32%" style="margin-right: 10px;">
  <img src="Sales_Strategy/reports/figures/qq_plot_email + call_rps.png" width="32%" style="margin-right: 10px;">
  <img src="Sales_Strategy/reports/figures/qq_plot_email_rps.png" alt="Transactions by week" width="32%">
</div>

Since the data isn't normally distributed, we will use non-parametric tests to determine whether there is a statistically significant difference in revenue for each of the sales methods. 

### Hypothesis Testing

We will use Kruskal-Wallis tests to compare the sales methods across the groups in the data set, using the following hypothesis: 

- Null Hypothesis: There is no difference in the distributions of revenue across the sales methods.
- Alternative Hypothesis: There is a difference in the distributions of revenue across the sales methods.
- Alpha: 0.05

#### Kruskal-Wallis Test Results


| **Source**      | **ddof1** | **H**           | **p-unc** |
|-----------------|-----------|-----------------|-----------|
| sales_method    | 2         | 11957.12        | 0.0       |


The Kruskal-Wallis test revealed significant differences in revenue distributions across the three sales methods, with an H-statistic of 11,957.12 and a p-value of 0.0, well below the 0.05 threshold. This allows us to confidently reject the null hypothesis, confirming that the choice of sales method impacts revenue. These results suggest that businesses must prioritize sales methods based on their revenue goals. For instance, methods like email + call, which showed higher average revenue per transaction, may be suited for high-value customers, while methods like email, with higher scalability, are better for maximizing total revenue.

#### Post-hoc pairwise comparisons 

To further explore which specific pairs of sales methods were significantly different, we conducted a post-hoc analysis using pairwise comparisons: 

| Contrast          | A       | B           | Paired | Parametric | T-statistic   | df              | Alternative | p-value | p-corr | p-adjust | BF10  | Hedges' g   |
|-------------------|---------|-------------|--------|------------|---------------|-----------------|-------------|---------|--------|----------|-------|-------------|
| sales_method      | call    | email       | False  | True       | -277.95       | 11303.13        | two-sided   | 0.0     | 0.0    | bonf     | inf   | -5.064      |
| sales_method      | call    | email + call| False  | True       | -232.81       | 2812.37         | two-sided   | 0.0     | 0.0    | bonf     | inf   | -7.366      |
| sales_method      | email   | email + call| False  | True       | -149.05       | 2822.69         | two-sided   | 0.0     | 0.0    | bonf     | inf   | -4.969      |

#### Conclusion

The pairwise comparisons between the sales methods (call, email, and email + call) reveal statistically significant differences in revenue across all pairs. The T-statistics are negative, indicating that for each comparison, the first sales method (A) generally has lower revenue than the second (B). The p-values for all comparisons are 0.0, confirming these differences are highly significant. The effect sizes, as measured by Hedges' g, range from -4.969 to -7.366, suggesting large and meaningful differences between the sales methods.

## Key Findings from Statistical Analysis

- Normality Check: The Shapiro-Wilk tests and Q-Q plots confirmed that the revenue data for each sales method is not normally distributed.
- Kruskal-Wallis Test: The Kruskal-Wallis test revealed significant differences in the distributions of revenue across the sales methods (call, email, email + call), with a p-value of 0.0, allowing us to reject the null hypothesis.
- Post-Hoc Pairwise Comparisons: Further analysis using pairwise comparisons confirmed that all pairs of sales methods (call vs. email, call vs. email + call, email vs. email + call) showed significant differences in revenue. The T-statistics were negative, indicating that the first method (A) generally had lower revenue than the second method (B) in each comparison.

These findings suggest that the choice of sales method (call, email, or email + call) significantly impacts the revenue generated, with substantial differences in performance across the methods.

# Sales method comparison 

Since the test above have shown that there are statistically significant differences in revenue for each of the sales methods, let us now investigate which is the highest performing one. 

The table below shows the average revenue generated per transaction for each of the sales methods: 

| **Sales Method** | **Total Revenue ($)** | **Total Transactions** | **Avg Revenue ($)** | **Avg Items Sold** | **Est. Cost/Transaction ($)** | **Avg Profit Margin (%)** |
|-------------------|-----------------------|-------------------------|---------------------|--------------------|------------------------------|---------------------------|
| Call             | 226,668.99           | 4,768                  | 47.54              | 9.49               | 5.00                         | 18%                       |
| Email            | 660,475.80           | 6,834                  | 96.65              | 9.68               | 2.00                         | 36%                       |
| Email + Call     | 473,828.41           | 2,572                  | 184.23             | 12.23              | 10.00                        | 42%                       |

Introducing estimated costs per transaction and average profit margins provides a clearer understanding of the efficiency of each sales method. These cost estimates are based on reasonable assumptions about resource intensity: call transactions are estimated at $5.00 each due to manual labor requirements, email at $2.00 reflecting automation and scalability, and email + call at $10.00 given its combined resource demands.

Using these estimates, email emerges as the most cost-effective method, with a strong profit margin (36%) and the lowest cost per transaction. Meanwhile, email + call achieves the highest average profit margin (42%) despite higher costs, suggesting its suitability for high-value opportunities. In contrast, call transactions are less efficient, with a relatively high cost and a low profit margin (18%).

These findings underscore the potential for optimizing email for scalability and selectively deploying email + call to maximize profitability.

## Which Method is Better?

- **Email** stands out as the most **scalable method** because it generates the highest number of transactions, leading to the highest total revenue. While its average revenue per transaction is lower than **email + call**, the number of transactions compensates for this difference, making it the most efficient in terms of total revenue generation.
  
- **Email + Call**, on the other hand, is the **most efficient per transaction** with higher revenue per sale and more items sold, but its **lower transaction volume** means it generates less total revenue compared to **email**.

- **Call** is the **least efficient** in terms of both total revenue and average revenue per transaction, making it the least favorable method for maximizing revenue.

### **Conclusion**
If the goal is to **maximize total revenue**, **email** is the best method due to its **higher transaction volume**. However, if **higher revenue per transaction** is prioritized, **email + call** may be the better choice, though it sacrifices scalability. For businesses seeking scalability and higher total revenue, **email** is recommended.

# Final thoughts, recommendations and metrics to follow

## Proposed Metric to follow: Revenue per Week by Sales Method
To evaluate the performance of sales strategies effectively, the business should monitor **weekly revenue** for each sales method. This metric combines the benefit of assessing both the **scalability** (transaction volume) and **efficiency** (revenue per transaction) of each sales method. By analyzing revenue on a weekly basis, trends over time—such as diminishing performance of a sales method or growth in another—can be identified early and acted upon.

### Thresholds for Evaluation:
   - Establish baselines for acceptable weekly revenue per sales method based on historical data.
   - For example:
     - **Email**: Should maintain at least $100,000 per week in total revenue.
     - **Email + Call**: Should maintain at least $75,000 per week to justify its higher resource costs.
     - **Call**: Should maintain at least $35,000 per week or be phased out if the cost-to-revenue ratio becomes unfavorable.

### Initial Metric Values (Based on Current Data):
The table below summarizes average weekly revenue per sales method over the 6-week period:

| **Sales Method** | **Average Weekly Revenue ($)** |
|-------------------|-------------------------------|
| Call             | 37,778.16                     |
| Email            | 110,079.30                    |
| Email + Call     | 78,971.40                     |

These initial values can serve as benchmarks for monitoring weekly performance.

---

## Final Summary and Recommendations

### Key Findings Summary

1. **Email is the Most Scalable**: It generates the highest total revenue ($660,475.80) and transactions (6,834), making it the most effective strategy for maximizing overall revenue.
2. **Email + Call is the Most Efficient**: With the highest average revenue per transaction ($184.23) and average profit margin (42%), it is the most effective method for high-value opportunities, albeit less scalable due to lower transaction volume (2,572).
3. **Call is the Least Favorable**: It generates the lowest total revenue ($226,668.99), has the lowest profit margin (18%), and is the least efficient method.
4. **Significant Differences in Sales Methods**: Statistical tests (Kruskal-Wallis and pairwise comparisons) confirm that revenue distributions differ significantly across sales methods. These findings reinforce the need for strategic prioritization.
5. **Top Performing States**: California, Texas, and New York together account for 27% of total revenue, representing high-priority regions for growth and investment.
6. **Revenue Over Time**: Average revenue per transaction has increased over the six-week period for all sales methods. However, transaction volume for `email` and `call` has declined, while `email + call` has grown.
7. **Minimal Customer Group Differences**: Revenue differences across tenure groups (New, Growing, Established, Loyal) are negligible, even when broken down by sales method.

### Recommendations:
1. **Prioritize the Email Sales Method**:
   - Focus on scaling this method further as it produces the highest revenue and transaction volume. To sustain and enhance the performance of email campaigns, the business should consider the following strategies:
       - **Customer Segmentation**: Personalize campaigns based on customer behavior or preferences, such as tailoring offers to high-value customers or targeting dormant users with reactivation incentives.
       - **Retention Strategies**: Investigate the decline in email transactions over time by analyzing customer engagement patterns. Implement tactics like loyalty programs, limited-time offers, or re-engagement campaigns to maintain interest and activity.

2. **Optimize the Email + Call Method**:
   - Retain this method for high-value customers or premium products where maximizing revenue per transaction is critical.
   - Investigate ways to streamline the process to reduce resource demands and increase transaction volume without sacrificing efficiency.

3.	**Limit the Use of the Call Method**:
    - Given its low efficiency and scalability, this method should be reserved for scenarios where other strategies, such as email or email + call, are not viable options.
    - Reallocate resources toward enhancing the more effective email and email + call strategies.

4. **Monitor Performance Using Revenue Metrics**:
   - Track weekly revenue and transaction volume for each method.
   - Reassess periodically to ensure the chosen strategies continue to align with business objectives.

# Future Directions: Embracing an Omnichannel Approach: 

While this analysis highlights the distinct advantages and limitations of the current sales methods (Call, Email, and Email + Call), the best course of action lies in adopting an omnichannel approach. By leveraging the strengths of each method and aligning them with specific customer needs or scenarios, the business can maximize both scalability and efficiency. For example, Email campaigns can drive broad engagement, Email + Call can focus on high-value opportunities, and Call can remain a targeted solution where other channels are unavailable.

In addition, it is crucial to expand the scope of this study by exploring other sales methods and their impacts on revenue. Future research could evaluate emerging channels such as SMS marketing, social media outreach, or live chat support to identify new opportunities for growth. By continuously analyzing the performance of both existing and new methods, the business can remain agile, optimize its sales strategy, and adapt to evolving market and customer dynamics.
