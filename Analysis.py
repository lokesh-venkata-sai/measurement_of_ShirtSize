import pandas as pd
from matplotlib import pyplot
import seaborn as sns
import sklearn.preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

path = "E:/study/sem 6/R&D/proj/filtereddata.csv"

df=pd.read_csv(path)

Y=df[["Actual (in cm)"]]
z=df[["ratio75","ratio100","ratio150"]]#for multiple linear regression
lm1=LinearRegression()
lm1.fit(z,Y)
print("intercept is ",lm1.intercept_)
print("coefficients are ",lm1.coef_)
Yhat=lm1.predict(z)
"""ax1 = sns.distplot(df['Actual (in cm)'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)#Yhat is given as a predicted values (calculated before)
pyplot.show()"""



predict =z.iloc[0:39,]
vector=Y.iloc[0:34,]
poly = PolynomialFeatures(degree=3)
x=z.iloc[0:34,]

X_ = poly.fit_transform(x)
predict_ = poly.fit_transform(predict)

clf = sklearn.linear_model.LinearRegression()
clf.fit(X_, vector)
Yhat=clf.predict(predict_)
print("predicted values")
print(Yhat)
ax1 = sns.distplot(df['Actual (in cm)'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)#Yhat is given as a predicted values (calculated before)
pyplot.show()