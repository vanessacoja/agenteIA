class PurchaseAgent:
    def get_purchase_links(self, book):
        return book.get("links", [])
