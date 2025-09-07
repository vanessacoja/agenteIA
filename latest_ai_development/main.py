#!/usr/bin/env python
import sys
import warnings
import os
from random import randint
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from agents.catalog_agent import CatalogAgent
from agents.purchase_agent import PurchaseAgent
from agents.support_agent import SupportAgent
from agents.llm_agent import LLMAgent
import os

API_KEY = os.environ.get("GEMINI_API_KEY")

def main():
    catalog_agent = CatalogAgent()
    purchase_agent = PurchaseAgent()
    support_agent = SupportAgent()
    llm_agent = LLMAgent(API_KEY)

    user_input = input("Qual livro você quer consultar? ")
    book = catalog_agent.find_book(user_input)

    if book:
        print(f"\nTítulo: {book['title']}")
        print(f"Autor: {book['author']}")
        print("Resumo (LLM):", llm_agent.summarize(book["summary"]))
        print(f"Preço: R${book['price']}")
        print("Links para compra:", purchase_agent.get_purchase_links(book))
    else:
        print("Livro não encontrado. Deseja abrir um ticket de suporte? (s/n)")
        if input().lower() == "s":
            print(support_agent.open_ticket(user_input))

if __name__ == "__main__":
    main()
