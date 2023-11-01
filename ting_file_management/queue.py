from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        # adiciona o dado no topo da lista
        self._list.append(value)
        return self._list

    def dequeue(self):
        # remove o dado no topo da lista
        return self._list.pop(0)

    def search(self, index):
        # Se o index for menor que 0 ou maior que a lista
        if index < 0 or index > len(self._list) - 1:
            # retorna a exception erro indexError
            raise IndexError('Índice Inválido ou Inexistente')
        return self._list[index]
