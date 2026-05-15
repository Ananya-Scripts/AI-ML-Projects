import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data={
    "hours": [1, 2, 3, 4, 5,6,7,8,9,10],
    "marks": [30,40, 50,65,75,83,90,105,120,150]
}

df= pd.DataFrame(data)
print("Raw Data")
print(df)

x=df[["hours"]]  # x is a 2D array, so we use double brackets to select the "hours" column as a DataFrame
y=df["marks"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)
print("x_train")
print("x_test")

model= LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)

score = r2_score(y_test,y_pred)
print ("\n Model Accuracy", score)

a= int (input("Enter hours to predict marks: "))    
new_hours= [[a]]
pred= model.predict(new_hours)
print("\n Obtain marks according to predictions:", pred)

plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.xlabel("hours")
plt.ylabel("marks")
plt.title("Hours vs Marks")
plt.show()
