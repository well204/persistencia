import pandas as pd

negocios = pd.Series([1200, 17500, 14300, 16000, 19500],
                     index = ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen",
                              "Micheal Corleone"])

total_arrecadado = negocios.sum()
media_receitas = negocios.mean()
associado_mais_recebeu = negocios.idxmax()


print(f"Total arrecadado na semana: {total_arrecadado}")
print(f"Média das receitas: {media_receitas}")
print(f"Associado que mais recebeu: {associado_mais_recebeu}")
print("\n")
print(negocios[negocios > negocios.mean()])