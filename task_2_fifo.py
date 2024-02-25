"""
На языке Python написать минимум по 2 класса реализовывающих
циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.
Оценивается:
Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""


class CircularBuffer1:

    def __init__(self, size):
        self.size = size
        self.buffer = []

    def is_empty(self):
        # Возращвет True если пусто, False если нет
        return len(self.buffer) == 0

    def is_full(self):
        # Возращвет True если буфер полон, False если нет
        return len(self.buffer) == self.size

    def enqueue(self, value):
        # Ставим данные в очередь
        if self.is_full():
            self.buffer.pop(0)  # удаление самого старого элемента при переполнении
        self.buffer.append(value)

    def dequeue(self):
        # Убираем данные из очереди(первый элемент)
        if self.is_empty():
            return None
        return self.buffer.pop(0)


class CircularBuffer2:

    def __init__(self, buff_size):
        self.buff_size = buff_size
        self.buffer = [None] * buff_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.buff_size == 0

    def is_full(self):
        return self.buff_size == self.buff_size

    def enqueue(self, value):
        if self.is_full():
            self.head = (self.head + 1) % self.size  # переход к следующему индексу по модулю
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.size -= 1
        return value


if __name__ == "__main__":
    test_buffer1 = CircularBuffer1(5)
    test_buffer1.enqueue(10)
    test_buffer1.enqueue(20)
    print(test_buffer1.is_empty())
    print(test_buffer1.is_full())
    print(test_buffer1.buffer)
    test_buffer1.enqueue(11)
    test_buffer1.enqueue(23)
    test_buffer1.enqueue(555)
    test_buffer1.enqueue(999)
    test_buffer1.enqueue(17)
    test_buffer1.enqueue(29)
    test_buffer1.enqueue(1)
    test_buffer1.enqueue(0)
    print(test_buffer1.is_empty())
    print(test_buffer1.is_full())
    print(test_buffer1.buffer)
    test_buffer1.dequeue()
    test_buffer1.dequeue()
    print(test_buffer1.buffer)
