from bs4 import BeautifulSoup

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

vitorias = 0

for linha in soup.find("table", {"id": "jogo"}).find_all("tr")[1:]:
    j1 = linha.find_all("td")[0].text
    j2 = linha.find_all("td")[1].text
    
    if (j1 == "Pedra" and j2 == "Tesoura") or \
       (j1 == "Tesoura" and j2 == "Papel") or \
       (j1 == "Papel" and j2 == "Pedra"):
        vitorias += 1

print(f"O Jogador 1 venceu {vitorias} vezes.")