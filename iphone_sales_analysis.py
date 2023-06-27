import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go
df = pd.read_csv("apple_products.csv")
#print(df.head())
#print(df.isnull().sum())
#print(df.describe())
highest_rated = df.sort_values(by = ['Star Rating'], ascending=False)
highest_rated = highest_rated.head(10)
#print(highest_rated['Product Name']) # starting k 5 iphones india m sabse jyada sell hone wale iphone h
iphone = highest_rated['Product Name'].value_counts()
label = iphone.index
counts = highest_rated["Number Of Ratings"]
figure1 = px.bar(highest_rated, x=label, y=counts, title = "Number Of Ratings Of Highest Rated Iphone")
figure1.show()
#analysis of revies
iphone = highest_rated['Product Name'].value_counts()
label = iphone.index
Review_counts = highest_rated["Number Of Reviews"]
figure2 = px.bar(highest_rated, x=label, y=Review_counts, title = "Number Of Reviews Of Highest Rated Iphone")
figure2.show()
figure3 = px.scatter(data_frame=df, x="Number Of Ratings", y="Sale Price", size = "Discount Percentage", trendline = "ols", title = "Relationship between sale price and number of ratings of iphones")
figure3.show()
# conclusion :- sale price jitna kam hota jata h utna kam bikta hai
#analysis on basis of discounts
figure4 = px.scatter(data_frame=df, x="Number Of Ratings", y="Discount Percentage", size = "Sale Price", trendline = "ols", title = "Relationship between Discount Percentage and number of ratings of iphones")
figure4.show()
#conclusion :- jitna jyada high discount utna jyada phone sell padhenga