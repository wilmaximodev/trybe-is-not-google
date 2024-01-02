import sys


def txt_importer(path_file):
    # Verifica se o arquivo possui a extensão .txt
    if not path_file.endswith('.txt'):
        print("Formato inválido. O arquivo deve ter extensão .txt",
              file=sys.stderr)
        return []

    try:
        # Tenta abrir o arquivo em modo de leitura ('r')
        with open(path_file, 'r') as file:
            # Lê todas as linhas do arquivo e as armazena em uma lista
            lines = file.read().split('\n')
            return lines
    except FileNotFoundError:
        # Se o arquivo não for encontrado, imprime uma mensagem de erro
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []
