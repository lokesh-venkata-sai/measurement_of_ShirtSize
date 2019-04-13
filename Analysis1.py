import pandas as pd
from matplotlib import pyplot
import seaborn as sns
import sklearn.preprocessing
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

path = "sizedata.csv"

df=pd.read_csv(path)

Y=df[["Actual (in cm)"]]
z=df[["W75","W100","W150"]]#for multiple linear regression
lm1=LinearRegression()
lm1.fit(z,Y)
print("intercept is ",lm1.intercept_)
print("coefficients are ",lm1.coef_)
Yhat=lm1.predict(z)
"""ax1 = sns.distplot(df['Actual (in cm)'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)#Yhat is given as a predicted values (calculated before)
pyplot.show()"""

x=df['W100'];
y=df["W150"];
x_test = x.iloc[16:22,]
f=np.polyfit(x.iloc[0:16,],y.iloc[0:16,],6);
p=np.poly1d(f)
print("---------------------------------------------")
print(p)
print("---------prediction of W100 from W75 -------------")
yhat=p(x_test)
print(yhat)
ax1 = sns.distplot(df['W150'], hist=False, color="r", label="Actual Value")
sns.distplot(yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)#Yhat is given as a predicted values (calculated before)
pyplot.title("from W100 to W150")
pyplot.show()