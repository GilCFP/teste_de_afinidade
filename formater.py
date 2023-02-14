# abre o arquivo de entrada
with open("input.txt", "r") as arquivo_entrada:
    # lê a primeira linha do arquivo de entrada
    nome_arquivo_saida = arquivo_entrada.readline().strip() + ".txt"
    # abre o arquivo de saída
    with open(nome_arquivo_saida.replace(" ","_"), "w") as arquivo_saida:
        # lê cada linha do arquivo de entrada a partir da segunda linha
        arquivo_saida.write(f"{arquivo_entrada.readline().strip()}\n")
        for linha in arquivo_entrada:
            # remove tudo antes do caractere "-" e o espaço subsequente
            linha = linha.split("- ", 1)[-1]
            if not "II" in linha and not "IV" in linha and not "VI" in linha:
                if linha.strip():
                    # escreve a linha no arquivo de saída
                    arquivo_saida.write(linha)
#TODO consertar o split pra que só corte a primeira sequência
