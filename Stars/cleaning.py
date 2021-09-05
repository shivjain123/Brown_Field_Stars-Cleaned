import pandas as pd

df = pd.read_csv("D:/(4) WhiteHatJr/Third Module/Web Scraping and Analysis/Stars/merged.csv")

#print(df.columns)

del df["Unnamed: 0"]
del df["Unnamed: 5"]
del df["Name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

df = df.dropna()

df.to_csv('D:/(4) WhiteHatJr/Third Module/Web Scraping and Analysis/Stars/cleaned.csv')