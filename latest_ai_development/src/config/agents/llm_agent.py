import openai

class LLMAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize(self, text):
        response = openai.ChatCompletion.create(
            model="gemini-free",
            messages=[{"role": "user", "content": f"Resuma o seguinte texto: {text}"}],
            temperature=0.7
        )
        return response.choices[0].message["content"]