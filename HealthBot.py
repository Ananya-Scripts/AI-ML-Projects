from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("Hcare1.json") as f1, open("Healthcare2.json") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

    hospital = data1["hospital"]
    For_Patients = data2["Doctor_Departments"]


def chatbot(user_input):
    hosp_data = "\n".join([f"{k}:{v}" for k, v in hospital.items()])
    pat_data = "\n".join([f"{k}:{v}" for k, v in For_Patients.items()])
    context = f"Hospital Info:\n{hosp_data}\n\nPatient info:\n{pat_data}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Act Like a Hospital info bot & your name is Doc_Box"},
            {"role": "user", "content": f"{context}\n\nUser question:{user_input}"}
        ]
    )
    return response.choices[0].message.content

while True:
    user = input("You:")
    if user.lower() == "exit":
        break
    print("Bot", chatbot(user))
