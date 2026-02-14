import pandas as pd
import numpy as np

# 1. Carregar dados identificados
df = pd.read_csv("dados_identificados.csv")

# Fold Change entre a primeira e a segunda amostra
# Usamos Log2 para que a diferença seja linear
# Coluna 1 (Amostra A) vs Coluna 2 (Amostra B)
amostra_A = df.columns[0]
amostra_B = df.columns[1]

df['Log2_Fold_Change'] = np.log2(df[amostra_B] + 1) - np.log2(df[amostra_A] + 1)

# 3. Filtrar os genes com diferenças > 2 ou < -2, ou seja, os que mais destacados
genes_importantes = df[df['Log2_Fold_Change'].abs() > 2]

# 4. Ordenar segundo a expressão gênica
genes_importantes = genes_importantes.sort_values(by='Log2_Fold_Change', ascending=False)

genes_importantes.to_csv("genes_candidatos.csv", index=False)
print(f"🧬 Encontramos {len(genes_importantes)} genes com mudança significativa!")
print("\nTop 5 Genes que AUMENTARAM a expressão:")
print(genes_importantes[['Gene Symbol', 'Log2_Fold_Change']].head())
