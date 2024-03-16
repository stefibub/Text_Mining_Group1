import pandas as pd
import re

df = pd.read_csv('dataset.csv')

df = df.drop_duplicates(subset='review_text', keep='first')

df['review_text'] = df['review_text'].str.lower()
df = df[df['review_text'].notna() & (df['review_text'] != '')]
df = df[df['app_name'].notna() & (df['app_name'] != '')]

print(df.head(10))