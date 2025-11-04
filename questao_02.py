import pandas as pd

negocios = pd.Series([1200, 17500, 14300, 16000, 19500],
                     index = ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen",
                              "Micheal Corleone"])

print(negocios.sum())
print(negocios.mean())
mais_arrecadou = negocios.max()
print(negocios.idxmax())

print(negocios[negocios > negocios.mean()])