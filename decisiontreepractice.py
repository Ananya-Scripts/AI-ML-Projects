import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data= {

    "WatchTime": [3,4,2,5,1,7,3],
    "User": [6,2,2,6,4,5,8]
}

df= pd.DataFrame(data)
x=df[["WatchTime"]]
y=df["User"]

model= DecisionTreeClassifier()
model.fit(x,y)
Time=model.predict ([[5]])
print(Time[0])
