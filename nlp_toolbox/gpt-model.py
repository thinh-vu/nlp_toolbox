import requests
import json

def gpt_api(openai_token, input_text, model="gpt-3.5-turbo"):
    """
    This function takes two parameters for the input: openai_token and input_text then generates the text response from OpenAI GPT model.

    Args:
    openai_token (str): The OpenAI API token.
    input_text (str): The input prompt to generate a response for.

    Returns:
    str: The generated text response.
    """
    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
      "model": model,
      "messages": [
        {
          "role": "user",
          "content": input_text
        }
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {openai_token}'
    }

    r = requests.request("POST", url, headers=headers, data=payload).json()
    response = r['choices'][0]['message']['content']
    return response