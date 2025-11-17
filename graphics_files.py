# Creează un program Python care generează un set de date simplu,

# creează un grafic pe baza datelor și salvează rezultatele în fișiere.


# Importă bibliotecile necesare: pandas, matplotlib.pyplot și numpy.

# Creează un DataFrame cu vânzări lunare pentru 6 luni.
# Coloane: "Luna" și "Vânzări".

# Creează un grafic de tip linie care afișează evoluția vânzărilor.

# Adaugă valori numerice deasupra fiecărui punct din grafic.

# Salvează graficul în fișierul "vanzari_grafic.png".

# Salvează DataFrame-ul în fișiere CSV.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


luni = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie"]
vanzari = np.random.randint(1000, 5000, size=6) 

df = pd.DataFrame({
    "Luna": luni,
    "Vânzări": vanzari
})

print(df)

plt.figure(figsize=(10, 5))
plt.plot(df["Luna"], df["Vânzări"], marker="o")
plt.title("Evoluția vânzărilor pe 6 luni")
plt.xlabel("Luna")
plt.ylabel("Vânzări")

for i, valoare in enumerate(df["Vânzări"]):
    plt.text(i, valoare + 50, str(valoare), ha='center')



plt.savefig("vanzari_grafic.png", dpi=300, bbox_inches="tight")
plt.close()


df.to_csv("vanzari.csv", index=False)
