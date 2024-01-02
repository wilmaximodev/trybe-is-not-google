def exists_word(word, instance):
    result_list = []

    # Itera sobre cada arquivo na fila
    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []

        # Itera sobre cada linha do arquivo
        for line_number, line in enumerate(
                file_data["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_number})

        if occurrences:
            result_list.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result_list


def search_by_word(word, instance):
    result_list = []

    # Itera sobre cada arquivo na fila
    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []

        # Itera sobre cada linha do arquivo
        for line_number, line_content in enumerate(
                file_data["linhas_do_arquivo"], start=1):
            # Realiza a busca case-insensitive na linha
            if word.lower() in line_content.lower():
                # Adiciona informações da ocorrência à lista
                occurrences.append(
                    {"linha": line_number, "conteudo": line_content})

        if occurrences:
            result_list.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result_list
