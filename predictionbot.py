import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()

genai_key=os.getenv("Gemini_API_Key")

if genai_key is None:
    raise Exception("API is missing")
else:
    print(genai_key[:0])   #8 is showing the the first 7 letters from the key

client=genai.Client(api_key=genai_key)
chat = client.chats.create(
    model="gemini-2.5-flash",
    config= {"system_instruction":"you are word and sentence predictor chatbot"}
)               


Question="How was your day?"
while True:
    user = input ("Question:")

    if user.lower()=="quit":
        print ("Bot: Bbyee")
        break
    response=chat.send_message(user)
    print ("Bot:", response.text)

