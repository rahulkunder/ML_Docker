import pandas
data = pandas.read_csv('SalaryData.csv')
x = data['YearsExperience']
y = data['Salary']
X_train = x.values.reshape(30,1)
from sklearn.linear_model import LinearRegression
mind = LinearRegression()
mind = mind.fit(X_train, y)
value = float(input("Enter the year of Experience: "))
print(mind.predict([[value]]))


