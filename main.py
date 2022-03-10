from src.scraper import Scraper


def main():
    name = "Япония"
    with open(f"data/{name}.html", "r", encoding="utf-8") as f:
        text = f.read()
        df = Scraper(text).start()
        df.to_excel(f"data/{name}.xlsx", index=False)