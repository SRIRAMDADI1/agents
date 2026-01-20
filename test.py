import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

question = input("Ask a question: ")

resp = client.chat.completions.create(
    model="gpt-4o-mini",  
    messages=[{"role": "user", "content": question}],
)   

print(resp.choices[0].message.content)