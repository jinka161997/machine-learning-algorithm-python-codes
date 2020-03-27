import pandas as pd
import seaborn as sb

from sklearn.linear_model import LogisticRegression


# loading claimants data 
claimants = pd.read_csv("file:///F:/pythone codes/logistic regression/claimants(1).csv")

claimants.head(10)
# Droping first column 
claimants.drop(["CASENUM"],inplace=True,axis = 1)

#cat_cols = ["ATTORNEY","CLMSEX","SEATBELT","CLMINSUR"]
#cont_cols = ["CLMAGE","LOSS"]

# Getting the barplot for the categorical columns 

sb.countplot(x="ATTORNEY",data=claimants)
pd.crosstab(claimants.ATTORNEY,claimants.CLMINSUR).plot(kind="bar")
help(sb.countplot)
sb.countplot(x="CLMSEX",data=claimants)
pd.crosstab(claimants.CLMSEX,claimants.CLMINSUR).plot(kind="bar")
sb.countplot(x="SEATBELT",data=claimants,)
pd.crosstab(claimants.SEATBELT,claimants.CLMINSUR).plot(kind="bar")

sb.countplot(x="CLMINSUR",data=claimants)

# Data Distribution - Boxplot of continuous variables wrt to each category of categorical columns
help(sb.boxplot)
sb.boxplot(data = claimants,orient = "v")
sb.boxplot(x="ATTORNEY",y="CLMAGE",data=claimants,palette = "hls")
sb.boxplot(x="ATTORNEY",y="LOSS",data=claimants,palette="hls")
sb.boxplot(x="CLMSEX",y="CLMAGE",data=claimants,palette="hls")
sb.boxplot(x="CLMSEX",y="LOSS",data=claimants,palette="hls")
sb.boxplot(x="SEATBELT",y="CLMAGE",data=claimants,palette="hls")
sb.boxplot(x="SEATBELT",y="LOSS",data=claimants,palette="hls")
sb.boxplot(x="CLMINSUR",y="CLMAGE",data=claimants,palette="hls")
sb.boxplot(x="CLMINSUR",y="LOSS",data=claimants,palette="hls")

# To get the count of null values in the data 

claimants.isnull().sum()


claimants.shape # 1340 6 => Before dropping null values

# To drop null values ( dropping rows)

claimants.dropna().shape # 1096 6 => After dropping null values

# Fill nan values with mode of the categorical column 

claimants["CLMSEX"].fillna(1,inplace=True) # claimants.CLMSEX.mode() = 1


claimants["CLMINSUR"].fillna(1,inplace=True) # claimants.CLMINSUR.mode() = 1

claimants["SEATBELT"].fillna(0,inplace=True) # claimants.SEATBELT.mode() = 0


claimants.CLMAGE.fillna(28.4144,inplace=True) # claimants.CLMAGE.mean() = 28.4
claimants.isnull().sum()
# Model building 


claimants.shape
X = claimants.iloc[:,[1,2,3,4,5]]
Y = claimants.iloc[:,0]
classifier = LogisticRegression()
classifier.fit(X,Y)

classifier.coef_ # coefficients of features 
classifier.predict_proba (X) # Probability values 

y_pred = classifier.predict(X)
claimants["y_pred"] = y_pred
y_prob = pd.DataFrame(classifier.predict_proba(X.iloc[:,:]))
new_df = pd.concat([claimants,y_prob],axis=1)
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(Y,y_pred)
print (confusion_matrix)

##########################################################################
# Loading data which contains categorical data to demonstrate how to 
# create dummy columns 

salary = pd.read_csv("E:\\Excelr Data\\Data Sets\\Support Vector Machines\\SalaryData_Test.csv")

# creating dummy columns for the categorical columns 
names = list(salary.columns)
sal_dummies = pd.get_dummies(salary[["workclass","occupation","education","maritalstatus","relationship","race","sex","native"]])
# Dropping the columns for which we have created dummies
salary.drop(["workclass","education","maritalstatus","occupation","relationship","race","sex","native"],inplace=True,axis = 1)

# adding the columns to the salary data frame 

salary = pd.concat([salary,sal_dummies],axis=1)

salary["cat"] = 0
salary.cat.head(15)

salary.loc[salary.Salary==" <=50K","cat"] = 1
salary.Salary.value_counts()
salary.cat.value_counts()
salary.drop(["Salary"],axis=1,inplace=True)

##########################################################################