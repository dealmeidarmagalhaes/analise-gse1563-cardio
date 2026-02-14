import pandas as pd
import numpy as np

# precisei mudar o script, aconteceu erro na identificação de id como primeira coluna, causando erro de str(not 'int'')
df = pd.read_csv("dados_identificados.csv")
col_controle = df.columns[1] 
col_tratado = df.columns[2]

print(f" Analisando mudança: {col_controle} -> {col_tratado}")


ctrl_values = pd.to_numeric(df[col_controle], errors='coerce')
trat_values = pd.to_numeric(df[col_tratado], errors='coerce')

df['LFC'] = np.log2(trat_values + 1) - np.log2(ctrl_values + 1)


candidatos = df[df['LFC'].abs() > 0.5].copy()
candidatos = candidatos.dropna(subset=['Gene Symbol'])
candidatos = candidatos.sort_values(by='LFC', ascending=False)

candidatos.to_csv("genes_candidatos.csv", index=False)

print(f"\n Sucesso! {len(candidatos)} genes analisados.")
print("\nTOP 5 GENES QUE MAIS SUBIRAM:")
print(candidatos[['Gene Symbol', 'LFC']].head())
