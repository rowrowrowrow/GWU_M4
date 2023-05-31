#!/usr/bin/env python
# coding: utf-8

# # Analyzing Portfolio Risk and Return
# 
# In this Challenge, you'll assume the role of a quantitative analyst for a FinTech investing platform. This platform aims to offer clients a one-stop online investment solution for their retirement portfolios that’s both inexpensive and high quality. (Think about [Wealthfront](https://www.wealthfront.com/) or [Betterment](https://www.betterment.com/)). To keep the costs low, the firm uses algorithms to build each client's portfolio. The algorithms choose from various investment styles and options.
# 
# You've been tasked with evaluating four new investment options for inclusion in the client portfolios. Legendary fund and hedge-fund managers run all four selections. (People sometimes refer to these managers as **whales**, because of the large amount of money that they manage). You’ll need to determine the fund with the most investment potential based on key risk-management metrics: the daily returns, standard deviations, Sharpe ratios, and betas.
# 
# ## Instructions
# 
# ### Import the Data
# 
# Use the ``risk_return_analysis.ipynb`` file to complete the following steps:
# 
# 1. Import the required libraries and dependencies.
# 
# 2. Use the `read_csv` function and the `Path` module to read the `whale_navs.csv` file into a Pandas DataFrame. Be sure to create a `DateTimeIndex`. Review the first five rows of the DataFrame by using the `head` function.
# 
# 3. Use the Pandas `pct_change` function together with `dropna` to create the daily returns DataFrame. Base this DataFrame on the NAV prices of the four portfolios and on the closing price of the S&P 500 Index. Review the first five rows of the daily returns DataFrame.
# 
# ### Analyze the Performance
# 
# Analyze the data to determine if any of the portfolios outperform the broader stock market, which the S&P 500 represents. To do so, complete the following steps:
# 
# 1. Use the default Pandas `plot` function to visualize the daily return data of the four fund portfolios and the S&P 500. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 2. Use the Pandas `cumprod` function to calculate the cumulative returns for the four fund portfolios and the S&P 500. Review the last five rows of the cumulative returns DataFrame by using the Pandas `tail` function.
# 
# 3. Use the default Pandas `plot` to visualize the cumulative return values for the four funds and the S&P 500 over time. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 4. Answer the following question: Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?
# 
# ### Analyze the Volatility
# 
# Analyze the volatility of each of the four fund portfolios and of the S&P 500 Index by using box plots. To do so, complete the following steps:
# 
# 1. Use the Pandas `plot` function and the `kind="box"` parameter to visualize the daily return data for each of the four portfolios and for the S&P 500 in a box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 2. Use the Pandas `drop` function to create a new DataFrame that contains the data for just the four fund portfolios by dropping the S&P 500 column. Visualize the daily return data for just the four fund portfolios by using another box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
#     > **Hint** Save this new DataFrame&mdash;the one that contains the data for just the four fund portfolios. You’ll use it throughout the analysis.
# 
# 3. Answer the following question: Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?
# 
# ### Analyze the Risk
# 
# Evaluate the risk profile of each portfolio by using the standard deviation and the beta. To do so, complete the following steps:
# 
# 1. Use the Pandas `std` function to calculate the standard deviation for each of the four portfolios and for the S&P 500. Review the standard deviation calculations, sorted from smallest to largest.
# 
# 2. Calculate the annualized standard deviation for each of the four portfolios and for the S&P 500. To do that, multiply the standard deviation by the square root of the number of trading days. Use 252 for that number.
# 
# 3. Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of the four fund portfolios and of the S&P 500 index. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 4. Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of only the four fund portfolios. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 5. Answer the following three questions:
# 
# * Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?
# 
# * Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?
# 
# * Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time?
# 
# ### Analyze the Risk-Return Profile
# 
# To determine the overall risk of an asset or portfolio, quantitative analysts and investment managers consider not only its risk metrics but also its risk-return profile. After all, if you have two portfolios that each offer a 10% return but one has less risk, you’d probably invest in the smaller-risk portfolio. For this reason, you need to consider the Sharpe ratios for each portfolio. To do so, complete the following steps:
# 
# 1. Use the daily return DataFrame to calculate the annualized average return data for the four fund portfolios and for the S&P 500. Use 252 for the number of trading days. Review the annualized average returns, sorted from lowest to highest.
# 
# 2. Calculate the Sharpe ratios for the four fund portfolios and for the S&P 500. To do that, divide the annualized average return by the annualized standard deviation for each. Review the resulting Sharpe ratios, sorted from lowest to highest.
# 
# 3. Visualize the Sharpe ratios for the four funds and for the S&P 500 in a bar chart. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 4. Answer the following question: Which of the four portfolios offers the best risk-return profile? Which offers the worst?
# 
# #### Diversify the Portfolio
# 
# Your analysis is nearing completion. Now, you need to evaluate how the portfolios react relative to the broader market. Based on your analysis so far, choose two portfolios that you’re most likely to recommend as investment options. To start your analysis, complete the following step:
# 
# * Use the Pandas `var` function to calculate the variance of the S&P 500 by using a 60-day rolling window. Visualize the last five rows of the variance of the S&P 500.
# 
# Next, for each of the two portfolios that you chose, complete the following steps:
# 
# 1. Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.
# 
# 2. Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.
# 
# 3. Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.
# 
# 4. Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# Finally, answer the following two questions:
# 
# * Which of the two portfolios seem more sensitive to movements in the S&P 500?
# 
# * Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?
# 

