# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:06:38 2018

@author: madis
"""

import pandas as pd
import numpy as np



# Finding mean,median,mode
mba = pd.read_csv("E:\\Excelr Data\\Data Sets\\Datasets_BA 2\\mba.csv")


mba.mean()
mba["workex"]
np.mean(mba.gmat)
mba['gmat'].mean() # mba.gmat.mean()
mba['gmat'].median()
mba['gmat'].mode()
mba['gmat'].var()
mba['gmat'].std()

# variance & Standard Deviation for Sample
mba['gmat'].var() # 860
mba['gmat'].std() # 29.39

# Variacne & Standard Deviation for Population
import numpy as np
np.var(mba['gmat']) # 859.70
np.std(mba['gmat']) # 29.32


# calculating the range value 
range = max(mba['gmat'])-min(mba['gmat']) # max(mba.gmat)-min(mba.gmat)
range


mba.columns # accessing column names 
mba.datasrno # Accessing datasrno using "." (dot) operation

mba["workex"]
mba[["datasrno","workex"]] #  accessing multiple columns 
mba.iloc[45:52,0:3] # mba.iloc[i,j] 
#     i => row index values  | j => column index values
mba.loc[45:51,["workex","datasrno"]]

mtcars = pd.read_csv("E:\Excelr Data\Python Classes\Basic Statistics _ Visualizations\\mtcars.csv")

mtcars1 = mtcars[(mtcars.mpg>15) &  (mtcars.mpg<19)]
mtcars2 = mtcars[(mtcars.mpg>15) |  (mtcars.mpg<19)]
mtcars.carb.value_counts()


# to get the count of each category from a specific column 
mtcars.gear.value_counts()


# Creating a data frame using dictionary object 
x = {"A":pd.Series([1,2,3,4,5,7,8,10]),"B":pd.Series(["A","B","C","D","E","F","G"]),"C":pd.Series([1,2,3,4,5,7,8])}
new_x = pd.DataFrame(x)
# creating Data frame using NUMPY
y = pd.DataFrame(np.random.randint(low=0, high=10, size=(6, 5)),columns=['a', 'b', 'c', 'd', 'e'])
y



# importing data set using pandas

mba.head()
mba.tail()

# Finding 3rd and 4rth Business Moments
mba.skew()
mba.kurt()

mba['gmat'].kurt()

# Graphical Representation of data
#import matplotlib.pyplot as plt
# Histogram
import matplotlib.pyplot as plt

plt.hist(mba['gmat']) # left skew 

#Boxplot
plt.boxplot(mba['gmat']);plt.ylabel("GMAT")# for vertical
plt.boxplot(mba['gmat'],1,'rs',0)# For Horizontal
help(plt.boxplot)


# Barplot
# bar plot we need height i.e value of each data
# left - for starting point of each bar plot of data on X-axis(Horizontal axis). Here data is mba['gmat']
index = np.arange(773) # np.arange(a)  = > creates consecutive numbers from 
# 0 to 772 

mba.shape # dimensions of data frame 
plt.bar(height = mba["gmat"], x = index) # initializing the parameter 
help(plt.bar)
# left with index values 

#mtcars = pd.read_csv("C:\\Users\\madis\\Downloads\\Python Classes\\Basic Statistics _ Visualizations\\mtcars.csv")


# table 
pd.crosstab(mtcars.gear,mtcars.cyl)



pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar")
mtcars.gear.value_counts().plot(kind="pie")

mtcars.mpg.plot(kind='area') 
plt.plot(np.arange(32),mtcars.mpg,"ro")

import seaborn as sns 
# getting boxplot of mpg with respect to each category of gears 
sns.boxplot(x="gear",y="mpg",data=mtcars)

sns.pairplot(mtcars.iloc[:,0:4]) # histogram of each column and 
# scatter plot of each variable with respect to other columns 

import numpy as np
plt.plot(np.arange(32),mtcars.mpg,"bo") # scatter plot of single variable

plt.plot(np.arange(32),mtcars.mpg,"ro-")

help(plt.plot)

# Scatter plot between different inputs



# ro  indicates r - red , o - points 
#


import pandas as pd

# importing data set using pandas
mba = pd.read_csv("E:\\Excelr Data\\Datasets\\Datasets_BA 2\\mba.csv")


import scipy.stats as stats
# ppf => Percent point function 
stats.norm.ppf(0.975,0,1)# similar to qnorm in R

# cdf => cumulative distributive function 
stats.norm.cdf(740,711,29) # similar to pnorm in R 

# cummulative distribution function
help(stats.norm.cdf)

#Q-Q plot

import pylab          
import scipy.stats as st

# Checking Whether data is normally distributed
st.probplot(mba['gmat'], dist="norm",plot=pylab)

stats.probplot(mba.workex,dist="norm",plot=pylab)

mtcars = pd.read_csv("E:\\Excelr Data\\Python Codes\\Basic Statistics _ Visualizations\\mtcars.csv")

st.probplot(mtcars.mpg,dist="norm",plot=pylab)
help(st.probplot)


# t distribution 

# Finding qnorm,qt  for 90%,95%,99% confidence level

import scipy.stats as stats
# percentage point function 
stats.norm.ppf(0.975,0,1)# similar to qnorm in R
stats.norm.ppf(0.995,0,1)
stats.norm.ppf(0.950,0,1)
stats.t.ppf(0.975, 139) # similar to qt in R
stats.t.ppf(0.995,139)
stats.t.ppf(0.950,139)
help(stats.t.ppf) 
