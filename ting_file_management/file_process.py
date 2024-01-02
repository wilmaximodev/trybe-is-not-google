import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    lines = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    if file_data in instance.queue:
        return None

    instance.enqueue(file_data)

    sys.stdout.write(f"{file_data}\n")


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        removing = instance.dequeue()
        if removing:
            print(
                f"Arquivo {removing['nome_do_arquivo']} removido com sucesso"
            )
        else:
            print("Não há elementos")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    index_search = len(instance)
    if position > index_search:
        return sys.stderr.write("Posição inválida")

    return sys.stdout.write(f"{instance.search(position)}")