# ### Import the Data

# #### Step 1: Import the required libraries and dependencies.

# In[1]:


# Import the required libraries and dependencies
# YOUR CODE HERE
import pandas as pd
from pathlib import Path
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# #### Step 2: Use the `read_csv` function and the `Path` module to read the `whale_navs.csv` file into a Pandas DataFrame. Be sure to create a `DateTimeIndex`. Review the first five rows of the DataFrame by using the `head` function.

# In[2]:


# Import the data by reading in the CSV file and setting the DatetimeIndex 
# Review the first 5 rows of the DataFrame
# YOUR CODE HERE
whales_navs_df = pd.read_csv(
    Path('./Resources/whale_navs.csv'), 
    index_col="date", 
    parse_dates=True, 
    infer_datetime_format=True
)

whales_navs_df.head()


# #### Step 3: Use the Pandas `pct_change` function together with `dropna` to create the daily returns DataFrame. Base this DataFrame on the NAV prices of the four portfolios and on the closing price of the S&P 500 Index. Review the first five rows of the daily returns DataFrame.

# In[3]:


# Prepare for the analysis by converting the dataframe of NAVs and prices to daily returns
# Drop any rows with all missing values
# Review the first five rows of the daily returns DataFrame.
# YOUR CODE HERE
whale_navs_daily_returns = whales_navs_df.pct_change().dropna()

whale_navs_daily_returns.head()


# ---

# ## Quantitative Analysis
# 
# The analysis has several components: performance, volatility, risk, risk-return profile, and portfolio diversification. You’ll analyze each component one at a time.

# ###  Analyze the Performance
# 
# Analyze the data to determine if any of the portfolios outperform the broader stock market, which the S&P 500 represents.

# #### Step 1:  Use the default Pandas `plot` function to visualize the daily return data of the four fund portfolios and the S&P 500. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[4]:


# Plot the daily return data of the 4 funds and the S&P 500 
# Inclue a title parameter and adjust the figure size
# YOUR CODE HERE
whale_navs_daily_returns.plot(figsize=(20,10), title="Whale Daily Returns", legend=True)


# #### Step 2: Use the Pandas `cumprod` function to calculate the cumulative returns for the four fund portfolios and the S&P 500. Review the last five rows of the cumulative returns DataFrame by using the Pandas `tail` function.

# In[5]:


# Calculate and plot the cumulative returns of the 4 fund portfolios and the S&P 500
# Review the last 5 rows of the cumulative returns DataFrame
# YOUR CODE HERE
whale_navs_cumulative_daily_returns = (1 + whale_navs_daily_returns).cumprod()

whale_navs_cumulative_daily_returns.tail()


# #### Step 3: Use the default Pandas `plot` to visualize the cumulative return values for the four funds and the S&P 500 over time. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[6]:


# Visualize the cumulative returns using the Pandas plot function
# Include a title parameter and adjust the figure size
# YOUR CODE HERE
whale_navs_cumulative_daily_returns.plot(figsize=(20,10), title="Whale Cumulative Daily Returns", legend=True)


# #### Step 4: Answer the following question: Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?

# **Question** Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?
# 
# **Answer** None of the funds outperform the S&P 500 Index

# ---

# ### Analyze the Volatility
# 
# Analyze the volatility of each of the four fund portfolios and of the S&P 500 Index by using box plots.

# #### Step 1: Use the Pandas `plot` function and the `kind="box"` parameter to visualize the daily return data for each of the four portfolios and for the S&P 500 in a box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[7]:


# Use the daily return data to create box plots to visualize the volatility of the 4 funds and the S&P 500 
# Include a title parameter and adjust the figure size
# YOUR CODE HERE
whale_navs_daily_returns.plot(kind='box', title="Whale Daily Returns, Box Plot", legend=True)


