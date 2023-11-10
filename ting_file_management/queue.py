from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        
        self._list.append(value)
        return self._list

    def dequeue(self):
      
        return self._list.pop(0)

    def search(self, index):
       
        if index < 0 or index > len(self._list) - 1:
           
            raise IndexError('Índice Inválido ou Inexistente')
        return self._list[index]
