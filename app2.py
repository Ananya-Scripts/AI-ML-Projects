import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

#we will load json data
with open("hello.json") as file:
    data= json.load(file)


#variable x for user request and variable y for bot response store

x=[]
y=[]

#for data extraction
for intent in data ["intents"]:
    for pattern in intent ["patterns"]:
        x.append (pattern)
        y.append (intent["tag"])

#text to number conversion
vectorizer = CountVectorizer()
x_vector = vectorizer.fit_transform(x)

#model training
model = LogisticRegression()
model.fit(x_vector,y)

#chat function
def chatbot(user_input):
    input_vector = vectorizer.transform([user_input])

    if input_vector.sum()==0:
        return"sorry"

    prediction = model.predict(input_vector) 

    for intent in data ["intents"]:
        if intent ["tag"]== prediction:
            return random.choice(intent["responses"])
    return"sorry"

print("I am running")

while True:
    user = input("you:")

    if user.lower()== "I'm done":
        print ("Bot: Byee")
        break
    response = chatbot(user)
    print ("Bot:", response)