# #### Step 2: Use the Pandas `drop` function to create a new DataFrame that contains the data for just the four fund portfolios by dropping the S&P 500 column. Visualize the daily return data for just the four fund portfolios by using another box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[8]:


# Create a new DataFrame containing only the 4 fund portfolios by dropping the S&P 500 column from the DataFrame
# Create box plots to reflect the return data for only the 4 fund portfolios
# Include a title parameter and adjust the figure size
# YOUR CODE HERE
fund_only_daily_returns = whale_navs_daily_returns.drop(columns="S&P 500")

fund_only_daily_returns.plot(figsize=(20,10), kind='box', title="Fund Daily Returns, Box Plot", legend=True)


# #### Step 3: Answer the following question: Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?

# **Question** Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?
# 
# **Answer** Berkshire Hathaway Inc. was the most volatile and Tiger Global Management LLC was the least volatile.

# ---

# ### Analyze the Risk
# 
# Evaluate the risk profile of each portfolio by using the standard deviation and the beta.

# #### Step 1: Use the Pandas `std` function to calculate the standard deviation for each of the four portfolios and for the S&P 500. Review the standard deviation calculations, sorted from smallest to largest.

# In[9]:


# Calculate and sort the standard deviation for all 4 portfolios and the S&P 500
# Review the standard deviations sorted smallest to largest
# YOUR CODE HERE
whale_navs_std_sorted = whale_navs_daily_returns.std().sort_values()

whale_navs_std_sorted


# #### Step 2: Calculate the annualized standard deviation for each of the four portfolios and for the S&P 500. To do that, multiply the standard deviation by the square root of the number of trading days. Use 252 for that number.

# In[10]:


# Calculate and sort the annualized standard deviation (252 trading days) of the 4 portfolios and the S&P 500
# Review the annual standard deviations smallest to largest
# YOUR CODE HERE
whale_navs_annualized_std = whale_navs_std_sorted * np.sqrt(252)

whale_navs_annualized_std


# #### Step 3: Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of the four fund portfolios and of the S&P 500 index. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[11]:


# Using the daily returns DataFrame and a 21-day rolling window, 
# plot the rolling standard deviation of the 4 portfolios and the S&P 500
# Include a title parameter and adjust the figure size
# YOUR CODE HERE
whale_navs_daily_returns.rolling(window=21).std().plot(figsize=(20,10), title="Whale 21 day rolling standard deviations")


# #### Step 4: Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of only the four fund portfolios. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[12]:


# Using the daily return data and a 21-day rolling window, plot the rolling standard deviation of just the 4 portfolios. 
# Include a title parameter and adjust the figure size
# YOUR CODE HERE
fund_only_daily_returns.rolling(window=21).std().plot(figsize=(20,10), title="Fund 21 day rolling standard deviations")


# #### Step 5: Answer the following three questions:
# 
# 1. Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?
# 
# 2. Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?
# 
# 3. Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time?

# **Question 1**  Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?
# 
# **Answer 1** The following portfolio funds have a greater annualized standard deviation than the S&P 500:
# 
# SOROS FUND MANAGEMENT LLC      0.022297
# 
# PAULSON & CO.INC.              0.034912
# 
# BERKSHIRE HATHAWAY INC         0.051692

# **Question 2** Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?
# 
# **Answer 2** Yes, they seem to be positively correlated.
# 

# **Question 3** Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time? 
# 
# **Answer 3** Berkshire Hathaway Inc. poses the most risk, however this doesn't appear to be the case during the earlier period between 2015 and 2016. During 2016 - 2017 the volatility of Berkshire Hathaway Inc. increased substantially.

# ---

# ### Analyze the Risk-Return Profile
# 
# To determine the overall risk of an asset or portfolio, quantitative analysts and investment managers consider not only its risk metrics but also its risk-return profile. After all, if you have two portfolios that each offer a 10% return but one has less risk, you’d probably invest in the smaller-risk portfolio. For this reason, you need to consider the Sharpe ratios for each portfolio.

# #### Step 1: Use the daily return DataFrame to calculate the annualized average return data for the four fund portfolios and for the S&P 500. Use 252 for the number of trading days. Review the annualized average returns, sorted from lowest to highest.

# In[13]:


# Calculate the annual average return data for the for fund portfolios and the S&P 500
# Use 252 as the number of trading days in the year
# Review the annual average returns sorted from lowest to highest
# YOUR CODE HERE
whale_navs_annualized_average_returns = (whale_navs_daily_returns.mean() * 252).sort_values()

