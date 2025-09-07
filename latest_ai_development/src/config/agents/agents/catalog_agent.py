import json
from pathlib import Path

class CatalogAgent:
    def __init__(self, catalog_path="config/books.json"):
        self.catalog_path = Path(catalog_path)
        with open(self.catalog_path, "r", encoding="utf-8") as f:
            self.books = json.load(f)

    def find_book(self, title: str):
        for book in self.books:
            if title.lower() in book["title"].lower():
                return book
        return None