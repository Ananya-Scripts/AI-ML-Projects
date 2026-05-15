import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data={
    "A": [10,12,18,20,25,36,42,46,55]
}

df= pd.DataFrame(data)
print("Raw Data")
# print(df)

x=df[["A"]]
x_train,x_test = train_test_split(x,test_size=0.1, random_state=60)
print(x_train)