whale_navs_annualized_average_returns


# #### Step 2: Calculate the Sharpe ratios for the four fund portfolios and for the S&P 500. To do that, divide the annualized average return by the annualized standard deviation for each. Review the resulting Sharpe ratios, sorted from lowest to highest.

# In[14]:


# Calculate the annualized Sharpe Ratios for each of the 4 portfolios and the S&P 500.
# Review the Sharpe ratios sorted lowest to highest
# YOUR CODE HERE
whale_navs_annualized_sharpe_ratio = whale_navs_annualized_average_returns / (whale_navs_daily_returns.std() * np.sqrt(252))

whale_navs_annualized_sharpe_ratio = whale_navs_annualized_sharpe_ratio.sort_values()

whale_navs_annualized_sharpe_ratio


# #### Step 3: Visualize the Sharpe ratios for the four funds and for the S&P 500 in a bar chart. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[15]:


# Visualize the Sharpe ratios as a bar chart
# Include a title parameter and adjust the figure size
# YOUR CODE HERE
whale_navs_annualized_sharpe_ratio.plot(figsize=(5,5),kind='bar', title="Whales Annualized Sharpe Ratio")


# #### Step 4: Answer the following question: Which of the four portfolios offers the best risk-return profile? Which offers the worst?

# **Question** Which of the four portfolios offers the best risk-return profile? Which offers the worst?
#     
# **Answer** Based on the annualized sharpe ratio metric, Berkshire Hathaway Inc. offers the best risk-return profile.

# ---

# ### Diversify the Portfolio
# 
# Your analysis is nearing completion. Now, you need to evaluate how the portfolios react relative to the broader market. Based on your analysis so far, choose two portfolios that you’re most likely to recommend as investment options.

# #### Use the Pandas `var` function to calculate the variance of the S&P 500 by using a 60-day rolling window. Visualize the last five rows of the variance of the S&P 500.

# In[16]:


# Calculate the variance of the S&P 500 using a rolling 60-day window.
# YOUR CODE HERE
snp500_rolling_60_variance = whale_navs_daily_returns['S&P 500'].rolling(window=60).var()

snp500_rolling_60_variance.tail()


# #### For each of the two portfolios that you chose, complete the following steps:
# 
# 1. Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.
# 
# 2. Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.
# 
# 3. Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.
# 
# 4. Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# ##### Portfolio 1 & 2 - Step 1: Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.

# In[17]:


# Establish the two portfolios I'll use for the following sections
top_2_portfolios = [
    'BERKSHIRE HATHAWAY INC',
    'TIGER GLOBAL MANAGEMENT LLC'
]

top_2_portfolios_df = whale_navs_daily_returns.loc[:,top_2_portfolios]

display(top_2_portfolios_df.head())


# In[18]:


# Calculate the covariance using a 60-day rolling window 
# Review the last five rows of the covariance data
# YOUR CODE HERE

top_2_portfolios_covariance = top_2_portfolios_df.rolling(window=60).cov(whale_navs_daily_returns['S&P 500'])

top_2_portfolios_covariance.tail()


# ##### Portfolio 1 & 2 - Step 2: Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.

# In[19]:


# Calculate the beta based on the 60-day rolling covariance compared to the market (S&P 500)
# Review the last five rows of the beta information
# YOUR CODE HERE
top_2_portfolios_beta = top_2_portfolios_covariance.div(snp500_rolling_60_variance, axis=0)

top_2_portfolios_beta.tail()


# ##### Portfolio 1 & 2 - Step 3: Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.

# In[20]:


# Calculate the average of the 60-day rolling beta
# YOUR CODE HERE

top_2_portfolios_60day_avg_beta = top_2_portfolios_beta.mean()

top_2_portfolios_60day_avg_beta


# ##### Portfolio 1 & 2 - Step 4: Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[21]:


# Plot the rolling beta 
# Include a title parameter and adjust the figure size
# YOUR CODE HERE

top_2_portfolios_beta.plot(figsize=(20,10), title=f"{' - '.join(top_2_portfolios)} Rolling 60 Beta", legend=True)


# #### Answer the following two questions:
# 
# 1. Which of the two portfolios seem more sensitive to movements in the S&P 500?
# 
# 2. Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?

# **Question 1** Which of the two portfolios seem more sensitive to movements in the S&P 500?
#     
# **Answer 1** Berkshire Hathaway Inc. seems more sensitive to movements in the S&P 500.
# 

# **Question 2** Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?
#     
# **Answer 2** Berkshire Hathaway Inc. because the risk-return profile is better.

# In[ ]:





# ---
