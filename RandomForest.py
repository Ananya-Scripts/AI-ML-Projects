import pandas as pd
from sklearn.ensemble import RandomForestClassifier
 #it works on major votes like if we have 4 false and 5 true then it will give 5 true not 4 false
data= {
    "hours_study":[1,2,3,4,5,6,7,8],
    "sleep_hours":[8,7,6,6,5,5,4,4],
    "pass":[0,0,0,1,1,1,1,1]
}
df=pd.DataFrame(data)
x=df[["hours_study","sleep_hours"]]
y=df["pass"]

model=RandomForestClassifier(n_estimators=10)  #estimator gives major result from the values
model.fit(x,y)
Result=model.predict([[4,6]])
print(Result[0])  #0 is a paramenter that giver integer value & not list