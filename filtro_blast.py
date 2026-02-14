import re
from datetime import datetime
import os

def gerar_laudo(gene_alvo, linhagem_detectada):
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_arquivo = f"laudo_{gene_alvo}.txt"
    
    with open(nome_arquivo, "w") as laudo:
        laudo.write(f"--- RELATÓRIO DE BIOINFORMÁTICA ---\n")
        laudo.write(f"Data da análise: {data_atual}\n")
        laudo.write(f"Gene Alvo: {gene_alvo}\n")
        laudo.write(f"Resultado: POSITIVO\n")
        laudo.write(f"Detalhe: {linhagem_detectada}\n")
        laudo.write(f"------------------------------------\n")
    return nome_arquivo

# --- INÍCIO DO PROGRAMA ---
print("=== SISTEMA AUTOMATIZADO DE TRIAGEM CARD ===")
alvo = input("Qual gene você deseja buscar? (Ex: NDM-1, KPC, OXA-48): ").upper()

caminho_input = "/home/ricardo/resultado_real.txt"
encontrado = False

if not os.path.exists(caminho_input):
    print(f"Erro: Arquivo {caminho_input} não encontrado!")
else:
    with open(caminho_input, "r") as arquivo:
        for linha in arquivo:
            # Busca dinâmica com o que o usuário digitou
            if linha.startswith(">") and re.search(rf"{alvo}\b", linha):
                gene_completo = linha.replace(">", "").strip()
                print(f"\n✅ SUCESSO: O gene {alvo} foi localizado!")
                
                nome_laudo = gerar_laudo(alvo, gene_completo)
                print(f"📄 Laudo gerado: {nome_laudo}")
                
                encontrado = True
                break

    if not encontrado:
        print(f"\n❌ O gene {alvo} não foi encontrado no arquivo de BLAST.")

