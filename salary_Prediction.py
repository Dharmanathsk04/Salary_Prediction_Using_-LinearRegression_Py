from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]

Y = [3000,3500,40000,50000,60000]

model = LinearRegression()

model.fit(X,Y)

prediction = model.predict([[3.5]])

print("predicted salary: ",prediction[0])