<<<<<<< HEAD
# Análise Comparativa de Sequências via BLAST+ (Microbiologia Médica)

## Descrição
Projeto focado no uso de ferramentas de alinhamento local para identificação de genes de resistência (ARGs) e fatores de virulência em isolados clínicos de ambiente hospitalar.

## Metodologia In Silico
- **Database:** Criação de bancos locais com sequências do **CARD** (Comprehensive Antibiotic Resistance Database).
- **Ferramenta:** Utilização do `blastn` e `blastp` via linha de comando (Linux/WSL).
- **Parâmetros:** Filtro de Identidade > 95% e E-value < 1e-10 para garantir precisão diagnóstica.

## Aplicação
Identificação rápida de plasmídeos contendo genes como *blaKPC*, *blaNDM* e *mcr-1* a partir de dados brutos de sequenciamento de nova geração (NGS).

## Resultados
- `blast_output.txt`: Relatório de alinhamento.
- `pipeline_blast.sh`: Script em Bash para automação das buscas.
=======
Este projeto utiliza ferramentas de Bioinformática (BLAST+) e Python para identificar genes de resistência no banco de dados CARD.

## Ferramentas Utilizadas:
- **BLAST+**: Para alinhamento de sequências.
- **CARD Database**: Banco de dados curado de genes de resistência.
- **Python**: Script automatizado para filtragem de resultados e geração de laudos técnicos.

## Como rodar o filtro:
`python3 filtro_blast.py`
>>>>>>> e2dcc15 (Meu primeiro script de bioinformática com Python)
