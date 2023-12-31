
**Problem Statement**: Given above data build a machine learning model that can predict home prices based on square feet area

You can represent values in above table as a scatter plot (values are shown in red markers). After that one can draw a straight line that best fits values on chart.

You can draw multiple lines like this but we choose the one where total sum of error is minimum

You might remember about linear equation from your high school days math class. Home prices can be presented as following equation,

home price = m * (area) + b


# import the libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# read the datset and manipulate
df = pd.read_csv('generated_dataset.csv')
df.drop_duplicates(inplace=True)
df.size
df.fillna(df.mean(), inplace=True)
df

# Commented out IPython magic to ensure Python compatibility.
# plot
%matplotlib inline
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.savefig("scatterplot.jpg")

# reshape
area = df.area.values.reshape(-1,1)
price = df.price.values.reshape(-1,1)

# train test split
from sklearn.model_selection import train_test_split

area_train,area_test,price_train,price_test = train_test_split(area,price,random_state=0,test_size=0.25)

# Create linear regression object
reg = linear_model.LinearRegression()
reg.fit(area_train,price_train)

# score
print(reg.score(area_test,price_test))

price_pred = reg.predict(area_test)
plt.scatter(area_test, price_test, color ='b')
plt.plot(area_test, price_pred, color ='k')
plt.show()

from sklearn.metrics import mean_absolute_error,mean_squared_error


mae = mean_absolute_error(y_true=price_test,y_pred=price_pred)
#squared True returns MSE value, False returns RMSE value.
mse = mean_squared_error(y_true=price_test,y_pred=price_pred) #default=True
rmse = mean_squared_error(y_true=price_test,y_pred=price_pred,squared=False)

print("MAE:",mae)
print("MSE:",mse)
print("RMSE:",rmse)

"""**(1) Predict price of a home with area = 3300 sqr ft**"""

reg.predict([[3300]])

reg.coef_

reg.intercept_

"""**Y = m * X + b (m is coefficient and b is intercept)**"""

3300*135.78767123 + 180616.43835616432

"""**(1) Predict price of a home with area = 5000 sqr ft**"""

reg.predict([[5000]])
