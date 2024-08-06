import numpy as np
import pandas as pd

df = pd.read_csv('chocolate_price.csv')


df = df[df['Cocoa Percent'] <= 70]
df.reset_index(drop=True, inplace=True)

companies = df.groupby(['Company', 'Review Date'])['Rating'].mean()
companies = companies.unstack()

companies.columns.name = None
companies.index.name = None

mean_ratings = companies.loc[:, "2012":].apply(lambda row: row.mean(), axis=1)

sorted_ratings = mean_ratings.sort_values(ascending=False, kind='mergesort')
best_ratings = sorted_ratings.head(10)
best_ratings.name = None
best_ratings.index.name = None

chocolates_to_sell = df[df['Company'].isin(best_ratings.index)].copy()
chocolates_to_sell.reset_index(drop=True, inplace=True)

priceSum = chocolates_to_sell['price(100g)'].sum()