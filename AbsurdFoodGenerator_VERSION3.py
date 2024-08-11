from openai import OpenAI
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

client = OpenAI(api_key='INSERT_API_KEY_HERE')


def generate_and_display():
    message = "Generate me a really weird, disgusting and absurd food combination. Make it really random, it can from whatever you want. Please, DO NOT generate food combinations with chocolate-covered anchovies, gummy worms and whiped cream! For example: Salted banana with wasabi."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    absurdfoodtext = response.choices[0].message.content
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, absurdfoodtext)

    dalle_response = client.images.generate(
        prompt=absurdfoodtext,
        n=1,
    )
    image_url = dalle_response.data[0].url

    response = requests.get(image_url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)

    image_label.config(image=img)
    image_label.image = img


root = tk.Tk()
root.title("Absurd Food Generator")

generate_button = tk.Button(root, text="Generate Absurd Food", command=generate_and_display)
generate_button.pack()

text_output = tk.Text(root, height=5, width=50)
text_output.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()