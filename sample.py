import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data={
    "students": ["A","B","C","D","E"],
    "marks": [30,40, 50,65,75]
}

df=pd.DataFrame(data)

print("chatbot was running")

while True:
    user = input("you :")
    if user.lower()=="quit":
        print ("Bot: goodbye")
        break
    response= chatbot(user)
    print ("Bot:", response)






