from sklearn import linear_model

clf = linear_model.LinearRegression()

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

clf.fit(x_train, y_train)

test_size = int(raw_input())
x_test = []

for i in range(test_size):
    row = [float(i) for i in raw_input().split()]
    x_test.append(row)

y_predict = clf.predict(x_test)

for y in y_predict:
    print '%.2f' % y