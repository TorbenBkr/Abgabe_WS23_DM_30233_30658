import pandas as pd
from scipy.stats import shapiro

# CSV-Datei einlesen und erste Zeile ignorieren
data = pd.read_csv('./output.csv', delimiter=',')

# Spalte auswählen, die überprüft werden soll
for i in range(1, len(data.columns)):
    column = data.iloc[:, i]

    # Shapiro-Wilk-Test durchführen
    statistic, p_value = shapiro(column)
    print(p_value)

    # Ergebnis ausgeben
    if p_value > 0.05:
        print("Die Daten sind wahrscheinlich normalverteilt.")
    else:
        print("Die Daten sind wahrscheinlich nicht normalverteilt.")