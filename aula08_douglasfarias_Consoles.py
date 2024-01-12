import pandas as pd

# 1. Abra o arquivo "best-selling game consoles.xlsx" em um dataframe.

baseConsoles = "C:\\Users\\dougl\\OneDrive\\Documentos\\Coderhouse\\Cientista de dados\\02_Python\\02_Desafios\\02_desafios\\aula08\\best-selling_game_consoles.xlsx"
consoles = pd.read_excel(baseConsoles, sheet_name="consoles")

#2. Substitua a palavra "NES" por "Nintendinho" no nome dos consoles e deixe todos os nomes em maiúsculos.
print("Etapa 2\ - Substituição NESn")

consoles["Console Name"] = consoles["Console Name"].str.replace(r"(?<!\w)NES(?!\w)","Nintendinho", regex=True).str.upper()

print (consoles["Console Name"])

print("\n####################################################################\n") #quebra de linha

#3. Filtre o nome dos consoles com data de release depois de 2010.
print("Etapa 3 - Filtro RELEASE YEAR\n")

consoles3 = consoles[consoles["Released Year"] > 2010]

print(consoles3)

print("\n####################################################################\n") #quebra de linha

#4. De um describe e info da base, substitua os missing values pela string "missing".
print("Etapa 4 - Describe, Info e missing values\n")

print(consoles.info())
print("\n############################\n") #quebra de linha

print(consoles.describe())
print("\n############################\n") #quebra de linha

consoles4 = consoles.fillna("Missing")

print(consoles4)

print("\n####################################################################\n") #quebra de linha

#5. Filtre os consoles que foram descontinuados a menos de 2 anos da data de release.
print("Etapa 5 - Filtro de descontinuidade\n")

consoles["Continuidade"] = consoles["Discontinuation Year"] - consoles["Released Year"]

consoles5 = consoles[consoles["Continuidade"] >=2]

print(consoles5)

print("\n####################################################################\n") #quebra de linha

#FINAL - Todas as condições juntas
print("RESULTADO FINAL\n")

consoles["Continuidade"] = consoles["Discontinuation Year"] - consoles["Released Year"]

filtroRelease = consoles["Released Year"] > 2010
filtroContinuidade = consoles["Continuidade"] >=2

consolesFinal = consoles[filtroRelease & filtroContinuidade]

print (consolesFinal)


