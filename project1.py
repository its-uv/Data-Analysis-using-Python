import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Reading csv file through pandas
df = pd.read_csv(
    'D:\\Py project\\Python_Diwali_Sales_Analysis-main\\Diwali Sales Data.csv', encoding='unicode_escape')

# DATA CLEANING

# Just for inspection
# print(df.shape)
# print(df.info())

# Removing null columns
df.drop(['Status', "unnamed1"], axis=1, inplace=True)

# Checking if null values still exists
is_null = pd.isnull(df).sum()

# Here removing entire rows which had missing values
df.dropna(inplace=True)

# Changing the type of a column <NOT IMPORTANT>

# df['Amount'] = df['Amount'].astype('int')
# print(df.info())
# print(df['Amount'].dtypes)

# Statistical data of our table
# print(df.describe()) ---UC

# print(df[['Age', 'Orders']].describe())  ---UC

# EXPLORATORY DATA ANALYSIS


ax = sns.countplot(x="Gender", data=df)


for bars in ax.containers:
    ax.bar_label(bars)

# plt.show()

sales_gen = df.groupby(['Gender'], as_index=False)[
    'Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender', y='Amount', data=sales_gen)

# plt.show()

# With we can see that most of the buyers are females and even their purchasing power is greater than men


ax = sns.countplot(data=df, x='Age Group', hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)

sales_age = df.groupby(['Age Group'], as_index=False)[
    'Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x="Age Group", y='Amount', data=sales_age)

# plt.show()

# From above graph we can see that most of the buyers are of age group between 26-35 yrs female


# State

# print(df.columns)

# Total number of order from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum(
).sort_values(by='Orders', ascending=False).head(10)

sns.set_theme(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x='State', y='Orders')

# Total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum(
).sort_values(by='Amount', ascending=False).head(10)

sns.set_theme(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x='State', y='Amount')

# From above graph we can see that unexpectedly most the orders are from UP, Karnataka, Maharashtra respectively


ax = sns.countplot(data=df, x='Marital_Status')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum(
).sort_values(by='Amount', ascending=False).head(10)

sns.set_theme(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')
# From above graphs we can see that most the buyers are married (women) and they have high purchasing power


ax = sns.countplot(data=df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)

sns.set_theme(rc={"figure.figsize": (15, 5)})

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum(
).sort_values(by='Amount', ascending=False).head(10)

sns.set_theme(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')

# From above graphs we can see that most of the buyers are working in IT,Aviation and Healtcare sector

ax = sns.countplot(data=df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)

sns.set_theme(rc={"figure.figsize": (15, 5)})

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum(
).sort_values(by='Amount', ascending=False).head(10)

sns.set_theme(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount')

# From above graph we can see that most of the sold products are from food,footwear and electronic category

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum(
).sort_values(by='Orders', ascending=False).head(10)

sns.set_theme(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders')

"""
CONCLUSION:
Married women of age group 26 - 35 yrs from UP, Maharashtra and Karnataka working IT, Healtcare and Aviation are more likely to buy products from food clothing and electronics category
"""
