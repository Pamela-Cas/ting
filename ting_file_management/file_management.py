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
    return data.splitlines()
