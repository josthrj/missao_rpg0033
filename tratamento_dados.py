import pandas as pd
import numpy as np

# 1. Leitura do arquivo CSV
df = pd.read_csv('dados.csv', sep=';', engine='python')

# 2. Verificar se os dados foram importados corretamente
print("\nInformações gerais sobre o DataFrame:")
print(df.info())

print("\nPrimeiras 5 linhas:")
print(df.head())

print("\nÚltimas 5 linhas:")
print(df.tail())

# 3. Criar uma cópia do DataFrame
df_limpo = df.copy()

# 4. Substituir valores nulos na coluna 'Calories' por 0
df_limpo['Calories'].fillna(0, inplace=True)

print("\nVerificação após substituir NaN por 0 em 'Calories':")
print(df_limpo[['ID', 'Calories']])

# 5. Substituir valores nulos na coluna 'Date' por '1900/01/01'
df_limpo['Date'].fillna('1900/01/01', inplace=True)

print("\nVerificação após preencher valores nulos em 'Date':")
print(df_limpo[['ID', 'Date']])

# 6. Tentar converter a coluna 'Date' para datetime (deve falhar)
# print(pd.to_datetime(df_limpo['Date'], format='%Y/%m/%d'))  # Erro proposital

# 7. Substituir '1900/01/01' por NaN para corrigir erro anterior
df_limpo['Date'].replace('1900/01/01', np.nan, inplace=True)

# 8. Tratar valor inválido '20201226' transformando em datetime
df_limpo['Date'].replace('20201226', '2020/12/26', inplace=True)

# 9. Converter coluna 'Date' para datetime
df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], errors='coerce')

print("\nVerificação após conversão para datetime:")
print(df_limpo[['ID', 'Date']])

# 10. Remover linhas com valores nulos (agora, apenas a linha 22)
df_final = df_limpo.dropna()

print("\nDataFrame final, após todas as transformações:")
print(df_final)

# Verificar estrutura final
print("\nInformações finais do DataFrame:")
print(df_final.info())
