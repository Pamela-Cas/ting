from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)
    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": (file),
        }
    instance.enqueue(data)
    sys.stdout.write(str(data))

def remove(instance):

    if len(instance) == 0:
        print("Não há elementos")
        return
    delete = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {delete} removido com sucesso\n")

def file_metadata(instance, position):
    try:
        data = instance.search(position)
        file = sys.stdout
        print(data, file)

    except IndexError:
       index_error = sys.stderr.write("Posição inválida")
       print(index_error)