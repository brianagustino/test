import openai
import os
import openai

#openai.api_key = os.getenv("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")
openai.api_key = "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"

MAX_TOKENS = 20
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role":"user", "content":"Get the estimate nutrition value of sate ayam in sate khas senayann"}],
    max_tokens=50
)

def ask_ai(role, message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":role, "content":message}],
    max_tokens=50
    )

print(response)