import openai


class LLMAgent:
    def __init__(self, api_key: str):
        """
        Inicializa o agente de LLM com a chave da API OpenAI.
        """
        openai.api_key = api_key

    def summarize(self, text: str) -> str:
        """
        Solicita ao modelo LLM para resumir o texto fornecido.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Substituir "gemini-free" por um modelo válido
                messages=[{"role": "user", "content": f"Resuma o seguinte texto: {text}"}],
                temperature=0.7
            )
            # Retorna o conteúdo da primeira resposta
            return response.choices[0].message["content"].strip()
        except Exception as e:
            print(f"Erro ao gerar resumo: {e}")
            return ""
