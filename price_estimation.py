import numpy as np
import pandas as pd

df = pd.read_csv('chocolate_preprocessed.csv')

max_rating = df['Rating'].max()
df['Rating'] = (df['Rating'] / max_rating) * 100
df['Rating'] = df['Rating'].astype(float)

df['price(100g)'] = df['Cocoa Percent'] * df['Rating'] * 25

dark_chocolates = df[df['Cocoa Percent'] > 70].copy()
dark_chocolates.reset_index(drop=True, inplace=True)

has_Trinitario = dark_chocolates['Bean Type'].str.contains('Trinitario')

dark_chocolates.loc[has_Trinitario, 'price(100g)'] *= 1.10

priceSum = dark_chocolates['price(100g)'].sum()