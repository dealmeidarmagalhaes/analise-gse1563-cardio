import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Carregar os resultados, usando bibliotecas mat e seaborn que facilitam na criação de visualização em python
try:
    df = pd.read_csv("genes_candidatos.csv")
    
    top_up = df.head(5)
    top_down = df.tail(5)
    plot_data = pd.concat([top_up, top_down])
   
    plt.figure(figsize=(12, 7))
    sns.set_theme(style="whitegrid")
    
    colors = ['#d73027' if x > 0 else '#4575b4' for x in plot_data['LFC']]
    
    sns.barplot(
        x='LFC', 
        y='Gene Symbol', 
        data=plot_data, 
        palette=colors
    )

    #com o objetivo de comparar os top 5 mais e menos ativos
    plt.title('Top 10 Genes Diferencialmente Expressos (GSE1563)', fontsize=15, pad=20)
    plt.xlabel('Log2 Fold Change (Mudança de Expressão)', fontsize=12)
    plt.ylabel('Gene Symbol', fontsize=12)

    
    plt.axvline(0, color='black', lw=1.5, ls='--')

    
    plt.tight_layout()
    plt.savefig('resultado_genes.png', dpi=300)
    print("\n Sucesso! O arquivo 'resultado_genes.png' foi criado na pasta.")

except Exception as e:
    print(f" Erro ao gerar gráfico: {e}")
