from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot():
    print("word & sentence prediction Chatboot (type 'exit' to quit)\n")

    while True:
        user_input = input("you:")

        if user_input.lower() == "exit":
            print("Bot:Goodbye")
            break

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "You are very helpful assistant that predicts completes sentences"},
                {"role": "user", "content": user_input}],
                max_tokens=100,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            print("Bot:", reply)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chatbot()
