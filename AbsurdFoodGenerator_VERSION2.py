from openai import OpenAI

client = OpenAI(api_key='NOT YOUR API KEY :)')

message = "Generate me a really weird, disgusting and absurd food combination. For example: Salted banana with wasabi."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message}]
)

absurdfoodtext = response.choices[0].message.content
print(absurdfoodtext)

dalle_response = client.images.generate(
    prompt=absurdfoodtext,
    n=1,
)

image_url = dalle_response.data[0].url
print(f"Image URL: {image_url}")