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
        print ("Não há elementos")
        return
    
def file_metadata(instance, position):
    """Aqui irá sua implementação"""
