#!/usr/bin/env python
import os
from agents.catalog_agent import CatalogAgent
from agents.purchase_agent import PurchaseAgent
from agents.support_agent import SupportAgent
from agents.llm_agent import LLMAgent

API_KEY = os.environ.get("GEMINI_API_KEY")

def main():
    # Verifica se a chave de API está definida
    if not API_KEY:
        print("Erro: GEMINI_API_KEY não definida.")
        return

    # Inicializa os agentes
    catalog_agent = CatalogAgent()
    purchase_agent = PurchaseAgent()
    support_agent = SupportAgent()
    llm_agent = LLMAgent(API_KEY)

    # Entrada do usuário
    user_input = input("Qual livro você quer consultar? ")
    book = catalog_agent.find_book(user_input)

    # Livro encontrado
    if book:
        print(f"\nTítulo: {book.get('title', 'N/A')}")
        print(f"Autor: {book.get('author', 'N/A')}")
        print("Resumo (LLM):", llm_agent.summarize(book.get("summary", "")))
        print(f"Preço: R${book.get('price', 'N/A')}")
        print("Links para compra:", purchase_agent.get_purchase_links(book))
    # Livro não encontrado
    else:
        print("Livro não encontrado. Deseja abrir um ticket de suporte? (s/n)")
        if input().lower() == "s":
            print(support_agent.open_ticket(user_input))

if __name__ == "__main__":
    main()
