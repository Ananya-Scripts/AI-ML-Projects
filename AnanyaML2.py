import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 

data={
    "Subscribers":[
        1000,
        2000,
        3000,
        4000,
        5000,
        6000
    ],
    "Likes":[
        200,
        600,
        1000,
        1400,
        1800,
        2200
        
    ]
}

df=pd.DataFrame(data)
print("RawData")
print(df)

x=df[["Subscribers"]]
y=df["Likes"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("x_train")
print("x_test")

model = LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)

score=r2_score(y_test,y_pred)
print("\n Model Accuracy:", score) 

a=int(input("Enter Subscribers to predict Likes:"))
new_likes= [[a]]
pred=model.predict(new_likes)
print("\n obtain Likes according to Subscribers:", pred)

plt.scatter(x,y)
plt.plot(x, model.predict(x))
plt.xlabel("Subscribe")
plt.ylabel("Likes")
plt.title("Subscribers vs Likes")
plt.show()
