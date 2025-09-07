#coraçao do projeto 
#Carregar os agentes do YAML

#Criar os agentes dinamicamente

#Definir as tarefas que cada agente vai executar

#Executar a “crew” (equipe de agentes)
import yaml
from crewai import Crew, Agent
from tools.custom_tool import custom_tool
from crewai.llms import gemini_pro
from crewai.knowledge import JSONKnowledgeBase

# Base de conhecimento
arquivo = "mock_catalog.json"

# Criar LLM
llm = gemini_pro(model="gemini-pro", temperature=0.7)


class LatestAiDevelopment:
    def __init__(self):
        self.crew = self._build_crew()

    def _build_crew(self):
        # Carrega os agentes do YAML
        with open("agents.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # Lista para armazenar os agentes
        agentes = []

        # Cria os agentes dinamicamente
        for nome, atributos in data.items():
            agentes.append(Agent(
                role=atributos.get("role", nome),
                goal=atributos.get("goal", ""),
                backstory=atributos.get("backstory", ""),
                tools=[custom_tool] if nome == "catalog_researcher" else [],
                verbose=True
            ))

        # Define tarefas associadas aos agentes
        tasks = [
            {"agent": agentes[0], "description": "Pesquisar title, author, imprint, release_date, availability"},
            {"agent": agentes[1], "description": "Gerar resumo do livro"},
            {"agent": agentes[2], "description": "Pesquisar melhores ofertas: preço, frete, site de compra"},
            {"agent": agentes[3], "description": "Simular abertura de ticket"}
        ]

        return Crew(agents=agentes, tasks=tasks, verbose=True)

    def kickoff(self):
        try:
            result = self.crew.kickoff()
            print("Resultado da equipe:", result)
            return result
        except Exception as e:
            print("Erro ao executar a equipe:", e)
            return None


# Exemplo de execução
if __name__ == "__main__":
    ai_dev = LatestAiDevelopment()
    ai_dev.kickoff()
