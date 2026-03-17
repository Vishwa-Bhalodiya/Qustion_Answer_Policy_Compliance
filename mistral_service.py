import os
from mistralai import Mistral

# Set your API key as environment variable
# export MISTRAL_API_KEY="your_api_key"
# or set in .env

api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)


def call_mistral(prompt: str):
    """
    Sends prompt to Mistral model and returns response text.
    """

    try:
        response = client.chat.complete(
            model="mistral-large-latest",  
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )
        print(response)  
        
        return response.choices[0].message.content

    except Exception as e:
        print("Mistral Error:", e)
        return None