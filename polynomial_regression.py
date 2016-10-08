from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np

model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                   ('linear', LinearRegression(fit_intercept=False))])
# basically features will be changed to 1 + x1 + x2 + x3 + x1 x2 x3 + x1 ** 2 x2 + etc
features, train_size = raw_input().split()

features = int(features)
train_size = int(train_size)
x_train = []
y_train = []
for i in range(train_size):
    row = [float(i) for i in raw_input().split()]
    x_train.append(row[:-1])
    y_train.append(row[-1])

# train classifier

model.fit(x_train, y_train)

test_size = int(raw_input())
x_test = []

for i in range(test_size):
    row = [float(i) for i in raw_input().split()]
    x_test.append(row)

y_predict = model.predict(x_test)

for y in y_predict:
    print '%.2f' % y