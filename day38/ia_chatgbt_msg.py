from openai import OpenAI
from dontenv import load_dotenv
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_completions = client.chat.completions.create(
    messages=[
        {
        "role": "user",
        "content": "Hello, how are you?"}
        ],
        model="gbt-4o"
    )

print(chat_completions.choices[0].message.content)