# Guia de Execução - Análise de Sentimento em Tweets

Este guia explica como executar os modelos de análise de sentimento em tweets usando Python 2.7 com Anaconda.

## Índice
1. [Visão Geral](#visão-geral)
2. [Requisitos](#requisitos)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Pré-processamento](#pré-processamento)
5. [Execução dos Modelos](#execução-dos-modelos)
   - [Script de Execução Automática](#script-de-execução-automática)
   - [Execução Manual](#execução-manual)
6. [Resultados Obtidos](#resultados-obtidos)
7. [Solução de Problemas](#solução-de-problemas)

## Visão Geral

Este projeto realiza análise de sentimento em tweets (classificação binária) usando diferentes algoritmos de aprendizado de máquina. A tarefa é determinar se um tweet expressa um sentimento positivo (1) ou negativo (0).

## Requisitos

- **Anaconda** (recomendado para gerenciamento de pacotes e ambientes)
- **Python 2.7**
- Bibliotecas:
  - numpy
  - scikit-learn
  - scipy
  - nltk
  - singledispatch (dependência do NLTK)

## Configuração do Ambiente

1. **Criar e ativar ambiente Anaconda**:
   ```bash
   # Criar ambiente com Python 2.7
   conda create -n twitter-sentiment python=2.7
   
   # Ativar o ambiente
   conda activate twitter-sentiment
   ```

2. **Instalar dependências**:
   ```bash
   # Instalar dependências principais
   conda install numpy scikit-learn scipy nltk
   
   # Instalar dependência adicional para o NLTK
   pip install singledispatch
   
   # Baixar dados do NLTK
   python -c "import nltk; nltk.download('punkt')"
   ```

## Pré-processamento

1. **Executar pré-processamento dos dados**:
   ```bash
   python code/preprocess.py twitter_cleaned.csv
   ```
   Este comando gera o arquivo `twitter_cleaned-processed.csv`.

2. **Gerar estatísticas e distribuições de frequência**:
   ```bash
   python code/stats.py twitter_cleaned-processed.csv
   ```
   Este comando gera arquivos de distribuição de frequência e exibe estatísticas sobre o conjunto de dados.

## Execução dos Modelos

Antes de executar qualquer modelo, certifique-se de que:
- O ambiente Anaconda está ativado (`conda activate twitter-sentiment`)
- Os dados foram pré-processados conforme as etapas acima
- O caminho dos arquivos em cada script está correto (arquivos com prefixo `twitter_cleaned-processed`)

### Script de Execução Automática

Para facilitar, criamos um script que executa todos os modelos sequencialmente e apresenta um relatório comparativo:

```bash
# Ative o ambiente primeiro
conda activate twitter-sentiment

# Execute o script
python executar_modelos.py
```

O script verifica automaticamente:
- Se você está no ambiente conda correto
- Se os arquivos de pré-processamento existem
- Executa cada modelo e coleta os resultados
- Apresenta um relatório comparativo de precisão

### Execução Manual

Alternativamente, você pode executar cada modelo manualmente conforme descrito abaixo:

### Modelo Baseline

```bash
python code/baseline.py
```

### Naive Bayes

```bash
python code/naivebayes.py
```

### SVM (Support Vector Machine)

```bash
python code/svm.py
```

### Random Forest

```bash
python code/randomforest.py
```

### Árvore de Decisão (Decision Tree)

```bash
python code/decisiontree.py
```

## Resultados Obtidos

Abaixo estão os resultados de precisão obtidos para cada modelo:

| Modelo            | Precisão (%)  |
|-------------------|---------------|
| Random Forest     | 91.52         |
| Naive Bayes       | 89.37         |
| SVM               | 89.28         |
| Árvore de Decisão | 74.53         |
| Baseline          | 68.94         |

## Solução de Problemas

### Python 2.7 obsoleto
O Python 2.7 atingiu o fim da vida útil em janeiro de 2020. O código está adaptado para esta versão e pode apresentar avisos de obsolescência.

### Problemas com TensorFlow/Keras
Para modelos neurais (CNN, LSTM), é necessário TensorFlow e Keras, que são difíceis de instalar para Python 2.7. Para estes modelos, recomenda-se:
- Criar um ambiente Anaconda separado com Python 3
- Adaptar os scripts para compatibilidade com Python 3

### Erros de importação
Se ocorrerem erros de "module not found", verifique se todas as dependências foram instaladas corretamente no ambiente Anaconda.

### Outros problemas
- Certifique-se de que os caminhos dos arquivos em cada script estão apontando para os arquivos corretos gerados nas etapas de pré-processamento
- Para arquivos grandes, ajuste o parâmetro `batch_size` se necessário

---

Este guia foi criado para facilitar a execução dos modelos de análise de sentimento em tweets. Para mais detalhes sobre os algoritmos e implementação, consulte o relatório completo do projeto disponível em `docs/`. 