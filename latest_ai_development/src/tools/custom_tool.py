from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# Define o esquema de entrada para o uso da ferramenta
class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Descrição do argumento que será processado pela ferramenta.")

# Define a ferramenta personalizada
class MyCustomTool(BaseTool):
    name: str = "My Custom Tool"
    description: str = (
        "Ferramenta personalizada para processar um argumento e retornar uma resposta simulada. "
        "Útil para testes ou demonstrações de integração com agentes CrewAI."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Aqui você pode implementar a lógica real da ferramenta
        return f"Resultado processado para o argumento: '{argument}'"