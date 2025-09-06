import yaml
from crewai import Crew, Agent
from tools.crew import LatestAiDevelopment
from tools.custom_tool import LatestAiDevelopment
from tools.custom_tool import custom_tool
from crewai.llms import gemini_pro
from crewai.knowledge import JSONKnowledgeBase
#knolwedge
arquivo = "mock_catalog.json"

#criar LLM
llm =LLM(model="gemmini-pro", temperature=0.7)

@CrewAIDevelopment
class LatestAiDevelopment:
    def __init__(self):
        self.crew = self._build_crew()

    def _build_crew(self):
        # Carrega os agentes do YAML
        with open("agents.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # Cria os agentes dinamicamente
        agentes = "config/agents.yaml"
        tasks ="config/tasks.yaml"
        for nome, atributos in data.items():
            agentes.append(Agent(
                role=atributos.get("role", nome),
                goal=atributos["goal"],
                backstory=atributos["backstory"],
                tools=[custom_tool] if nome == "catalog_resercher" else [],
                verbose=True
            ))

        # Define tarefas 
        tasks = [
            {"agent": agentes[0], "description": "Pesquisar title,author,imprint,relese_date,synopsis,avalabilyty"},
            {"agent": agentes[1], "description": "Gerar resumo do livro"},
            {"agent": agentes[2], "description": "Pesquisar melhores ofertas, preço, frete, site comprar"},
            {"agent": agentes[3], "description": "Simular abertura de ticket"}
        ]

        return Crew(agents=agentes, tasks=tasks, verbose=True)

    def kickoff(self):
        result = self.crew.kickoff()
        print("Resultado da equipe:", result)
        return result