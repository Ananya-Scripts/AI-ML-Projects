import pandas as pd 
from sklearn.tree import DecisionTreeClassifier    #decision tree classifier doesn't suppourt on string
data= {
    "hours":[1,2,3,4,5,6,7,8],
    "pass": [0,0,0,1,1,1,1,1]     #0=fail 1=pass, so if it will come 0 it means fail & 1 is pass 
}

df= pd.DataFrame(data)
x=df[["hours"]]
y=df["pass"]

model=DecisionTreeClassifier()
model.fit(x,y)
Result=model.predict([[3.5]])
print(Result[0])


