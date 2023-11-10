def exists_word(word, instance):
    results = []
    for index in range(len(instance)):

        file_lines = instance.search(index)["linhas_do_arquivo"]
        file_name = instance.search(index)["nome_do_arquivo"]

        occurrences = [
            {"linha": i + 1}
            for i, linha in enumerate(file_lines)
            if word.lower() in linha.lower()
        ]

        if occurrences:
            if any(occur["linha"] for occur in occurrences):
                results.append(
                    {
                        "palavra": word,
                        "arquivo": file_name,
                        "ocorrencias": occurrences,
                    }
                )
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
