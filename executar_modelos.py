#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para executar todos os modelos de análise de sentimento
e mostrar resultados comparativos.
"""

import os
import sys
import subprocess
import time
from collections import OrderedDict

def print_header(message):
    """Imprime uma mensagem de cabeçalho formatada."""
    print("\n" + "="*80)
    print(" " + message.center(78))
    print("="*80 + "\n")

def run_command(command):
    """Executa um comando e retorna a saída."""
    print("> Executando: " + command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out, err, process.returncode

def parse_accuracy(output):
    """Extrai a precisão da saída do modelo."""
    if isinstance(output, bytes):
        output = output.decode('utf-8')
    
    lines = output.split('\n')
    for line in lines:
        if 'Correct' in line and '%' in line:
            # Tenta extrair o valor de precisão
            try:
                return float(line.split('=')[1].strip().replace('%', ''))
            except:
                return None
    return None

def check_processed_files():
    """Verifica se os arquivos pré-processados estão presentes."""
    required_files = [
        'twitter_cleaned-processed.csv',
        'twitter_cleaned-processed-freqdist.pkl',
        'twitter_cleaned-processed-freqdist-bi.pkl'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    return missing_files

def main():
    print_header("ANÁLISE DE SENTIMENTO EM TWEETS")
    
    # Verifica se estamos no ambiente Anaconda correto
    if not os.environ.get('CONDA_DEFAULT_ENV') == 'twitter-sentiment':
        print("ATENÇÃO: Você não parece estar no ambiente 'twitter-sentiment'.")
        print("Execute 'conda activate twitter-sentiment' antes de executar este script.")
        choice = raw_input("Deseja continuar mesmo assim? (s/n): ")
        if choice.lower() != 's':
            return
    
    # Verifica arquivos pré-processados
    missing_files = check_processed_files()
    if missing_files:
        print("AVISO: Os seguintes arquivos pré-processados estão faltando:")
        for file in missing_files:
            print("  - " + file)
        
        print("\nPode ser necessário executar o pré-processamento primeiro:")
        print("  python code/preprocess.py twitter_cleaned.csv")
        print("  python code/stats.py twitter_cleaned-processed.csv")
        
        choice = raw_input("\nDeseja continuar mesmo assim? (s/n): ")
        if choice.lower() != 's':
            return
    
    # Modelos a serem executados
    models = OrderedDict([
        ('Baseline', 'python code/baseline.py'),
        ('Naive Bayes', 'python code/naivebayes.py'),
        ('SVM', 'python code/svm.py'),
        ('Random Forest', 'python code/randomforest.py'),
        ('Decision Tree', 'python code/decisiontree.py')
    ])
    
    # Armazena resultados
    results = {}
    
    # Executa cada modelo
    for name, command in models.items():
        print_header("Executando modelo: " + name)
        start_time = time.time()
        
        out, err, code = run_command(command)
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        if code != 0:
            print("\nERRO ao executar o modelo " + name + ":")
            print(err.decode('utf-8'))
            results[name] = "ERRO"
        else:
            accuracy = parse_accuracy(out)
            if accuracy:
                results[name] = accuracy
                print("\n> Precisão: {:.2f}%".format(accuracy))
            else:
                results[name] = "N/A"
                print("\n> Não foi possível determinar a precisão")
            
        print("> Tempo de execução: {:.2f} segundos".format(elapsed))
    
    # Mostra resultados comparativos
    print_header("RESULTADOS COMPARATIVOS")
    
    # Ordena resultados por precisão (do maior para o menor)
    sorted_results = sorted(
        [(name, score) for name, score in results.items() if isinstance(score, (int, float))],
        key=lambda x: x[1],
        reverse=True
    )
    
    # Adiciona os resultados não numéricos ao final
    sorted_results.extend(
        [(name, score) for name, score in results.items() if not isinstance(score, (int, float))]
    )
    
    # Imprime tabela
    print("| {:^20} | {:^15} |".format("Modelo", "Precisão (%)"))
    print("|" + "-"*22 + "|" + "-"*17 + "|")
    
    for name, score in sorted_results:
        if isinstance(score, (int, float)):
            print("| {:20} | {:15.2f} |".format(name, score))
        else:
            print("| {:20} | {:^15} |".format(name, score))
    
    print("\nConclusão: O modelo com melhor desempenho foi '{}'".format(sorted_results[0][0]))

if __name__ == "__main__":
    main() 