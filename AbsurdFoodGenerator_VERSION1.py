import openai

openai.api_key = 'NO YOU WILL NOT STEAL MY API KEY'

# Předurčená zpráva
message = "Generate me a really weird, disgusting and absurd food combination. For example: Salted banana with wasabi."

# Pošle zprávu a získá odpověď
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message}]
)

# Vypíše odpověď do konzole
print(response['choices'][0]['message']['content'])