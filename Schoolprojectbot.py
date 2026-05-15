import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import json

with open ("schoolproject.json") as file:
    class_data=json.load(file)

with open ("SchoolInfo.json") as file:
    school_data=json.load(file)

x=[]
y=[]

training_data=[
    ("school details","school"),
    ("tell me school info", "school"),
    ("principal name", "school"),
    ("timing","school"),
    ("contact number", "school"),
    ("student details","student"),
    ("class info", "student"),
    ("teacher", "student"),
    ("class1 teacher","student")
]

for pattern,tag in training_data:
    x.append(pattern)
    y.append(tag)

vectorizer=CountVectorizer()
X=vectorizer.fit_transform(x)

model=RandomForestClassifier()
model.fit(X,y)

def predict_intent(text):
    inp=vectorizer.transform([text])
    return model.predict(inp)[0]

def get_school_data():
    info=school_data["school_info"][0]

    return{
        "principal":info["Principal Name"][0],
        "timing":info["Timing"][0],
        "PTM":info["P.T.M Days"][0],
        "Contact":info["School_care"][0]
    }

def get_classes():
    return list(class_data["class"][0].key())

def get_teachers(class_name):
    classes=class_data["class"][0]

    if class_name in classes:
        return classes[class_name]["Teacher"]
    else:
        return None





    



