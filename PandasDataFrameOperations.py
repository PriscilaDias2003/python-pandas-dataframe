
import pandas as pd

# Instruções 1
# Criar um DataFrame com o nome frutas no seguinte formato

frutas = pd.DataFrame({
    'Maçã': [0, 30],
    'Banana': [20, 20]
}, index=['', ''])

#Criar um DataFrame com o nome vendas_frutas no seguinte formato

vendas_frutas = pd.DataFrame({
    'Maçã': [1000, 5000],
    'Banana': [700, 2000]
}, index=['Vendas 2022', 'Vendas 2023'])

# Instruções 
# Carregando o DataFrame a partir de um arquivo CSV

file_path = '/mnt/data/WorldHits.csv'
data = pd.read_csv(file_path)

# Exibindo as primeiras linhas do arquivo para verificar o conteúdo
print(data.head())

# --------------------
# Operações solicitadas no DataFrame
# --------------------

# 1. Tipo de dados de cada coluna
data_types = data.dtypes

# 2. Leitura de valores de uma coluna em específico ('Popularity')
popularity_values = data['Popularity']

# 3. Obter o valor máximo de uma coluna ('Popularity')
max_popularity = data['Popularity'].max()

# 4. Verificar os dados de uma coluna com um determinado valor (máximo de 'Popularity')
tracks_with_max_popularity = data[data['Popularity'] == max_popularity]

# Exibindo os resultados das operações
print("Tipos de dados de cada coluna:\n", data_types)
print("\nPrimeiros valores da coluna 'Popularity':\n", popularity_values.head())
print("\nValor máximo da coluna 'Popularity':", max_popularity)
print("\nDados das faixas com a máxima popularidade:\n", tracks_with_max_popularity)
