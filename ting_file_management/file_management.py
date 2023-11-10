import sys
import os.path


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
    if not path_file.endswith("txt"):
        print("Formato inválido", file=sys.stderr)
        return

    with open(path_file, "r") as file:
        data = file.read()
        content = data.splitlines()
    return content
# https://pt.stackoverflow.com/questions/2823/como-checar-se-um-arquivo-existe-usando-python
# https://www.w3schools.com/python/ref_file_read.asp
# https://pt.stackoverflow.com/questions/2823/como-checar-se-um-arquivo-existe-usando-python
# https://www.w3schools.com/python/ref_string_endswith.asphttps://pt.stackoverflow.com/questions/2823/como-checar-se-um-arquivo-existe-usando-python
# monitoria ana laura
