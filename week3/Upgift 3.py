import numpy as np
import pandas as pd

# Ladda CSV-filen
df = pd.read_csv("python/Anaconda/Ny mapp/my_pandas_script.py.csv")

# Dynamiskt beräkna antalet prover (rader) och kolumner
samples = df.shape[0]  # Antal rader (prover)
columns = df.shape[1]  # Antal kolumner

# Skriv ut antalet prover och kolumner
print("Number of samples (rows):", samples)
print("Number of columns:", columns)

# Använd describe för att få en sammanfattad vy av datasetet
print(df.describe())

# Funktion för att räkna andelen NaN-värden i varje kolumn
def count_nan():
    # För varje kolumn i datasetet, använd isna() och summera de saknade värdena
    # Dividera med det totala antalet rader och multiplicera med 100 för att få procent
    for col in df.columns:
        missing_percentage = df[col].isna().sum() / samples * 100
        print(f"The column {col} is missing {missing_percentage:.2f}% of data!")
        
# Kör funktionen för att räkna NaN-värden
count_nan()

# 1. Extrahera alla rader som har NaN-värden
nan_samples = df[df.isna().any(axis=1)]

# 2. Få indexen för dessa rader
nan_indexes = nan_samples.index

# 3. Ta bort dessa rader från dataframe
df = df.dropna()

# Kör count_nan igen för att se hur datasetet ser ut efter att NaN-rader tagits bort
count_nan()

# Funktion för att normalisera värden i en kolumn
def normalize_values(col_value, min_val, max_val):
    normalized_val = (col_value - min_val) / (max_val - min_val)
    return normalized_val

# Main-funktion för att normalisera alla kolumner
def main():
    for column in df.columns:
        min_val = df[column].min()
        max_val = df[column].max()
        df[column] = df[column].apply(normalize_values, args=(min_val, max_val))

# Kör main-funktionen
main()

# Visa en sammanfattad beskrivning av det normaliserade datasetet
print(df.describe())
