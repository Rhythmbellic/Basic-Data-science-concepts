#importing some required libraries.
import pandas as pd
import numpy as np
import matlplotlin.pyplot as plt
import seaborn as sns
#storing data frame in one variable.
housing=pd.read_csv("housing.csv")
#taking look on a small part of data.
housing.head(10)
#knowing all specs about data.
housing.info()
#staticall description.
housing.describe()
#plotting graph of all numerical variable to know the data distribution.
housing.hist(bins=50,figsize=(20,15))
#counting of catagarical values.
housing.groupby('ocean_proximity')['total_rooms'].count()
#from here we will plot graphs to see the graphical representation of catagarical variables.
values=('1h ocean','INLAND','ISLAND','NEAR BAY','NEAR OCEAN')
labels=(9136,6551,5,2290,2658)
plt.pie(labels,labels=values)
plt.bar(values,labels,color='green')
#lets plot some more graph of numerical variables
plt.scatter(x=housing['total_bedrooms'],y=housing['median_house_value'])
plt.hist(housing['total_bedrooms'],bins=10)
plt.boxplot(housing['housing_median_age'])
#to know about all unique values of catagarical variable
housing['ocean_proximity'].unique()
#to be continued
