import os
import openai  # pip install openai

openai.api_key = ('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')

user_prompt = "versace perfume transparent"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)

# optional
# img_url = "https://www.freepnglogos.com/uploads/perfume-png/perfume-png-transparent-images-png-only-12.png"
# img_name = img_url.split('/')[-1]
# img_name