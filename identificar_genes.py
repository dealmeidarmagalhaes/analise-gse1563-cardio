import GEOparse
import pandas as pd

# 1. Carregar o arquivo, script mais robusto afim de encontrar e relacionar os dados obrtidos a genes
gse = GEOparse.get_GEO(filepath="./GSE1563_family.soft.gz")
plataforma = list(gse.gpls.values())[0]

print("Colunas disponíveis na plataforma:", plataforma.table.columns)


coluna_nome = [c for c in plataforma.table.columns if 'Symbol' in c or 'SYMBOL' in c]
coluna_nome = coluna_nome[0] if coluna_nome else 'ID'

tabela_traducao = plataforma.table[['ID', coluna_nome]]

df_expressao = pd.read_csv("dados_expressao.csv")
# Garantir que a coluna de ID se chama 'ID' para o merge, senão nãoé possivel mapear e relacionar dados aos genes
if 'ID' not in df_expressao.columns:
    df_expressao.rename(columns={df_expressao.columns[0]: 'ID'}, inplace=True)

resultado = df_expressao.merge(tabela_traducao, on='ID', how='left')

# 5. Salvar
resultado.to_csv("dados_identificados.csv", index=False)
print(f"\n✅ Nova tentativa concluída usando a coluna: {coluna_nome}")
print(resultado.head())
